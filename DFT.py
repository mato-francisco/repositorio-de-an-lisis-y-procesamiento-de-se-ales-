 
import numpy as np
import matplotlib.pyplot as plt

N=100

ff=10

def funcion_sen(vmax,dc,ff,ph,nn,fs):
    
    t=np.arange(0,(nn)/fs,1/fs)
    
    y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    
    return t ,y 

delta=np.zeros(N)

delta[1]=1
t , y = funcion_sen(1,0,10,0,N,N)  
X=np.zeros(N,dtype=np.complex128())

for k in np.arange(0,N):
    for n in np.arange(0,N):
        X[k]+=(y[n]*np.exp(-2.j*(np.pi/N)*n*k))
        
plt.figure(1)

plt.plot(np.arange(0,N),np.abs(X), linestyle='',marker='.' ,color='b')
plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis([0,N,0,100]) #en donde aparece el cuadro
plt.draw()
plt.tight_layout() 
plt.show()