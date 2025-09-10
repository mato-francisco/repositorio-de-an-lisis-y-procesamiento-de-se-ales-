import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
def funcion_sen(ff,nn,vmax=1,dc=0,ph=0,fs=2):#todas las variables que estan igualadas a un valor seran las 
                                             #opcionale y si nos las pongo cuando llamo la funcion toma esos 
                                             #valore. fs = 2 para que cumpla nyquis 
    
    t=np.arange(0,(nn)/fs,1/fs)
   
    y=vmax*np.sin(ff*2*np.pi*t+ph)+dc
    
    return t,y 
N=500
fs=N/10
t=np.linspace(0,1/10,N)

x=np.zeros(N,dtype=float)
for k in np.arange(0,N):
    if(t[k]<0.01):
        
        x[k]=1
    else:
        x[k]=0
        
h=np.zeros(N)
for n in np.arange(N):
    h[n]=3*(10**-2)*x[n]+5*(10**-2)*x[n-1]+3*(10**-2)*x[n-2]+1.5*h[n-1]-0.5*h[n-2]

energia=np.sum(h**2) 
plt.plot(t,h, label=".",marker="x" ,color='b')
plt.legend()
plt.title("señal de entrada: señal senoidal de 2Khz,desfazada y amplidicada pi/2")
plt.grid(True, linestyle=':') 
plt.xlabel('eje de n en tiempo discreto')
plt.ylabel('eje de h[n] ')
print("Muestras",N,"frecuencia de muestro",round(fs,2),"energia de la señal",round(energia,2))