def buscar_u_elemento(lista,elemento):
    '''Recibe una lista y un elemento y devuelva la posición de la última
    aparición de ese elemento en la lista (o -1 si el elemento no pertenece a la lista)'''
    pos=-1
    for n_s,s in enumerate(lista):
        if s==elemento:
            pos=n_s
        else:
            continue
    return pos

    
def buscar_n_elemento(lista,elemento):
    '''Recibe una lista y un elemento y devuelva la cantidad
    de veces que aparece el elemento en la lista.'''
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


def maximo(lista):
    '''Devuelve el máximo de una lista, la lista debe ser
    no vacía y de números positivos.'''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m=e
        else:
            continue
    if m==0:
        for s in lista: #Ej recorriendo [-5,4]
            m=s #m=-5
            if s > m: #si s=-5 y m=-5, no cumple y sigue. Y en la siguiente vuelta s=-4 > m=-5 cumple
                m=s #Por lo que ahi m pasa a ser -4, osea el maximo de los numeros negativos
            else:
                continue         
    return m            
