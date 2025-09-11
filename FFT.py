import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
<<<<<<< HEAD
def funcion_sen(ff,nn,vmax=1,dc=0,ph=0,fs=2,dev_estandar=1):#todas las variables que estan igualadas a un valor seran las 
=======
def funcion_sen(ff,nn,vmax=1,dc=0,ph=0,fs=2):#todas las variables que estan igualadas a un valor seran las 
>>>>>>> a875cef09584373cbc1560b893aa9ca9ab44bce0
                                             #opcionale y si nos las pongo cuando llamo la funcion toma esos 
                                             #valore. fs = 2 para que cumpla nyquis 
    
    t=np.arange(0,(nn)/fs,1/fs)
<<<<<<< HEAD
    if(dev_estandar==1):
        y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    else:
        y=vmax*np.sin(ff*2*np.pi*t-ph)+dc+np.random.normal(0,dev_estandar,size=nn)

=======
   
    y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    
>>>>>>> a875cef09584373cbc1560b893aa9ca9ab44bce0
    return t,y 

nn=1000
fs=nn
deltaf=fs/nn


<<<<<<< HEAD
x , y =funcion_sen( (nn/4)*deltaf,nn,fs=fs,dev_estandar=np.sqrt(2)) #NO pude esscribir en la funcion ff=(nn/4)*deltaf
x , z =funcion_sen(((nn+1)/4)*deltaf,nn,fs=fs,dev_estandar=np.sqrt(2)  )
x , w =funcion_sen( deltaf*((nn+0.5)/4 ),nn,fs=fs,dev_estandar=np.sqrt(2) )
=======
x , y =funcion_sen( (nn/4)*deltaf,nn,fs=fs) #NO pude esscribir en la funcion ff=(nn/4)*deltaf
x , z =funcion_sen(((nn+1)/4)*deltaf,nn,fs=fs  )
x , w =funcion_sen( deltaf*((nn+0.5)/4 ),nn,fs=fs )
>>>>>>> a875cef09584373cbc1560b893aa9ca9ab44bce0
        
fftY=np.fft.fft(y)
fftZ=np.fft.fft(z)
fftW=np.fft.fft(w)

ffYabs=np.abs(fftY)
ffZabs=np.abs(fftZ)
ffWabs=np.abs(fftW)

plt.figure(1)
plt.clf

ff=np.arange(nn)*deltaf #escala el eje en frecuencia no normalizada por resolucion espectral
                        #para pasar de eje de muestra a frecuencia, multiplico n por la resolucion espectral 

plt.plot(ff,ffYabs, label="y",linestyle='',marker='.' ,color='b')

#plt.plot(ff,20*np.log10(ffYabs), label="dB((nn)/4)",linestyle='',marker='x' ,color='k')
#como el pasaje db es multiplicando 20 entonces es en desibeles de señal(de voltaje)

plt.plot(ff,ffZabs, label="z",linestyle='',marker='.' ,color='g')
#plt.plot(ff,20*np.log10(ffZabs), label="dB((nn+1)/4)",linestyle='',marker='.' ,color='r')

plt.plot(ff,ffWabs,label="w", linestyle='',marker='.' ,color='r')
#plt.plot(ff,20*np.log10(ffWabs), label="dB((nn+0.5)/4)",linestyle='',marker='.' ,color='r')

#al no poner una relacion cada punto lo relaciona a una secuencia de numeros tipo 1 2 3 etc y cada punto
#el 1 le correspone al ffyabs(1) ffyabs(1) ffyabs(2)  

plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('frecuencia (HZ)')
plt.ylabel('amplitud[db]')
plt.xlim(0,nn/2)
#plt.axis([0,nn/2,0,10000]
plt.draw()
plt.tight_layout() 

plt.show()