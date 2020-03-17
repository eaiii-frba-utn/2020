# encoding: utf-8
VERSION = 20181217


'''
DESCRIPTION
    This calculator employs the n = 0 sheath helix waveguide mode
    to determine the RF inductance of a single‑layer helical round‑wire air‑core coil.

    Unlike quasistatic inductance calculators, this RF inductance calculator allows for
    more accurate inductance predictions at high frequencies
    by including the transmission line effects apparent with longer coils.

    Furthermore, the calculator closely follows the National Institute of Standards and Technology (NIST)
    methodology for applying round wire and non-uniformity correction factors and
    takes into account both the proximity effect and the skin effect.


USAGE
    See: https://hamwaves.com/inductance/en/index.html


COPYRIGHT
    Copyright (C) 2007-2018  Serge Y. Stroobandt

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


CONTACT
    xdg-open mailto:$(echo c2VyZ2VAc3Ryb29iYW5kdC5jb20K |base64 -d)


TODO
    - Replace fzero by Brent's method: 
        + https://en.wikipedia.org/wiki/Brent's_method
        + http://people.sc.fsu.edu/~jburkardt/py_src/brent/brent.html
        + http://people.sc.fsu.edu/~jburkardt/py_src/brent/zero.py
        + http://www.netlib.org/go/zeroin.f
    - Z_c inf (400, 200, 420, 1, 1)
    - f_res (400, 200, 420, 1, .1) improve seeded guesses?
    - Try fzero for finding f_res.
    - more precise self-resonant frequency
'''


# ## IMPORTS ###


#from browser import document, alert
from math import atan, log, pi, sqrt, tan
from mathextra import cot, I0, I1, K0, K1
from fzero import fzero
import time


# ## CLASSES ###


# +
class Conductor:

    def __init__(self, description, rho, mu_r):
        self.description = description
        self.rho = rho
        self.mu_r = mu_r
        
        
# plating conductivity and permeability
plating = dict()
plating['annealed copper']   = Conductor('annealed copper', 17.241, 0.99999044)
plating['hard-drawn copper'] = Conductor('hard-drawn copper', 17.71, 0.99999044)
plating['silver']            = Conductor('silver', 15.9, 0.9999738)
plating['aluminium']         = Conductor('aluminium', 28.24, 1.00002212)        


# -

class HeaderIndices:

    def __init__(self, header, value):
        '''An object containing a value and its two nearest indices on a table header.'''
        self.value = value

        index2 = 0
        while(value >= header[index2] and index2 < len(header)-1):
            index2 += 1
        self.index2 = index2

        index1 = 0
        if(index2 > 0):
            index1 = index2 - 1
        self.index1 = index1


class Phi_p_d:
    pass    # Used to store interpolation results


# ## GLOBALS ###


c_0 = 299792458.0
mu_0 = pi * 4E-7
Z_0 = mu_0 * c_0





# MEDHURST'S EMPERICAL DATA

# +
# Medhurst matrix lookup rows are l/D.
l_D_header = [0, 0.2, 0.4, 0.6, 0.8, 1, 2, 4, 6, 8, 10, 1E31]

# Medhurst matrix lookup columns are p/d.
p_d_header = [1, 1.111, 1.25, 1.429, 1.667, 2, 2.5, 3.333, 5, 10, 1E31]

# Medhurst matrix
medhurst = []

# l/D ↓          p/d →
medhurst.append([5.31, 3.73, 2.74, 2.12, 1.74, 1.44, 1.20, 1.16, 1.07, 1.02, 1.00])
medhurst.append([5.45, 3.84, 2.83, 2.20, 1.77, 1.48, 1.29, 1.19, 1.08, 1.02, 1.00])
medhurst.append([5.65, 3.99, 2.97, 2.28, 1.83, 1.54, 1.33, 1.21, 1.08, 1.03, 1.00])
medhurst.append([5.80, 4.11, 3.10, 2.38, 1.89, 1.60, 1.38, 1.22, 1.10, 1.03, 1.00])
medhurst.append([5.80, 4.17, 3.20, 2.44, 1.92, 1.64, 1.42, 1.23, 1.10, 1.03, 1.00])
medhurst.append([5.55, 4.10, 3.17, 2.47, 1.94, 1.67, 1.45, 1.24, 1.10, 1.03, 1.00])
medhurst.append([4.10, 3.36, 2.74, 2.32, 1.98, 1.74, 1.50, 1.28, 1.13, 1.04, 1.00])
medhurst.append([3.54, 3.05, 2.60, 2.27, 2.01, 1.78, 1.54, 1.32, 1.15, 1.04, 1.00])
medhurst.append([3.31, 2.92, 2.60, 2.29, 2.03, 1.80, 1.56, 1.34, 1.16, 1.04, 1.00])
medhurst.append([3.20, 2.90, 2.62, 2.34, 2.08, 1.81, 1.57, 1.34, 1.165, 1.04, 1.00])
medhurst.append([3.23, 2.93, 2.65, 2.27, 2.10, 1.83, 1.58, 1.35, 1.17, 1.04, 1.00])
medhurst.append([3.41, 3.11, 2.815, 2.51, 2.22, 1.93, 1.65, 1.395, 1.19, 1.05, 1.00])
# -

# ## FUNCTIONS ###


def lookup_Phi(l, D, p, d):

    l_D = HeaderIndices(l_D_header, l/D)
    p_d = HeaderIndices(p_d_header, p/d)

    # triple linear interpolation
    # h-h1 = (h2-h1) / (x2-x1) * (x-x1)
    # Phi_p_d_index1 = (Phi2 - Phi1) / (l_D.index2 - l_D.index1) * (l/D - l_D.index1) + Phi1
    Phi_p_d.index1  = medhurst[l_D.index2][p_d.index1] - medhurst[l_D.index1][p_d.index1]
    Phi_p_d.index1 /= l_D_header[l_D.index2] - l_D_header[l_D.index1]
    Phi_p_d.index1 *= l/D - l_D_header[l_D.index1]
    Phi_p_d.index1 += medhurst[l_D.index1][p_d.index1]

    Phi_p_d.index2  = medhurst[l_D.index2][p_d.index2] - medhurst[l_D.index1][p_d.index2]
    Phi_p_d.index2 /= l_D_header[l_D.index2] - l_D_header[l_D.index1]
    Phi_p_d.index2 *= l/D - l_D_header[l_D.index1]
    Phi_p_d.index2 += medhurst[l_D.index1][p_d.index2]

    Phi  = Phi_p_d.index2 - Phi_p_d.index1
    Phi /= p_d_header[p_d.index2] - p_d_header[p_d.index1]
    Phi *= p/d - p_d_header[p_d.index1]
    Phi += Phi_p_d.index1
    return Phi


def find_f_res():
    # Secant method root finding algorithm
    # Loosely based upon http://www.see.ed.ac.uk/~jwp/JavaScript/programming/chop2.html
    print(a)
    x_1 = c_0 / l_w_eff / 40
    x_2 = x_1 * 100
    max_tries = 40

    for tries in range(-1, max_tries+1):    # <= max

        if tries == -1:
            x = x_1
            print('x1')
        if tries == 0:
            x = x_2
        if tries > 0:
            x = (x_1 + x_2) / 2

        # First, solve the sheath helix dispersion function for tau at frequency x.
        omega = 2 * pi * x
        k_0 = omega / c_0

        F = lambda tau: K1(tau*a) * I1(tau*a) / K0(tau*a) / I0(tau*a) - (tau / k_0 * tan(psi))**2

        tau_1 = k_0 * cot(psi)**2 - k_0**2    # an estimate
        tau_2 = k_0                           # another estimate
        zero = fzero(F, tau_1, tau_2)
        if zero['error_code'] == 2:
            alert('An error occurred when solving for the resonant frequency.\n'
                + 'However, all shown results are useable.\n\n'
                + zero['error_msg'])
            #document['f_res'].value = ''
        tau = zero['zero']

        # Then, check for resonance.
        # β² = k_0² + τ²
        # βℓ → π/2
        fx = sqrt(k_0**2 + tau**2) * l - pi/2

        if tries == -1:
            fx_1 = fx
        if tries == 0:
            fx_2 = fx
        if tries <= 0:
            continue

        if fx * fx_1 > 0:
            fx_1 = fx
            x_1 = x
        else:
            fx_2 = fx
            x_2 = x
    print(x)
    return x


def calculate(event):

    document['txt'].clear()

    try:

        plating_nr = int(document['plating'].value)
        rho = plating[plating_nr].rho * 1E-9
        mu_r_w = plating[plating_nr].mu_r
        document['rho'].value = '%.2f' % (rho * 1E9)
        document['mu_r_w'].value = '%.8f' % mu_r_w

        N = float(document['N'].value)
        global l
        l = float(document['l'].value) * 1E-3
        p = l / N
        document['p'].value = '%.2f' % round(p * 1E3, 2)

        D = float(document['D'].value) * 1E-3
        d = float(document['d'].value) * 1E-3
        Phi = lookup_Phi(l, D, p, d)
        document['Phi'].value = '%.2f' % round(Phi, 2)

        D_eff = D - d * (1 - 1/sqrt(Phi))
        document['D_eff'].value = '%.2f' % round(D_eff * 1E3, 2)


        # Correction factors

        if l <= D_eff:    # The short coil expression gives a value that agrees better with the AGM result.
            k_L  = 1 + 0.383901 * (l/D_eff)**2 + 0.017108 * (l/D_eff)**4
            k_L /= 1 + 0.258952 * (l/D_eff)**2
            k_L *= log(4 * D_eff/l) - 0.5
            k_L += 0.093842 * (l/D_eff)**2 + 0.002029 * (l/D_eff)**4 - 0.000801 * (l/D_eff)**6
            k_L *= 2/pi * l/D_eff
        else:
            k_L  = 1 + 0.383901 * (D_eff/l)**2 + 0.017108 * (D_eff/l)**4
            k_L /= 1 + 0.258952 * (D_eff/l)**2
            k_L -= 4/3/pi * D_eff/l
        document['k_L'].value = '%.6f' % round(k_L, 6)

        k_s = 5/4 - log(2 * p/d)
        document['k_s'].value = '%.6f' % round(k_s, 6)

        c_9 = -log(2*pi) +3/2 +0.33084236 +1/120 -1/504 +0.0011925
        k_m  = log(2*pi) -3/2 -log(N)/6/N -0.33084236/N -1/(120*N**3) +1/(504*N**5) -0.0011925/N**7 + c_9/N**9
        document['k_m'].value = '%.8f' % round(k_m, 8)


        # Effective series AC resistance

        l_w_phys = sqrt((N * pi * D)**2 + l**2)
        document['l_w_phys'].value = '%.1f' % round(l_w_phys * 1E3, 1)

        global l_w_eff
        l_w_eff = sqrt((N * pi * D_eff)**2 + l**2)
        document['l_w_eff'].value = '%.1f' % round(l_w_eff * 1E3, 1)

        f = float(document['f'].value) * 1E6
        delta_i = sqrt(rho /pi /f /mu_0 /mu_r_w)
        document['delta_i'].value = '%.2f' % round(delta_i * 1E6, 2)

        R_eff_s  = rho * l_w_eff
        R_eff_s /= pi * (d * delta_i - delta_i**2)
        R_eff_s *= Phi
        if(N > 1):
            R_eff_s *= (N-1) / N
        document['R_eff_s'].value = '%.3f' % round(R_eff_s, 3)


        # Corrected current-sheet geometrical formula

        mu_r_core = 1
        L_s  = pi * (D_eff * N)**2 /4 /l * k_L
        L_s -= D_eff * N * (k_s + k_m) / 2
        L_s *= mu_r_core * mu_0
        document['L_s'].value = '%.3f' % round(L_s * 1E6, 3)

        global psi
        psi = atan(p /pi /D_eff)
        document['psi'].value = '%.2f' % round(psi / pi * 180, 2)


        # Copy & paste text field
        t = time.time()
        document['txt'] <= 'QOIL™ — https://hamwaves.com/qoil/ — v{}\n'.format(VERSION)
        document['txt'] <= time.strftime('  Coil design %Y-%m-%d %H:%M\n', time.localtime(t))

        offset = 28
        document['txt'] <= '\nINPUT\n'
        document['txt'] <= '  {:{offset}} D = {} mm\n'.format('mean diameter of the coil', document['D'].value, offset=offset)
        document['txt'] <= '  {:{offset}} N = {}\n'.format('number of turns', document['N'].value, offset=offset)
        document['txt'] <= '  {:{offset}} ℓ = {} mm\n'.format('length of the coil', document['l'].value, offset=offset)
        document['txt'] <= '  {:{offset}} d = {} mm\n'.format('wire or tubing diameter', document['d'].value, offset=offset)
        document['txt'] <= '  {:{offset}} f = {} MHz\n'.format('design frequency', document['f'].value, offset=offset)
        document['txt'] <= '  The (plating) material is {}.\n'.format(plating[plating_nr].description)

        document['txt'] <= '\nINTERMEDIATE RESULTS\n'
        document['txt'] <= '  {:{offset}} p = {} mm\n'.format('winding pitch', document['p'].value, offset=offset)
        document['txt'] <= '  {:{offset}} ℓ_w_phys = {} mm\n'.format('physical conductor length', document['l_w_phys'].value, offset=offset)
        document['txt'] <= '  {:{offset}} ψ = {}°\n'.format('effective pitch angle', document['psi'].value, offset=offset)


        # Characteristic impedance of the sheath helix waveguide mode

        offset = 55
        try:
            omega = 2 * pi * f
            k_0 = omega / c_0
            global a
            a = D_eff / 2

            # Sheath helix dispersion function
            F = lambda tau: K1(tau*a) * I1(tau*a) / (K0(tau*a) * I0(tau*a)) - (tau / k_0 * tan(psi))**2

            tau_1 = k_0                  # smallest tau estimate
            tau_2 = k_0 * cot(psi)**2    # largest tau estimate
            zero = fzero(F, tau_1, tau_2)
            tau = zero['zero']
            beta = sqrt(k_0**2 + tau**2)
            document['beta'].value = '%.4f' % round(beta, 4)

            Z_c = 60 * beta / k_0 * I0(tau*a) * K0(tau*a)
            document['Z_c'].value = '%.1f' % round(Z_c, 1)


            # Effective equivalent circuit

            # Corrected sheath helix waveguide formula
            L_eff_s  = Z_c / omega * tan(beta * l) * k_L
            L_eff_s -= mu_0 * D_eff * N * (k_s + k_m) / 2
            document['L_eff_s'].value = '%.3f' % round(L_eff_s * 1E6, 3)

            X_eff_s = omega * L_eff_s
            document['X_eff_s'].value = '%.1f' % round(X_eff_s, 1)

            Q_eff = X_eff_s / R_eff_s
            document['Q_eff'].value = '%d' % int(Q_eff)


            # Effective circuit results in copy & paste text field
            document['txt'] <= '\nRESULTS\n'
            document['txt'] <= '  Effective equivalent circuit\n'
            document['txt'] <= '    {:{offset}} L_eff_s = {} μH\n'.format('effective series inductance @ design frequency', document['L_eff_s'].value, offset=offset)
            document['txt'] <= '    {:{offset}} X_eff_s = {} Ω\n'.format('effective series reactance @ design frequency', document['X_eff_s'].value, offset=offset)
            document['txt'] <= '    {:{offset}} R_eff_s = {} Ω\n'.format('effective series AC resistance @ design frequency', document['R_eff_s'].value, offset=offset)
            document['txt'] <= '    {:{offset}} Q_eff = {}\n'.format('effective unloaded quality factor @ design frequency', document['Q_eff'].value, offset=offset)


        except:
            document['txt'] <= '  Lumped circuit equivalent\n'
            document['txt'] <= '    {:{offset}} L_s = {} μH\n'.format('f-independent series inductance; geometrical formula', document['L_s'].value, offset=offset)
            document['txt'] <= '    An error occurred when solving the dispersion function!\n'
            document['txt'] <= '    However, all shown results are useable.\n'

            outputs = ['beta', 'Z_c', 'L_eff_s', 'X_eff_s', 'Q_eff', 'R_s', 'C_p', 'f_res']
            for i in range(len(outputs)):
                document[outputs[i]].value = ''


        try:
            # Lumped equivalent circuit

            R_p = (Q_eff**2 + 1) * R_eff_s
            X_L_s = omega * L_s

            # https://en.wikipedia.org/wiki/Quadratic_equation#Reduced_quadratic_equation
            P = R_p / (2 * X_L_s)
            Q_L = P + sqrt(P**2 - 1)

            R_s = X_L_s / Q_L
            document['R_s'].value = '%.3f' % round(R_s, 3)

            X_eff_p = (Q_eff**2 + 1) / Q_eff**2 * X_eff_s
            X_L_p = (Q_L**2 + 1) / Q_L**2 * X_L_s

            X_C_p = X_eff_p * X_L_p / (X_L_p - X_eff_p)
            C_p = -1 /omega /X_C_p
            document['C_p'].value = '%.1f' % round(C_p * 1E12, 1)


            # Lumped circuit results in copy & paste text field
            document['txt'] <= '  Lumped circuit equivalent\n'
            document['txt'] <= '    {:{offset}} L_s = {} μH\n'.format('f-independent series inductance; geometrical formula', document['L_s'].value, offset=offset)
            document['txt'] <= '    {:{offset}} R_s = {} Ω\n'.format('series AC resistance @ design frequency', document['R_s'].value, offset=offset)
            document['txt'] <= '    {:{offset}} C_p = {} pF\n'.format('parallel stray capacitance @ design frequency', document['C_p'].value, offset=offset)


        except:
            document['txt'] <= '  Lumped circuit equivalent\n'
            document['txt'] <= '    {:{offset}} L_s = {} μH\n'.format('f-independent series inductance; geometrical formula', document['L_s'].value, offset=offset)
            document['txt'] <= '    No lumped circuit equivalent is available!\n'
            document['txt'] <= '    However, all shown results are useable.\n'

            outputs = ['R_s', 'C_p', 'f_res']
            for i in range(len(outputs)):
                document[outputs[i]].value = ''


        offset = 57
        try:
            # Self‑resonant frequency

            f_res = find_f_res()
            document['f_res'].value = '%.3f' % round(f_res * 1E-6, 3)


            # Resonant frequency in copy & paste text field
            document['txt'] <= '  {:{offset}} f_res = {} MHz\n'.format('Self-resonant frequency', document['f_res'].value, offset=offset)


        except:
            document['txt'] <= '  An error occurred when solving for the self-resonant frequency!\n'
            document['txt'] <= '  However, all shown results are useable.\n'

            document['f_res'].value = ''


        document['txt'] <= '\nDONATE\n'
        document['txt'] <= '  If this calculator proved any useful to you,\n'
        document['txt'] <= '  please, consider making a one-off donation\n'
        document['txt'] <= '  towards keeping me and the server up and running.\n'
        document['txt'] <= '  Thank you!'


    except:
        document['txt'].clear()    # COMMENT THIS LINE FOR TESTING PROGRESS
        outputs  = ['p', 'Phi', 'D_eff', 'k_L', 'k_s', 'k_m', 'l_w_phys', 'l_w_eff', 'delta_i', 'R_eff_s', 'L_s', 'psi']
        outputs += ['beta', 'Z_c', 'L_eff_s', 'X_eff_s', 'Q_eff', 'R_s', 'C_p', 'f_res']
        for i in range(len(outputs)):
            document[outputs[i]].value = ''


def myCalculate(D, N, l, d, f,plating_nr = 'hard-drawn copper' ):

    
    try:

        rho = plating[plating_nr].rho * 1E-9
        mu_r_w = plating[plating_nr].mu_r
        
        print('rho    = {:.2f}'.format(rho * 1E9) )
        print('mu_r_w = {:.2f}'.format(mu_r_w) )
        
        
        global l
        l = float(l) * 1E-3
        p = l / N
        
        #print('p = {:.2f}'.format(p * 1E3) )
        
        #document['p'].value = '%.2f' % round(p * 1E3, 2)

        D = float(D) * 1E-3
        d = float(d) * 1E-3
        
        Phi = lookup_Phi(l, D, p, d)
        
        #document['Phi'].value = '%.2f' % round(Phi, 2)

        D_eff = D - d * (1 - 1/sqrt(Phi))
        #document['D_eff'].value = '%.2f' % round(D_eff * 1E3, 2)


        # Correction factors

        if l <= D_eff:    # The short coil expression gives a value that agrees better with the AGM result.
            k_L  = 1 + 0.383901 * (l/D_eff)**2 + 0.017108 * (l/D_eff)**4
            k_L /= 1 + 0.258952 * (l/D_eff)**2
            k_L *= log(4 * D_eff/l) - 0.5
            k_L += 0.093842 * (l/D_eff)**2 + 0.002029 * (l/D_eff)**4 - 0.000801 * (l/D_eff)**6
            k_L *= 2/pi * l/D_eff
        else:
            k_L  = 1 + 0.383901 * (D_eff/l)**2 + 0.017108 * (D_eff/l)**4
            k_L /= 1 + 0.258952 * (D_eff/l)**2
            k_L -= 4/3/pi * D_eff/l
        #document['k_L'].value = '%.6f' % round(k_L, 6)

        k_s = 5/4 - log(2 * p/d)
        #document['k_s'].value = '%.6f' % round(k_s, 6)

        c_9 = -log(2*pi) +3/2 +0.33084236 +1/120 -1/504 +0.0011925
        k_m  = log(2*pi) -3/2 -log(N)/6/N -0.33084236/N -1/(120*N**3) +1/(504*N**5) -0.0011925/N**7 + c_9/N**9
        #document['k_m'].value = '%.8f' % round(k_m, 8)


        # Effective series AC resistance
        l_w_phys = sqrt((N * pi * D)**2 + l**2)
        #document['l_w_phys'].value = '%.1f' % round(l_w_phys * 1E3, 1)

        global l_w_eff
        l_w_eff = sqrt((N * pi * D_eff)**2 + l**2)
        #document['l_w_eff'].value = '%.1f' % round(l_w_eff * 1E3, 1)

        f = float(f) * 1E6
        delta_i = sqrt(rho /pi /f /mu_0 /mu_r_w)
        #document['delta_i'].value = '%.2f' % round(delta_i * 1E6, 2)

        R_eff_s  = rho * l_w_eff
        R_eff_s /= pi * (d * delta_i - delta_i**2)
        R_eff_s *= Phi
        if(N > 1):
            R_eff_s *= (N-1) / N
        #document['R_eff_s'].value = '%.3f' % round(R_eff_s, 3)


        # Corrected current-sheet geometrical formula

        mu_r_core = 1
        L_s  = pi * (D_eff * N)**2 /4 /l * k_L
        L_s -= D_eff * N * (k_s + k_m) / 2
        L_s *= mu_r_core * mu_0
        #document['L_s'].value = '%.3f' % round(L_s * 1E6, 3)

        global psi
        psi = atan(p /pi /D_eff)
        #document['psi'].value = '%.2f' % round(psi / pi * 180, 2)


        # Copy & paste text field

        offset = 28
        print('{:{offset}} D = {} mm\n'.format('mean diameter of the coil', D, offset=offset) )
        print('{:{offset}} N = {}\n'.format('number of turns', N, offset=offset) )
        print('{:{offset}} ℓ = {} mm\n'.format('length of the coil', l, offset=offset) )
        print('{:{offset}} d = {} mm\n'.format('wire or tubing diameter', d, offset=offset) ) 
        print('{:{offset}} f = {} MHz\n'.format('design frequency', f, offset=offset) )
        print('  The (plating) material is {}.\n'.format(plating[plating_nr].description) )

        print('\nINTERMEDIATE RESULTS\n' )
        print('  {:{offset}} p = {} mm\n'.format('winding pitch', p, offset=offset))
        print('  {:{offset}} ℓ_w_phys = {} mm\n'.format('physical conductor length', l_w_phys, offset=offset))
        print('  {:{offset}} ψ = {}°\n'.format('effective pitch angle', psi, offset=offset))


        # Characteristic impedance of the sheath helix waveguide mode

        offset = 55
        try:
            omega = 2 * pi * f
            k_0 = omega / c_0
            global a
            a = D_eff / 2

            # Sheath helix dispersion function
            F = lambda tau: K1(tau*a) * I1(tau*a) / (K0(tau*a) * I0(tau*a)) - (tau / k_0 * tan(psi))**2

            tau_1 = k_0                  # smallest tau estimate
            tau_2 = k_0 * cot(psi)**2    # largest tau estimate
            zero = fzero(F, tau_1, tau_2)
            tau = zero['zero']
            beta = sqrt(k_0**2 + tau**2)
            #document['beta'].value = '%.4f' % round(beta, 4)

            Z_c = 60 * beta / k_0 * I0(tau*a) * K0(tau*a)
            #document['Z_c'].value = '%.1f' % round(Z_c, 1)


            # Effective equivalent circuit

            # Corrected sheath helix waveguide formula
            L_eff_s  = Z_c / omega * tan(beta * l) * k_L
            L_eff_s -= mu_0 * D_eff * N * (k_s + k_m) / 2
            #document['L_eff_s'].value = '%.3f' % round(L_eff_s * 1E6, 3)

            X_eff_s = omega * L_eff_s
            #document['X_eff_s'].value = '%.1f' % round(X_eff_s, 1)

            Q_eff = X_eff_s / R_eff_s
            #document['Q_eff'].value = '%d' % int(Q_eff)


            # Effective circuit results in copy & paste text field
            print('Effective equivalent circuit \n')
            print('{:{offset}} L_eff_s = {} μH\n'.format('effective series inductance @ design frequency', L_eff_s, offset=offset) )
            print('{:{offset}} X_eff_s = {} Ω\n'.format('effective series reactance @ design frequency',  X_eff_s, offset=offset) )
            print('{:{offset}} R_eff_s = {} Ω\n'.format('effective series AC resistance @ design frequency',  R_eff_s, offset=offset) )
            print('{:{offset}} Q_eff = {}\n'.format('effective unloaded quality factor @ design frequency',  Q_eff, offset=offset) )


        except:
            print('  Lumped circuit equivalent\n' )
            print('    {:{offset}} L_s = {} μH\n'.format('f-independent series inductance; geometrical formula', L_s, offset=offset) )
            print('    An error occurred when solving the dispersion function!\n')
            print('    However, all shown results are useable.\n')

            #outputs = ['beta', 'Z_c', 'L_eff_s', 'X_eff_s', 'Q_eff', 'R_s', 'C_p', 'f_res']
            #for i in range(len(outputs)):
            #    document[outputs[i]].value = ''


        try:
            # Lumped equivalent circuit

            R_p = (Q_eff**2 + 1) * R_eff_s
            X_L_s = omega * L_s

            # https://en.wikipedia.org/wiki/Quadratic_equation#Reduced_quadratic_equation
            P = R_p / (2 * X_L_s)
            Q_L = P + sqrt(P**2 - 1)

            R_s = X_L_s / Q_L
            #document['R_s'].value = '%.3f' % round(R_s, 3)

            X_eff_p = (Q_eff**2 + 1) / Q_eff**2 * X_eff_s
            X_L_p = (Q_L**2 + 1) / Q_L**2 * X_L_s

            X_C_p = X_eff_p * X_L_p / (X_L_p - X_eff_p)
            C_p = -1 /omega /X_C_p
            #document['C_p'].value = '%.1f' % round(C_p * 1E12, 1)


            # Lumped circuit results in copy & paste text field
            print('  Lumped circuit equivalent\n')
            print('    {:{offset}} L_s = {} μH\n'.format('f-independent series inductance; geometrical formula', L_s, offset=offset))
            print('    {:{offset}} R_s = {} Ω\n'.format('series AC resistance @ design frequency', R_s, offset=offset))
            print('    {:{offset}} C_p = {} pF\n'.format('parallel stray capacitance @ design frequency',  C_p, offset=offset))


        except:
            print('  Lumped circuit equivalent\n')
            print('    {:{offset}} L_s = {} μH\n'.format('f-independent series inductance; geometrical formula', L_s, offset=offset))
            print('    No lumped circuit equivalent is available!\n'  )
            print('    However, all shown results are useable.\n'  )

            #outputs = ['R_s', 'C_p', 'f_res']
            #for i in range(len(outputs)):
            #    document[outputs[i]].value = ''


        offset = 57
        f_res = find_f_res()
        try:
            # Self‑resonant frequency

            f_res = find_f_res()
            #document['f_res'].value = '%.3f' % round(f_res * 1E-6, 3)


            # Resonant frequency in copy & paste text field
            #document['txt'] <= '  {:{offset}} f_res = {} MHz\n'.format('Self-resonant frequency', document['f_res'].value, offset=offset)


        except:
            print('  An error occurred when solving for the self-resonant frequency!\n')
            print('  However, all shown results are useable.\n')

            #document['f_res'].value = ''



    except:
        #document['txt'].clear()    # COMMENT THIS LINE FOR TESTING PROGRESS
        outputs  = ['p', 'Phi', 'D_eff', 'k_L', 'k_s', 'k_m', 'l_w_phys', 'l_w_eff', 'delta_i', 'R_eff_s', 'L_s', 'psi']
        outputs += ['beta', 'Z_c', 'L_eff_s', 'X_eff_s', 'Q_eff', 'R_s', 'C_p', 'f_res']
        #for i in range(len(outputs)):
        #    document[outputs[i]].value = ''

myCalculate(4, 10, 20, 1, 100,plating_nr = 'hard-drawn copper' )

# ## MAIN ###


document['brython'].style.display = 'initial'
calculate(None)


# ## EVENT HANDLERS ###


inputs = ['D', 'N', 'l', 'd', 'f']
for i in range(len(inputs)):
    document[inputs[i]].bind('input', calculate)
    #document[inputs[i]].bind('focus', calculate)

document['plating'].bind('change', calculate)
