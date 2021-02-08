def buscar_u_elemento(lista,elemento):
    'Recibe una lista y un elemento y devuelva la posición de la última aparición de ese elemento en la lista (o -1 si el elemento no pertenece a la lista)'
    pos=-1
    for n_s,s in enumerate(lista):
        if s==elemento:
            pos=n_s
        else:
            continue
    return pos

    
def buscar_n_elemento(lista,elemento):
    'Recibe una lista y un elemento y devuelva la cantidad de veces que aparece el elemento en la lista.'
    from collections import Counter
    cant=Counter()
    for n_s,s in enumerate(lista):
        if s==elemento:
            cant[s] +=1
        else: 
            continue
    if cant==Counter():
        respuesta=print(f'El numero {elemento} no se encuentra en la lista')
        return respuesta
    else:
        return cant




