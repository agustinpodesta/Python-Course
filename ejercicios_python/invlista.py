def invertir_lista(lista):
    invertida = []
    long=len(lista)
    for n_e,e in enumerate(lista,start=1): # Recorro la lista      
        invertida.append(e)
        invertida[n_e-1]=lista[long-1]
        long =long - 1
    return invertida



