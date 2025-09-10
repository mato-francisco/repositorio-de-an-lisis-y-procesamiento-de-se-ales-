import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
def funcion_sen(ff,nn,vmax=1,dc=0,ph=0,fs=2,dev_estandar=1):#todas las variables que estan igualadas a un valor seran las 
                                             #opcionale y si nos las pongo cuando llamo la funcion toma esos 
                                             #valore. fs = 2 para que cumpla nyquis 
    
    t=np.arange(0,(nn)/fs,1/fs)
    if(dev_estandar==1):
        y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    else:
        y=vmax*np.sin(ff*2*np.pi*t-ph)+dc+np.random.normal(0,dev_estandar,size=nn)

    return t,y 

nn=100
fs=nn
deltaf=fs/nn
x , y=funcion_sen(ff=1,nn=nn,fs=fs,dev_estandar=np.sqrt(2))
plt.figure(1)
plt.plot(x,(y),linestyle='',marker='.' ,color='b')
plt.grid(True, linestyle=':') 
plt.xlabel('eje de n muestras discretas)')
plt.ylabel('eje de h[n]')
#plt.axis([0,nn/2,0,10000]
plt.draw()
plt.tight_layout() 

plt.show()