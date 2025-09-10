

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
def funcion_sen(ff,nn,vmax=1,dc=0,ph=0,fs=2):#todas las variables que estan igualadas a un valor seran las 
                                             #opcionale y si nos las pongo cuando llamo la funcion toma esos 
                                             #valore. fs = 2 para que cumpla nyquis 
    
    t=np.arange(0,(nn)/fs,1/fs)
   
    y=vmax*np.sin(ff*2*np.pi*t+ph)+dc
    
    return t,y 
f=2000
N=100
fs=N
numero_periodos=3
fs=N*f/numero_periodos
t,x=funcion_sen(ff=f,nn=N,fs=fs,vmax=np.pi/2,ph=np.pi/2)

plt.plot(t,x,label="" ,linestyle='',marker="." ,color='r')
plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('eje de n en tiempo discreto')
plt.ylabel('eje de h[n] ')