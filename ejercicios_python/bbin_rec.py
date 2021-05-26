#Busqueda binaria

def bbinaria_rec(lista, e):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''    
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] == e:
            res = True     # elemento encontrado!
            return res
       
        if lista[medio] > e:
            res = bbinaria_rec(lista[:medio], e) # descarto mitad derecha
        else:              # if listamedio] < e:
            res = bbinaria_rec(lista[medio + 1:], e) # descarto mitad izquierda

    return res

bbinaria_rec([1, 3, 4, 5, 6], 6)
