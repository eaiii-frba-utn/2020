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


if __name__ == "__main__":
    print('Hola')