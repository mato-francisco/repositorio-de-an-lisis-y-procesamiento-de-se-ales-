import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
def funcion_sen(ff,nn,vmax=1,dc=0,ph=0,fs=2):#todas las variables que estan igualadas a un valor seran las 
                                             #opcionale y si nos las pongo cuando llamo la funcion toma esos 
                                             #valore. fs = 2 para que cumpla nyquis 
    
    t=np.arange(0,(nn)/fs,1/fs)
   
    y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    
    return t,y 

nn=1000
fs=nn
deltaf=fs/nn


x , y =funcion_sen( (nn/4)*deltaf,nn,fs=fs)

sigma=np.std(y)

print(sigma)

ynormalizada=y/sigma

print(np.var(ynormalizada))

energia_n=np.sum(np.abs(ynormalizada)**2)

print(energia_n)

ffty=np.fft.fft(ynormalizada)#tranfromo la funcion SIN normalizar por el desvio estandar 

energia_f=np.sum(np.abs(ffty)**2)

print("energia en x")

print(energia_n)

print("energia en f normalizada por n")

print((energia_f)/nn)