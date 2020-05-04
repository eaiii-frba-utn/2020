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
import matplotlib.pyplot as plt


# defino la función que se emplea para el cálculo de dBm  
def dBm(x):
    return 10*np.log10(x/1e-3)

# defino la función para mostrar los resultados
def imprimePRL(f, Prl):
    # Máximo de potencia en RL
    xmax = np.where(max(Prl) == Prl  ) 
    # Buscamos el ancho de banda (OJO que en potencia es 3dB) 
    x3db = (Prl >= max(Prl)/2 ) # el max(Prl)/2 es el limite de 3dB
    # ancho de banda
    BW = max(f[x3db]) - min(f[x3db])
    fo = f[xmax][0]
    Qc = fo/BW
    print('frecuencia central')
    print('fo =  {:1.3e} MHz'.format(f[xmax][0]))
    print('Ancho de banda:')
    print('Qc  =  {:1.3e} '.format(Qc) )
    print('BW  =  {:1.3f} MHz'.format(BW/1e6) )
    print('')
    print('Potenicia:')
    print('PRL  =  {:1.3e} W (eff)'.format( (Prl)[xmax][0]) )
    print('PRL  =  {:1.2e} dBm (eff)'.format(dBm(Prl)[xmax][0]) )



    # plot
    plt.plot(f,dBm(Prl))
    plt.plot(f[x3db] , dBm(Prl)[x3db], 'g.' )
    plt.plot(f[xmax] , dBm(Prl)[xmax], 'ro' )
    plt.grid()
    plt.ylabel('PRL/dBm')
    plt.xlabel('Frecuencia/Hz')
    
    # agrego la flecha de ancho de bandaa
    xymin = (min(f[x3db]), dBm(Prl)[xmax][0]-3)
    xymax = (max(f[x3db]), dBm(Prl)[xmax][0]-3)
    xytext= (f[xmax] , dBm(Prl)[xmax][0]-4 )
    plt.annotate(s=' ',xy=xymin, xycoords='data',xytext=xymax,textcoords='data',arrowprops=dict(arrowstyle="<->"))

    plt.annotate(s='BW',xy=xytext, xycoords='data',fontsize=12.0,textcoords='data',ha='center')

    
    return


# defino la función para mostrar los resultados
def imprimeZin(f, Z):
    ax = plt.subplot(111)
    ax.grid(True)
    ax.plot(f , np.abs(Z)      )
    #ax.plot(fo, np.abs(Z), 'ro')
    ax2 = ax.twinx()
    ax2.plot(f , np.angle(Z)*180/np.pi  , 'r--'    )
    plt.ylabel('Zin')
    plt.xlabel('Frecuencia/Hz')
    
    return


def PlotCpx(f,Z, labelx = ' ', labely = ' '):
    ax = plt.subplot(111)
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.ylabel(labely)
    plt.xlabel(labelx)
    ax.plot(f , (Z.real ) )
    ax2 = ax.twinx()
    ax2.plot(f ,Z.imag  , 'r--'    )
    
def PlotCpxSlog(f,Z, labelx = ' ', labely = ' '):
    ax = plt.subplot(111)
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.ylabel(labely)
    plt.xlabel(labelx)
    ax.semilogx(f , (Z.real ) )
    ax2 = ax.twinx()
    ax2.plot(f ,Z.imag*180/np.pi  , 'r--'    )    

def PlotArySlog(f,Z, labelx = ' ', labely = ' '):
    ax = plt.subplot(111)
    ax.grid(True)
    plt.ylabel(labely)
    plt.xlabel(labelx)
    ax.semilogx(f , (Z ) )
    
    
def PlotAry(f,Z, labelx = ' ', labely = ' '):
    ax = plt.subplot(111)
    ax.grid(True)
    plt.ylabel(labely)
    plt.xlabel(labelx)
    ax.plot(f , (Z ) )