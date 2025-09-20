import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft


nn=100
fs=nn
deltaf=fs/nn

t=np.arange(0,(nn)/fs,1/fs)
y=np.sin(np.pi*2*(nn/4)*t)
dev_y=np.std(y)
y=y/dev_y

z=np.sin(np.pi*2*((nn/4)+0.25)*t)
dev_z=np.std(z)
z=z/dev_z

w=np.sin(np.pi*2*((nn/4)+0.5)*t)
dev_w=np.std(w)
w=w/dev_w
 


       
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

aux=np.abs(fftY)**2
aux=np.sum(aux)
plt.plot(ff,ffYabs, label="dB((nn)/4)",linestyle='',marker='X' ,color='b')

#plt.plot(ff,20*np.log10(ffZabs), label="dB((nn/4)+0.25)",linestyle='',marker='o' ,color='r')

#plt.plot(ff,20*np.log10(ffWabs), label="dB((nn/4)+0.5)",linestyle='',marker='s' ,color='g')


plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('frecuencia (HZ)')
plt.ylabel('amplitud[db]')
plt.xlim(0,nn)
#plt.axis([0,nn/2,0,10000]
plt.draw()
plt.tight_layout() 

plt.show()

#parsebal---------------------------------
energia_y=np.sum(np.abs(y)**2)
energia_ffy=np.sum(np.abs(fftY)**2)/nn
print("energia de la señal de frecuencia N/4")
print(energia_y)
print("energia de tranformada de la señal de frecuencia N/4")
print(energia_ffy)
energia_z=np.sum(np.abs(z)**2)
energia_ffz=np.sum(np.abs(fftZ)**2)/nn
print("energia de la señal de frecuencia N/4")
print(energia_z)
print("energia de tranformada de la señal de frecuencia N/4+0.25")
print(energia_ffz)
energia_w=np.sum(np.abs(w)**2)
energia_ffw=np.sum(np.abs(fftW)**2)/nn
print("energia de la señal de frecuencia N/4+0.5")
print(energia_w)
print("energia de tranformada de la señal de frecuencia N/4+0.5")
print(energia_ffw)
#zero_padding--------------------------------
