import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sp

def funcion_sen(vmax,dc,ff,ph,nn,fs):
    
    t=np.arange(0,(nn)/fs,1/fs)
    
    y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    
    return t ,y 


#Una señal sinusoidal de 2KHz y Misma señal amplificada y desfazada en π/2.-----

ff=2000
ph=0
vmax=1
dc=0
nn=500
fs=500000


tiempo_a , espacio_a = funcion_sen(vmax,dc,ff,ph,nn,fs)

tiempo_b , espacio_b = funcion_sen(np.pi/2,dc,ff/2,np.pi/2,nn,fs)

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(tiempo_a,espacio_a,label=f"N = {nn}, fs = {fs}" ,linestyle='',marker="." ,color='r')
plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

plt.subplot(2,1,2)
plt.plot(tiempo_b,espacio_b,label=f"N = {nn}, fs = {fs}", linestyle='',marker="." ,color='g')
plt.legend()

plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis([np.min(tiempo_b),np.max(tiempo_b),-2,2]) 

plt.tight_layout()
plt.draw()
#Misma señal modulada en amplitud por otra señal sinusoidal de la mitad de la frecuencia
tiempo_c , espacio_c = funcion_sen(vmax,dc,ff/2,ph,nn,fs)

espacio_ac=espacio_a *espacio_c

plt.figure(2)

plt.plot(tiempo_a,espacio_a,label="señal", linestyle='-.' ,color='r')
plt.plot(tiempo_b,espacio_c,label="señal a mitad de frecuencia", linestyle='-.' ,color='g')
plt.plot(tiempo_a,espacio_ac,label="señal modulada", linestyle='-' ,color='b')
plt.legend()

plt.grid(True, linestyle=':') 
plt.title(f"N = {nn}, fs = {fs}")
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis([np.min(tiempo_b),np.max(tiempo_b),-2,2]) #en donde aparece el cuadro
plt.draw()
#Señal anterior recortada al 75% de su amplitud------------------------
recortada=np.clip(espacio_a,-0.375,0.375)

plt.figure(3)

plt.plot(tiempo_a,espacio_a, linestyle='-.' ,color='r')

plt.plot(tiempo_a,recortada, linestyle='-' ,color='b')


plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis([np.min(tiempo_b),np.max(tiempo_b),-2,2]) 

plt.draw()
#Una señal cuadrada de 4KHz-------------------------------------------
nn=501
ff=4000
t=np.linspace(0,20*1/ff,nn)
espacio_cuadrado=sp.square(2 * np.pi * ff * t)

plt.figure(4)

plt.plot(t,espacio_cuadrado, label=f"N={nn},fs={ff*nn}",marker="x" ,color='b')
plt.legend()

plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis([0,0.001,-2,2]) 
plt.draw()
#Un pulso rectangular de 10ms------------------------------------------------
N=501

tiempo_pulso=np.linspace(0,1/10,N)

pulso=np.zeros(N,dtype=float)
for k in np.arange(0,N):
    if(tiempo_pulso[k]<0.01):
        
        pulso[k]=1
    else:
        pulso[k]=0

plt.figure(5)
plt.plot(tiempo_pulso,pulso,linestyle='-' ,color='b')


plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis([0,1/10,-1,2]) 
plt.draw()
#Verificar ortogonalidad entre la primera señal y las demás-------------------
ortogonalida_1_2=np.inner(espacio_a,espacio_b)
print(ortogonalida_1_2)

ortogonalida_1_3=np.inner(espacio_a,espacio_ac)
print(ortogonalida_1_3)

ortogonalida_1_4=np.inner(espacio_a,recortada)
print(ortogonalida_1_4)

ortogonalida_1_5=np.inner(espacio_a,espacio_cuadrado)
print(ortogonalida_1_5)

ortogonalida_1_5=np.inner(espacio_a,pulso)
print(ortogonalida_1_5)

#Graficar la autocorrelación de la primera señal y la correlación entre ésta y las demás

correlacion_a_b=np.corrcoef(espacio_a,espacio_b)
correlacion_a_ac=np.corrcoef(espacio_a,espacio_ac)
correlacion_a_recortada=np.corrcoef(espacio_a,recortada)
correlacion_a_rectangular=np.corrcoef(espacio_a,espacio_cuadrado)
correlacion_a_pulso=np.corrcoef(espacio_a,pulso)


plt.figure(6)
plt.plot(tiempo_a,espacio_a,label="autocorelacion",marker=".",linestyle="" ,color='b')
plt.plot(tiempo_a,espacio_b,label="correlacion_a_desfasada",marker=".",linestyle="" ,color='r')
plt.plot(tiempo_a,espacio_ac,label="correlacion_a_modulada",marker="." ,linestyle="",color='g')
plt.plot(tiempo_a,recortada,label="correlacion_a_recortada",marker=".",linestyle="" ,color='y')
plt.plot(tiempo_a,espacio_cuadrado,label="correlacion_a_rectangular",marker="." ,linestyle="",color='k')
plt.plot(tiempo_a,pulso,label="correlacion_a_pulso",marker="." ,linestyle="",color='m')
plt.legend()

plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.draw()

