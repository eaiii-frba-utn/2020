'''
VERSION
    20180916


PUBLIC DOMAIN NOTICE
    The utility posted on this page is based on the program "FZERO.F",
    written by L. F. Shampine (SNLA) and H. A. Watts (SNLA),
    based upon a method by T. J. Dekker.

    FZERO.F is part of the SLATEC library of programs, and
    its original FORTRAN code can be found at:
    https://www.netlib.org/slatec/src/fzero.f

    The code was developed at US Government research laboratories and
    is therefore public domain software.
    https://en.wikipedia.org/wiki/SLATEC

    SLATEC is an acronym for the Sandia, Los Alamos, 
    Air Force Weapons Laboratory Technical Exchange Committee.

    The JavaScript code as published by David Binner on
    http://www.akiti.ca/f2z.js
    http://www.akiti.ca/fxn2zero.html
    was transcoded by Serge Y. Stroobandt 
    to Brython code and extensively edited.


PURPOSE
    Search for a zero of a function f(x) in a given interval
    (b,c).  It is designed primarily for problems where f(b)
    and f(c) have opposite signs.


KEYWORDS
    bisection, nonlinear equations, roots, zeros


AUTHORS
    Binner David, (AKiTi.ca, Coquitlam, BC, Canada)
    Shampine, L. F., (SNLA)
    Stroobandt, Serge Y., (Hasselt, Belgium)
    Watts, H. A., (SNLA)


DESCRIPTION
     FZERO searches for a zero of a REAL function f(x) between the
     given REAL values b and c until the width of the interval (b,c)
     has collapsed to within a tolerance specified by the stopping
     criterion,

        abs(b-c) <= 2 * (rw * abs(b) + ae).

     The method used is an efficient combination of bisection and the
     secant rule and is due to T. J. Dekker.


REFERENCES
    Shampine, L. F. (SNLA) and H. A. Watts (SNLA),
        FZERO, A Root-solving Code,
        Report SC-TM-70-631,
        Sandia Laboratories,
        September, 1970

    Dekker, T. J.,
        Finding a Zero by Means of Successive Linear Interpolation,
        Constructive Aspects of the Fundamental Theorem of Algebra,
        edited by B. Dejon and P. Henrici,
        Wiley-Interscience
        1969
'''


from math import nan


error_msg = [''] * 5

error_msg[0] = 'The zero is within the requested tolerance (on the order of Machine Epsilon), \
                \nthe interval has collapsed to the requested tolerance, \
                \nthe function changes sign over the interval, and \
                \nthe function decreased in magnitude as the interval collapsed.'

error_msg[1] = 'A zero has been found, but the interval has not collapsed \
                \nto the requested tolerance.'

error_msg[2] = 'MAXIT (200) function evaluations. The solution may be meaningless. Check it.'

error_msg[3] = 'b and c are the same. Please, try again with a non-zero interval. No further action taken.'

error_msg[4] = 'The function does not change sign over the input interval. Please select another interval. No further action taken.'


# https://stackoverflow.com/a/52355075/2192488
sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)


def fzero(f, b, c):    # f is a function and b and c are starting values for x.

    neg_flag = False
    zero = nan
    count = 0

    # https://en.wikipedia.org/wiki/Machine_epsilon#Approximation
    epsilon_m = 1
    while 1 + 0.5 * epsilon_m != 1:
        epsilon_m = 0.5 * epsilon_m

    if b == c:
        # b and c are the same. Please, try again with a non-zero interval. No further action taken.
        return {'zero':zero, 'f_evaluations':count, 'epsilon_m':epsilon_m, 'error_code':3, 'error_msg':error_msg[3]}

    if b > c:
        # Swap interval endpoints.
        z = b
        b = c
        c = z

    if abs(b) > abs(c):    # Most of the interval is negative.
        if c >= 0:
            # The interval is truncated so that it does NOT include 0.
            c = -b
            b = 0.0000000001
        else:
            z = -b
            b = -c
            c = z
    else:
        neg_flag = True
        if b <= 0:
            # The interval was truncated so that it does NOT include 0.
            b = 0.0000000001

    z = (c + b) / 2
    fc = fz = f(z)

    t = b
    fb = f(b)

    count = 2

    if fb == 0:
        if neg_flag:
            zero = b
        else:
            zero = -b
        return {'zero':zero, 'f_evaluations':count, 'epsilon_m':epsilon_m, 'error_code':1, 'error_msg':error_msg[1]}

    if fz == 0:
        if neg_flag:
            zero = z
        else:
            zero = -z
        return {'zero':zero, 'f_evaluations':count, 'epsilon_m':epsilon_m, 'error_code':1, 'error_msg':error_msg[1]}

    if sign(fz) == sign(fb):
        t = c
        fc = f(c)
        count = 3

        if fc == 0:
            if neg_flag:
                zero = c
            else:
                zero = -c
            return {'zero':zero, 'f_evaluations':count, 'epsilon_m':epsilon_m, 'error_code':1, 'error_msg':error_msg[1]}

        if sign(fz) != sign(fc):
            b = z
            fb = fz
        else:
            # The sign is the same on this interval as well.
            # Hence, there is no zero on the input interval.
            return {'zero':zero, 'f_evaluations':count, 'epsilon_m':epsilon_m, 'error_code':4, 'error_msg':error_msg[4]}
    else:
        c = z

    a = c
    fa = fc
    ic = 0
    acbs = abs(c - b)
    MAXIT = 200

    while count < MAXIT:
        if abs(fc) < abs(fb):
            # Perform interchange.
            a = b
            fa = fb
            b = c
            fb = fc
            c = a
            fc = fa

        cmb = (c - b) / 2
        acmb = abs(cmb)
        tol = (abs(b) + 1) * epsilon_m

        # Test stopping criterion
        if acmb <= tol:
            error_code = 0
            break

        if fb == 0:
            error_code = 1
            break

        # Calculate new iterate implicitly as b + p/q,
        # where p is arranged to be >= 0.
        # This implicit form is used to prevent overflow.
        p = (b - a) * fb
        q = fa - fb
        if p < 0:
            p = -p
            q = -q

        # Update a and check for satisfactory reduction in the size of the bracketing interval.
        # If not, perform bisection.
        a = b
        fa = fb
        ic += 1

        if ic >= 4 and 8 * acmb >= acbs:
            # Use bisection.
            b = (c + b) / 2
        else:
            if ic >= 4:
                ic = 0
                acbs = acmb

            if p <= tol * abs(q):    # Test for too small a change
                b += tol * sign(cmb)
            else:    # The root is between b and (b + c) / 2.
                if p < cmb * q:
                    # Use the secant rule.
                    b += p/q
                else:
                    # Use bisection.
                    b = (c + b) / 2

        # Have now computed new iterate, b.
        fb = f(b)
        count += 1

        if fb == 0:
            if neg_flag:
                zero = b
            else:
                zero = -b
            return {'zero':zero, 'f_evaluations':count, 'epsilon_m':epsilon_m, 'error_code':1, 'error_msg':error_msg[1]}

        # Decide whether the next step is interpolation or extrapolation.
        if sign(fb) == sign(fc):
            c = a
            fc = fa
    # END of while loop

    if count >= MAXIT:
        error_code = 2

    if neg_flag:
        zero = b
    else:
        zero = -b

    return {'zero':zero, 'f_evaluations':count, 'epsilon_m':epsilon_m, 'error_code':error_code, 'error_msg':error_msg[error_code]}
