
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
M=8

N=100

n=np.arange(8)

nn=np.arange(8)%4

x=4+3*np.sin(n*np.pi/2)

y=4+3*np.sin((-nn)*np.pi/2)

rxx=sig.correlate(x, x)

X=np.zeros(N,dtype=np.complex128())

for k in np.arange(0,N):
    for nnn in np.arange(0,N):
        X[k]+=(X[nnn]*np.exp(-2.j*(np.pi/N)*n*k))

plt.figure(1)

plt.plot(np.arange(8),x,label ="x", linestyle='',marker='x' ,color='b')

plt.plot(np.arange(8),y,label="y", linestyle='',marker='.' ,color='r')

plt.plot(np.arange(8),X,label="y", linestyle='',marker='.' ,color='g')

plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.draw()
plt.tight_layout() 
plt.show()