# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 21:08:54 2021

@author: Agustin Podesta
"""

import numpy as np
a = np.array([1,2,3,4,5,6])
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a[0])

np.zeros(2)
np.ones(2)
np.empty(2)
np.arange(4)
np.arange(1,10,3)
np.linspace(1,5,num=7)

np.arange(1,20,2)
np.linspace(1,19,num=10, dtype=np.int64)

a = np.array([1, 2, 3, 4])
b = np.array([5, 4, 7, 8])
np.concatenate((a,b))

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
np.concatenate((x, y), axis=0)
x[1]

array_ejemplo = np.array([[[0, 1, 2, 3],[4, 5, 6, 7]],
                          [[0, 1, 2, 3],[4, 5, 6, 7]],
                          [[0 ,1 ,2, 3], [4, 5, 6, 7]]])
                          
#Eje X: seria la cantidad de grupos de listas de alguna manera, osea [[...]],[[...]],[[...]] que en este caso son 3.
#Eje Y: seria la cantidad de listas en c/grupo, osea [[...],[...]],[[...],[...]],[[...],[...]] que en este caso son 2 listas por grupo.
#Eje Z: seria la cantidad de valores dentro de c/lista dentro de c/grupo, osea [a,b,c,d] que en este caso son 4.

# x = 000 , 444 , ... (rango: 0-3)
# y = 04 (rango: 0-2)
#z = 01234, 4567, ... (rango: 0-4)
a = np.arange(7)
b = a.reshape(3,2)
vec_fila = a[:, np.newaxis]
vec_fila.shape

a = np.array([[1, 2, 3, 4], [5, 4, 7, 3], [2, 10, 3, 12]])
y = a>=3
print(a[y])
b = np.nonzero(a<5)
print(b)
lista_de_coordenadas = list(zip(b[0],b[1]))
print(lista_de_coordenadas)
b1 = a[1,1:] #el primer 1 indica la segunda celda, y el segundo 1 indica desde donde en la celda, osea desde la psoicion 1 de la segunda celda.
print(b1)

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
...               [0.54627315, 0.05093587, 0.40067661, 0.55645993],
...               [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

a.min(axis = 0)

np.ones(3)
np.zeros(3)
rng = np.random.default_rng(0)
rng.random(3)
np.random.random(3)
rng.random((3,2))

#Guardar un array como .npy 
a = np.array([1,2,3,4,5,6])
np.save('filename', a)
b = np.load('filename.npy')   
print(b)

#Guardar un array como .csv o .txt
csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.savetxt('new_file.csv', csv_arr)
np.loadtxt('new_file.csv')

a = np.array([1,2,3])
b = a[:].copy()
b[0] = 2
b

data = np.array([[1, 2], [3, 4], [5, 6]])
data[0:3, 1]
    
    