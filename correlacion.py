 
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
def funcion_sen(ff,nn,vmax=1,dc=0,ph=0,fs=2):#todas las variables que estan igualadas a un valor seran las 
                                             #opcionale y si nos las pongo cuando llamo la funcion toma esos 
                                             #valore. fs = 2 para que cumpla nyquis 
    
    t=np.arange(0,(nn)/fs,1/fs)
   
    y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    
    return t,y 

f=100
N=500
numero_periodos=10
fs=N*f/numero_periodos


t , x = funcion_sen(ff=f,nn=N,fs=fs)
correlacion=np.correlate(x, x,mode="full")
plt.plot(np.arange(2*N-1)*2*np.pi/1000,correlacion/np.max(correlacion), label="respuesta al impulso",linestyle='-',marker='.' ,color='b')
#plt.plot(np.arange(N)/fs,x, label="respuesta al impulso",linestyle='-',marker='.' ,color='b')
plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('eje de n muestras discretas)')
plt.ylabel('eje de h[n]')
#plt.axis([0,nn/2,0,10000]
plt.draw()
plt.tight_layout() 

plt.show()