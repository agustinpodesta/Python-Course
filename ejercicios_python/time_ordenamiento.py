#MERGE SORT
#%%
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
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
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
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
    while j < len(lista2):
        resultado.append(lista2[j])
        j +=1

    return resultado

def generar_lista(N):
    import numpy as np
    lista = np.random.randint(1, 300, N)
    return lista 

def imprimir_merge(lista):
    global cont
    cont = 0
    merge_sort(lista)

#%%


#SELECTION SORT    
#%%
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n) 

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]

        # reducir el segmento en 1
        n = n - 1
    return lista

#Aclaracion: este es el algoritmo mas simple para contar la cantidad de comparaciones que 
#hace, ya que independientemente de como este desordenada la lista, el resultado siempre
# es n(n-1)/2, siendo n el largo de la lista. 

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

#%%


#INSERTION SORT
#%%
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v


#%%


#BUBBLE SORT
#%%
def ord_burbujeo(lista):
    #Voy a necesitar dos ciclos for. El interno (de for j), es para recorrer toda la lista y
    #llevar el mayor valor hasta el final de la lista. Ej: [3,8,7,4] --> [3,7,8,4] -->[3,7,4,8]
    #Pero eso no me garantiza que la lista haya quedado ordenada. Es por esto que estas
    #recorridas se repiten sucesivas veces (ahi entra el for externo de i) de manera de
    #garantizar que el lista quede completamente ordenada.
    for i in range(len(lista)):
        for j in range(1, len(lista)-i): #Aca va de 1 hasta len(lista) - 1 nunca llega hasta 
                                         #el ultimo valor en un range. 
            #Comparemos el si el valor anterior es mayor que el siguiente,
            #si es asi se los intercambia. 
            if lista[j-1] > lista[j]:
                lista[j-1], lista[j] = lista[j], lista[j-1]
    return 

#%%
       
import matplotlib.pyplot as plt
import numpy as np


#Aparentemente tanto en ordenamiento por burbuja como en por seleccion, la cantidad de 
#comparaciones es siempre la misma, sin importar el orden de la lista. Por lo tanto, calculo
#primero el numero de comparaciones con el ordenamiento por insercion, y una vez ordenada la 
#lista, calculo las comparaciones para el resto de los ordenamientos. 
#listas = [np.random.randint(minx, maxx, N) for i in range (k)]
def generar_listas(N):
    import numpy as np
    listas = []
    for N in range(1, N):
        lista = np.random.randint(1, 1000, N)
        listas.append(lista)
    return listas   


listas = generar_listas(257)


import time
import timeit as tt
def experimento_timeit(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección, insercion, burbujeo, y mezcla para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método para cada lista.
    """
    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_burbujeo = []
    tiempos_mezcla = []
    
    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number = num, globals = globals())
        tiempo_mezcla = tt.timeit('merge_sort(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        tiempos_insercion.append(tiempo_insercion)
        tiempos_burbujeo.append(tiempo_burbujeo)
        tiempos_mezcla.append(tiempo_mezcla)
        
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    tiempos_mezcla = np.array(tiempos_mezcla)
    
    return tiempos_seleccion, tiempos_insercion, tiempos_burbujeo, tiempos_mezcla

tiempos_seleccion = experimento_timeit(listas, 100)[0]
tiempos_insercion = experimento_timeit(listas, 100)[1]
tiempos_burbujeo = experimento_timeit(listas, 100)[2]
tiempos_mezcla = experimento_timeit(listas, 100)[3]

plt.plot(tiempos_seleccion, label = 'Ordenamiento por seleccion')
plt.plot(tiempos_insercion, label = 'Ordenamiento por insercion')
plt.plot(tiempos_burbujeo, label = 'Ordenamiento por burbujeo')
plt.plot(tiempos_mezcla, label = 'Ordenamiento por mezcla')
plt.legend(loc='upper left',  bbox_to_anchor=(1,1))
plt.show()