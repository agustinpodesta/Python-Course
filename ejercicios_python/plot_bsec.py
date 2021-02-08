# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:51:34 2021

@author: Agustin Podesta
"""

import random

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primer aparición, 
    de lo contrario devuelve -1.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def generar_lista(n, m):
    ''' Devuelve una lista ordenada de n elementos diferentes entre 0 y m-1 '''
    
    l = random.sample(range(m), k = n) #Ej: print(sample([1, 2, 3, 4, 5], 3)) = [2, 3, 5]
    l.sort()
    return l

def generar_elemento(m):
    ''' devuelve un elemento aleatorio entre 0 y m-1'''
    
    return random.randint(0, m-1)

m = 10000
n = 100
#Osea la lista va tomar valores entre 0 y 10000, pero solo van a ser 100 numeros.
k = 1000
lista = generar_lista(n, m)

def experimento_secuencial_promedio(lista, m, k):
    '''El siguiente código da la cantidad de comparaciones promedio en k
    experimentos elementales'''
    
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

import matplotlib.pyplot as plt
import numpy as np

largos_1 = np.arange(256) + 1 # estos son los largos de listas que voy a usar (el +1 es para que arranque desde 1 y no desde 0)
comps_promedio_1 = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos_1):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio_1[i] = experimento_secuencial_promedio(lista, m, k) #El promedio se hacia solo una vez, por eso lo meto en un for para que me lo haga muchas veces.

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos_1,comps_promedio_1,label = 'Búsqueda Secuencial')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaiciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()


