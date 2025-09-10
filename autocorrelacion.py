import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
def funcion_sen(ff,nn,vmax=1,dc=0,ph=0,fs=2):#todas las variables que estan igualadas a un valor seran las 
                                             #opcionale y si nos las pongo cuando llamo la funcion toma esos 
                                             #valore. fs = 2 para que cumpla nyquis 
    
    t=np.arange(0,(nn)/fs,1/fs)
   
    y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    
    return t,y 

ff=2000
ph=0
vmax=1
dc=0

N=100
periodos_visible=3
fs=N*ff/periodos_visible
deltaf=fs/N

x , z =funcion_sen(ff=2000,nn=N,fs=fs)

plt.figure(1)
plt.plot(x,z,label=" ",linestyle='-',marker="." ,color='r')
plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.draw()
plt.show()

autocorrelacion=np.correlate(z, z,mode="full")

plt.figure(2)
plt.plot(np.arange(N+N-1),autocorrelacion,label=" ",linestyle='-',marker="." ,color='r')
plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.draw()
plt.show()
