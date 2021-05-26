# -*- coding: utf-8 -*-

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""   

    if len(lista) < 2:
        return lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)

    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    global cont
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        cont +=1 #Incremento el contador cuando se comparan valores.
        
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    while i < len(lista1): 
        resultado.append(lista1[i])
        i +=1
        cont +=1
    while j < len(lista2):
        resultado.append(lista2[j])
        j +=1
        cont +=1

    return resultado

def generar_lista(N):
    import numpy as np
    lista = np.random.randint(1, 300, N)
    return lista 

def imprimir_merge(lista):
    global cont
    cont = 0
    merge_sort(lista)

