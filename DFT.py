 
import numpy as np
import matplotlib.pyplot as plt

N=100

ff=100



delta=np.zeros(N)

delta[1]=1

X=np.zeros(N,dtype=np.complex128())

for k in np.arange(0,N):
    for n in np.arange(0,N):
        X[k]+=(delta[n]*np.exp(-2.j*(np.pi/N)*n*k))
        
plt.figure(1)

plt.plot(np.arange(0,N),np.abs(X), linestyle='-',marker='.' ,color='b')
plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis([0,N,0,2]) #en donde aparece el cuadro
plt.draw()
plt.tight_layout() 
plt.show()