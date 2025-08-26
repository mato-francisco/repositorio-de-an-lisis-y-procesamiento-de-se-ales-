import numpy as np
import matplotlib.pyplot as plt

def funcion_sen(vmax,dc,ff,ph,nn,fs):
    
    t=np.arange(0,(nn)/fs,1/fs)
    
    y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    
    return t ,y 


ff=500
ph=0
vmax=1
dc=1
nn=10
fs=5000
#ejemplo de clase: se quiere ver la señal  en 1s por lo tanto la relación queda N = ts
#para ver tantas muestras en un periodo, hay que hacer "periodo/muestras=periodo de muestro"

tiempo , espacio = funcion_sen(vmax,dc,ff,ph,nn,fs)

plt.figure(1)

plt.plot(tiempo,espacio, linestyle='-.' ,color='r')
plt.plot(tiempo,espacio, linestyle='',marker='.' ,color='b')
plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis([np.min(tiempo),np.max(tiempo),np.min(espacio)-0.5,np.max(espacio)+0.5]) #en donde aparece el cuadro
plt.draw()


#caso frecuencia 500

plt.figure(2)

ff=500 
ph=0
vmax=1
dc=0
nn=500
fs=100000

tiempo , espacio = funcion_sen(vmax,dc,ff,ph,nn,fs)

plt.plot(tiempo,espacio,label="500hz", linestyle='-' ,color='r')

#caso frecuencia 999

ff=999
ph=0
vmax=1
dc=0
nn=500
fs=100000

tiempo , espacio = funcion_sen(vmax,dc,ff,ph,nn,fs)

plt.plot(tiempo,espacio, label="999hz",linestyle='-' ,color='b')

#caso frecuencia 1001

ff=1001
ph=0
vmax=1
dc=0
nn=500
fs=100000

tiempo , espacio = funcion_sen(vmax,dc,ff,ph,nn,fs)

plt.plot(tiempo,espacio, label="1001hz",linestyle='-' ,color='g')

#caso frecuencia 2001

ff=2001
ph=0
vmax=1
dc=0
nn=500
fs=250000

tiempo , espacio = funcion_sen(vmax,dc,ff,ph,nn,fs)

plt.plot(tiempo,espacio, label="2001hz",linestyle='-' ,color='y')

plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis([np.min(tiempo),np.max(tiempo),np.min(espacio)-0.5,np.max(espacio)+0.5]) #en donde aparece el cuadro
plt.legend() 
plt.draw()


plt.tight_layout() 
plt.show()


