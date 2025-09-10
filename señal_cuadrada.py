 
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
from scipy import signal as sp
def funcion_sen(ff,nn,vmax=1,dc=0,ph=0,fs=2):#todas las variables que estan igualadas a un valor seran las 
                                             #opcionale y si nos las pongo cuando llamo la funcion toma esos 
                                             #valore. fs = 2 para que cumpla nyquis 
    
    t=np.arange(0,(nn)/fs,1/fs)
   
    y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    
    return t,y 

nn=501
ff=4000
t=np.linspace(0,20*1/ff,nn)
espacio_cuadrado=sp.square(2 * np.pi * ff * t)

plt.figure(4)

plt.plot(t,espacio_cuadrado, label=f"N={nn},fs={ff*nn}",marker="x" ,color='b')
plt.legend()

plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis([0,0.001,-2,2]) 
plt.draw()