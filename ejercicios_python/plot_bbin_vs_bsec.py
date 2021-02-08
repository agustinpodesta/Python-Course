# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:32:02 2021

@author: Agustin Podesta
"""

def donde_insertar(lista, x):   
    '''
    Inserta el numero 'x' en la lista
    '''
    for n_i,n in enumerate(lista):
        if x > n:
            if n_i == len(lista) - 1:
                lista.append(x)
                posicion = n_i + 1
                break
            continue
        if x <= n and x!=n:
            lista.insert(n_i,x)
            posicion = n_i
            break
    return lista, posicion
    
            

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos_si = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    insercion = None
    pos_no = -1
    comps = 0 # inicializo en cero la cantidad de comparaciones
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        comps += 1
        if lista[medio] == x:
            pos_si = medio     # elemento encontrado! 
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if pos_si == -1:
        insercion, pos_no = donde_insertar(lista, x)
    return pos_si, insercion, pos_no, comps

import random


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

def experimento_binario_promedio(lista, m, k):
    '''El siguiente código da la cantidad de comparaciones promedio en k
    experimentos elementales'''
    
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[3]

    comps_prom = comps_tot / k
    return comps_prom

import matplotlib.pyplot as plt
import numpy as np

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar (el +1 es para que arranque desde 1 y no desde 0)
comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio[i] = experimento_binario_promedio(lista, m, k) #El promedio se hacia solo una vez, por eso lo meto en un for para que me lo haga muchas veces.

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos,comps_promedio,label = 'Búsqueda Binaria')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaiciones")
plt.title("Complejidad de la Búsqueda")
plt.ylim(8,10)
plt.legend()

import plot_bsec

plt.plot(plot_bsec.largos_1,plot_bsec.comps_promedio_1,label = 'Búsqueda Secuencial')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaiciones")
plt.title("Complejidad de la Búsqueda")
plt.ylim(8,10)
plt.legend()
