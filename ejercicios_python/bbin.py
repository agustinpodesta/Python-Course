# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:03:09 2021

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



def impresion(lista, x, verbose = False):
    pos_si, insercion, pos_no, comps = busqueda_binaria(lista, x, verbose)
    print(f'Se realizaron {comps} comparaciones')
    if pos_si == -1:
        respuesta = print(f'No se encontro el {x} en la lista, pero si se agregara quedaria asi: {insercion} \nEs decir que se lo colocó en la posicion {pos_no}')
    else:
        respuesta = print(f'El valor {x} fue encontrado en la posicion {pos_si}')
    return respuesta

impresion([1,2,3,4,5,6,7,8], 9, verbose=True)
