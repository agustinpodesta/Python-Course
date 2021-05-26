
def ord_burbujeo(lista):
    comparaciones, intercambios = 0, 0
    #Voy a necesitar dos ciclos for. El interno (de for j), es para recorrer toda la lista y
    #llevar el mayor valor hasta el final de la lista. Ej: [3,8,7,4] --> [3,7,8,4] -->[3,7,4,8]
    #Pero eso no me garantiza que la lista haya quedado ordenada. Es por esto que estas
    #recorridas se repiten sucesivas veces (ahi entra el for externo de i) de manera de
    #garantizar que el lista quede completamente ordenada.
    for i in range(len(lista)):
        for j in range(1, len(lista)-i): #Aca va de 1 hasta len(lista) - 1 nunca llega hasta 
                                         #el ultimo valor en un range. 
            comparaciones += 1
            #Comparemos el si el valor anterior es mayor que el siguiente,
            #si es asi se los intercambia. 
            if lista[j-1] > lista[j]:
                intercambios += 1
                lista[j-1], lista[j] = lista[j], lista[j-1]
    return comparaciones, intercambios

ord_burbujeo([3, 8, 7, 4])

#Probando con varias listas, cambiando el orden y el largo, me di cuenta que el numero total
#de comparaciones es (n - 1) + (n - 2) + (n-3) +(n-4) +(n-5) ...(2) + (1). Y eso es lo mismo
#que n(n - 1)/2 i.e, n^2.
