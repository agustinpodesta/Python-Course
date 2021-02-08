# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 18:17:49 2021

@author: Agustin Podesta
"""
def envido():
    import random
    from collections import Counter
    valores = [1,2,3,4,5,6,7,10,11,12]
    palos = ['oro', 'copa','espada','basto']
    naipes = [(palo,valor) for palo in palos for valor in valores]
    muestra = random.choices(naipes, k=3)
    palos = [e[0] for e in muestra] 
    contador = Counter(palos)
    veces_repetido = contador.most_common()[0][1]
    if veces_repetido == 2: #Si en las 3 cartas, hay dos del mismo palo.
        palo_repetido = contador.most_common()[0][0]
        for n_i,i in enumerate(muestra):
            if muestra[n_i][1] == 10 or muestra[n_i][1] == 11 or muestra[n_i][1] == 12:
                muestra[n_i] =  muestra[n_i][0], 0
        suma = sum([e[1] for e in muestra if e[0] in (palo_repetido,)]) + 20
        if suma > 30:
            verdad = True
            return verdad
        else:   
            verdad = False
            return verdad
    else:
        verdad = False
        return verdad
                
ver = envido()              
    
N = 100000
G = sum([envido() for i in range(N)])        
prob = G/N
veces = 1/prob
print(f'\n Jugué {N} veces, de las cuales {G} tuve un envido de la puta madre (31,32,33).')
print(f'Podemos estimar la probabilidad de sacar ese envido mediante {prob:.6f}.')
print(f'En promedio, uno debe jugar {veces:.0f} veces para obtener una generala servida.')