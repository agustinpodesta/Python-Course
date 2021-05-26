#MERGE SORT
#%%
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

#%%


#SELECTION SORT    
#%%
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    cont_2 = 0
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)[0] 
        cont_1 = buscar_max(lista, 0, n)[1]
        cont_2 += cont_1

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]

        # reducir el segmento en 1
        n = n - 1
    return cont_2

#Aclaracion: este es el algoritmo mas simple para contar la cantidad de comparaciones que 
#hace, ya que independientemente de como este desordenada la lista, el resultado siempre
# es n(n-1)/2, siendo n el largo de la lista. 

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    cont_2 = 0
    pos_max = a
    for i in range(a + 1, b + 1):
        cont_2 += 1
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max, cont_2


#%%


#INSERTION SORT
#%%
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    cont_1 = 0
    cont_3 = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        cont_1 += 1
        if lista[i + 1] < lista[i]:
            cont_2 = reubicar(lista, i + 1)
            cont_3 += cont_2 
    return cont_3 + cont_1

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    cont_2 = 0
    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        cont_2 +=1

    lista[j] = v
    return cont_2


#%%

       
import matplotlib.pyplot as plt
import numpy as np
from burbujeo_posta import ord_burbujeo

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
listas_insercion = listas.copy()
listas_burbuja = listas.copy()
listas_seleccion = listas.copy()
listas_mezcla = listas.copy()

#Ordenamiento por insercion:
insercion = [ord_insercion(i) for i in listas_insercion]

#Ordenamiento por burbuja:
burbuja = [ord_burbujeo(i)[0] for i in listas_burbuja]

#Ordenamiento por seleccion:
seleccion = [ord_seleccion(i) for i in listas_seleccion]

#Ordenamiento por mezcla:
mezcla = []
for i in listas_mezcla:
    imprimir_merge(i)
    mezcla.append(cont)

x = np.linspace(0, 80, num = 256)

plt.plot(x, insercion, label = 'Ordenamiento por insercion')
plt.plot(x, burbuja, color = 'yellow', label = 'Ordenamiento por burbuja')
plt.plot(x, seleccion, linestyle = (0, (1, 10)), color = 'red', label = 'Ordenamiento por seleccion')
plt.plot(x, mezcla, label = 'Ordenamiento por mezcla')
plt.legend(loc='upper left',  bbox_to_anchor=(1,1))
plt.show()





