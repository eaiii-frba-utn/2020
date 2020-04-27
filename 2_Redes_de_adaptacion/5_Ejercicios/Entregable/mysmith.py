#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""Bibliotecas de funciones para graficar la carta de Smith"""

__author__ = "A. Almela"
__copyright__ = "Electrónica Aplicada III"
__credits__ = ["UTN FRBA"]
__license__ = "GPL"
__version__ = "1.0"
__email__ = "dalmela@frba.utn.edu.ar"
__status__ = "Development"

import numpy as np
from skrf.media import DistributedCircuit
from skrf import Frequency
from skrf import network
from skrf.network import *

## Defino las funciones para agregar componentes en derivación (Zparal) y en serie (Yserie). 
## La salida es una variable Network de skrf

def Yserie(freq, ys, z0=50):
    y = np.empty(shape=(len(freq.f),2,2), dtype=complex)
    for i,f in enumerate(freq.f):
        y[i,0,0] =  ys
        y[i,0,1] = -ys
        y[i,1,0] = -ys
        y[i,1,1] =  ys
    a = network.y2s(y,z0=z0)
    ntwk = Network(frequency=freq, s= a, z0=z0)
    return ntwk


def Zparal(freq, zp, z0=50):
    z = np.empty(shape=(len(freq.f),2,2), dtype=complex)
    for i,f in enumerate(freq.f):
        z[i,0,0] =  zp
        z[i,0,1] =  zp
        z[i,1,0] =  zp
        z[i,1,1] =  zp
    a = network.z2s(z,z0=z0)
    ntwk = Network(frequency=freq, s= a, z0=z0)
    return ntwk

## Convierte a network de skrf una impedancia de carga dada. 

def ZL(freq, zl, z0=50):
    z = np.empty(shape=(len(freq.f),1,1), dtype=complex)
    for i,f in enumerate(freq.f):
        z[i,0,0] =  zl
    a = network.z2s(z,z0=z0)
    ntwk = Network(frequency=freq, s= a, z0=z0)
    return ntwk

## Convierte a network de skrf una admitancia de carga dada.
def YL(freq, yl, z0=50):
    y = np.empty(shape=(len(freq.f),1,1), dtype=complex)
    for i,f in enumerate(freq.f):
        z[i,0,0] =  yl
    a = network.y2s(z,z0=z0)
    ntwk = Network(frequency=freq, s= a, z0=z0)
    return ntwk

# Calcula X dada una frecuencia y un valor de capacidad
def Xc(f, C):
    if C == 0 : x = -np.inf
    else      : x = -(2*np.pi*f*C)**-1 
    return x


# Calcula X dada una frecuencia y un valor de inductancia
def Xl(f, L):
    return (2*np.pi*f*L) 

# Calcula B dada una frecuencia y un valor de inductancia
def Bl(f, L):
    if L == 0 : y = -np.inf
    else      : y = -(2*np.pi*f*L)**-1 
    return y 

# Calcula B dada una frecuencia y un valor de capacidad
def Bc(f, C):
    return (2*np.pi*f*C) 

def printSmith(nw, c = 'r', m = 'o'):
    nw.plot_s_smith(m=0,n=0,color=c,draw_labels=True,show_legend = False, chart_type='yz',marker=m)
    return 

# print datos
def printZ(Z):
    r = Z.real
    x = Z.imag
    if r == 0 : Q = np.inf 
    else:       Q = abs(x/r)
    print('R = {:1.3e} ohms'.format(r))
    print('X = {:1.3e} ohms'.format(x))
    print('Q = {:1.3f} '.format(Q) )
    return Q

# print datos
def printY(Y):
    g = Y.real
    b = Y.imag
    if g == 0 : Q = np.inf 
    else:       Q = abs(b/g)
    print('g = {:1.3e} ohms'.format(g))
    print('b = {:1.3e} ohms'.format(b))
    print('Q = {:1.3f} '.format(Q) )
    return Q

def printS(S1):
    s11 =   S1[0,0]
    s12 =   S1[0,1]
    s21 =   S1[1,0]
    s22 =   S1[1,1]
    print( 's11= |{:1.4f}|  ({:1.4f})' .format(abs(s11),np.angle(s11)*180/np.pi ))
    print( 's12= |{:1.4f}|  ({:1.4f})' .format(abs(s12),np.angle(s12)*180/np.pi ))
    print( 's21= |{:1.4f}|  ({:1.4f})' .format(abs(s21),np.angle(s21)*180/np.pi ))
    print( 's22= |{:1.4f}|  ({:1.4f})' .format(abs(s22),np.angle(s22)*180/np.pi ))

def printY(Y1,f):
    wo  = 2*np.pi*f
    y11 =   Y1[0,0]
    y12 =   Y1[0,1]
    y21 =   Y1[1,0]
    y22 =   Y1[1,1]
    print( 'y11= {0.real:1.4f}+  ({0.imag:1.4f})j' .format(y11) )
    print( 'y12= {0.real:1.4f}+  ({0.imag:1.4f})j' .format(y12) )
    print( 'y21= {0.real:1.4f}+  ({0.imag:1.4f})j' .format(y21) )
    print( 'y22= {0.real:1.4f}+  ({0.imag:1.4f})j' .format(y22) )
    print(' ')

    print( 'r11= {0.real:1.4F}' .format(1/y11.real) )
    print( 'c11= {0.real:1.4E}' .format(y11.imag/wo) )


    print( 'gm =  {0.real:1.4E}+  ({0.imag:1.4E})j' .format((y21)) )
    print( 'gr =  {0.real:1.4E}+  ({0.imag:1.4E})j' .format((y12)) )

    print( 'r22= {0.real:1.4F}' .format(1/y22.real) )
    print( 'c22= {0.real:1.4E}' .format(y22.imag/wo) )

def Yini(yg, yl, yt, printme = False):
    y11 = yt[0,0]
    y12 = yt[0,1]
    y21 = yt[1,0]
    y22 = yt[1,1]
    yin  = y11 - (y21*y12)/(y22+yl)
    if printme:
        print( 'yin  = {0.real:4.3F} {0.imag:4.2E}' .format(yin) )
        print( 'rin  = {0.real:4.3F} ' .format(1/yin.real) )    
    return yin
    
def Youti(yg, yl, yt, printme = False):
    y11 = yt[0,0]
    y12 = yt[0,1]
    y21 = yt[1,0]
    y22 = yt[1,1]
    yout = y22 - (y21*y12)/(y11+yg)
    if printme:
        print( 'yout = {0.real:4.3F} {0.imag:4.2E}' .format(yout) )
        print( 'rout = {0.real:4.3F} ' .format(1/yout.real) )    
    return yout   

if __name__ == "__main__":
    print('Hola')