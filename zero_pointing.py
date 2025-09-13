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

    return y

N=100
fs=N
deltaf=fs/N
 
zeross=np.zeros(9*N)

y=funcion_sen(ff=10,nn=N,fs=N ,dev_estandar=np.sqrt(1))

zero_pointing=np.concat((y,zeross),axis=0)

ffpointing=np.fft.fft(zero_pointing)


plt.figure(1)
plt.clf

ff=np.arange(10*N)*(fs/(10*N))
#como esta interpolada al extender 10 veces la cantidadad de muestaras me cambia el 
#delta f entonces tengo que volver a escalar la frecuencia
#
#plt.plot(ff,np.abs(ffpointing), label="zero_pointing",linestyle='',marker='.' ,color='b')
plt.plot(ff,20*np.log10(ffpointing), label="",linestyle='',marker='.' ,color='k')
plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('frecuencia (HZ)')
plt.ylabel('f(w)')
plt.xlabel('drecuencia en db')
plt.ylabel('fdb(w)')
plt.xlim(0,N/2)
#plt.axis([0,nn/2,0,10000]
plt.draw()
plt.tight_layout() 

plt.show()
plt.figure(2)
plt.clf

ffsen=np.fft.fft(y)
fsen=np.arange(N)*(fs/(N))

plt.plot(ff,np.abs(ffpointing), label="interpolado",linestyle='',marker='.' ,color='b')
plt.plot(fsen,np.abs(ffsen), label="no interpolado",linestyle='',marker='x' ,color='r',)
plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('frecuencia (HZ)')
plt.ylabel('f(w)')
plt.xlim(0,N/2)
#plt.axis([0,nn/2,0,10000]
plt.draw()
plt.tight_layout() 

plt.show()