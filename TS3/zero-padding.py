

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


fftY=np.fft.fft(y,n=10*nn)
fftZ=np.fft.fft(z,n=10*nn)
fftW=np.fft.fft(w,n=10*nn)

ffYabs=np.abs(fftY)
ffZabs=np.abs(fftZ)
ffWabs=np.abs(fftW)

plt.figure(1)
plt.clf

ff=np.arange(10*nn)*fs/(10*nn) #escala el eje en frecuencia no normalizada por resolucion espectral
                        #para pasar de eje de muestra a frecuencia, multiplico n por la resolucion espectral 



plt.plot(ff,ffYabs, label="dB((nn)/4)",linestyle='',marker='x' ,color='b')

plt.plot(ff,ffZabs, label="dB((nn/4)+0.25)",linestyle='',marker='.' ,color='r')

plt.plot(ff,ffWabs, label="dB((nn/4)+0.5)",linestyle='',marker='s' ,color='g')


plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('frecuencia (HZ)')
plt.ylabel('amplitud[db]')
plt.xlim(0,nn/2)
#plt.axis([0,nn/2,0,10000]
plt.draw()
plt.tight_layout() 

plt.show()

#parsebal---------------------------------
energia_y=np.sum(np.abs(y)**2)
energia_ffy=np.sum(np.abs(fftY)**2)/nn
print("energia de la señal de frecuencia N/4")
print(f"{energia_y:.2f}")
print("energia de tranformada de la señal de frecuencia N/4")
print(f"{energia_ffy:.2f}")
energia_z=np.sum(np.abs(z)**2)
energia_ffz=np.sum(np.abs(fftZ)**2)/nn
print("energia de la señal de frecuencia N/4")
print(f"{energia_z:.6f}")
print("energia de tranformada de la señal de frecuencia N/4+0.25")
print(f"{energia_ffz:.6f}")
energia_w=np.sum(np.abs(w)**2)
energia_ffw=np.sum(np.abs(fftW)**2)/nn
print("energia de la señal de frecuencia N/4+0.5")
print(f"{energia_w:.2f}")
print("energia de tranformada de la señal de frecuencia N/4+0.5")
print(f"{energia_ffw:.2f}")