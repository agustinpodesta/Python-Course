# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 11:55:59 2021

@author: Agustin Podesta
"""

#Ejercicio 4.6: Generala servida

def tirar():
    import random
    tirada = []
    for i in range(5):
        dado = random.randint(1,6)
        tirada.append(dado)
    return tirada


def es_generala(tirada):
    for n_i,i in enumerate(tirada):
        if tirada[n_i] == tirada[n_i - 1]: #Aca lo que hace es fijarse si el primer valor de la lista es igual al ultimo, si el segundo es igual al anteultimo, si el tercero es igual al antepenultimo y asi sucesivamente.
            verdad = True
        else:
            verdad = False
            break
    return verdad
  

N = 100000
G = sum([es_generala(tirar()) for i in range(N)])        
prob = G/N
veces = 1/prob
print(f'\n Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
print(f'En promedio, uno debe tirar los dados {veces:.0f} veces para obtener una generala servida.')

#Por si no entendiste el concepto del True y False
x = [False, True, True]
suma = sum([s for s in x])
suma

#Ejercicio 4.7: Generala no necesariamente servida
import random
from collections import Counter
def tirar():
    tirada_1 = []
    for i in range(5):
        dado = random.randint(1,6)
        tirada_1.append(dado)
    return tirada_1


def es_generala(tirada_1):
    for n_a,a in enumerate(tirada_1): #En el caso de que en el primer intento salga generala
        if tirada_1[n_a] == tirada_1[n_a - 1]:
            verdad = True
        else:
            verdad = False
            break
    if verdad == True:
        return verdad
    else:
        contador_1 = Counter(tirada_1)
        repetida_1 = contador_1.most_common()[0][0] #En el caso de que sean todos valores diferentes agarra el primero de la lista
        tirada_2 = [e for e in tirada_1 if e not in (repetida_1,)] 
        resto_1 = [e for e in tirada_1 if e in (repetida_1,)]
        for n_i,i in enumerate(tirada_2):
            dado = random.randint(1,6)
            tirada_2[n_i] = dado
        contador_2 = Counter(tirada_2)
        repetida_2 = contador_2.most_common()[0][0]
        tirada_3 = [e for e in tirada_2 if e not in (repetida_2,)]
        resto_2 = [e for e in tirada_2 if e in (repetida_2,)]
        for n_s,s in enumerate(tirada_3):
            dado = random.randint(1,6)
            tirada_3[n_s] = dado
        total = resto_1 + resto_2 + tirada_3
        for n_p,p in enumerate(total):
            if total[n_p] == total[n_p - 1]:
                verdad = True
            else:
                verdad = False
                break
        return verdad


N = 100000
G = sum([es_generala(tirar()) for i in range(N)])        
prob = G/N
veces = 1/prob
print(f'\n Usando las reglas originales, tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida en serio mediante {prob:.6f}.')
print(f'En promedio, usando las reglas originales uno debe tirar los dados {veces:.0f} veces para obtener una generala servida.')
  

#Estrategia de otros: si en la primera tirada salen todos dados diferentes, se meten al cubilete y tira los cinco nuevamente.
import random
from collections import Counter
def tirar():
    tirada_1 = []
    for i in range(5):
        dado = random.randint(1,6)
        tirada_1.append(dado)
    return tirada_1

tire = tirar()

def es_generala(tirada_1):
    for n_a,a in enumerate(tirada_1): #En el caso de que en el primer intento salga generala
        if tirada_1[n_a] == tirada_1[n_a - 1]:
            verdad = True
        else:
            verdad = False
            break
    if verdad == True: #En el caso de que sean todos =, que la funcion termine y no siga con el resto.
        return verdad
    else:
        contador_1 = Counter(tirada_1)
        repetida_1 = contador_1.most_common()[0][0] #En el caso de que sean todos diferentes agarra uno al azar
        tirada_2 = [e for e in tirada_1 if e not in (repetida_1,)] 
        resto_1 = [e for e in tirada_1 if e in (repetida_1,)]
        if tirada_1[n_a] != tirada_1[n_a - 1]:
            tirada_2 = tirar()
            resto_1 = []
        for n_i,i in enumerate(tirada_2):
            dado = random.randint(1,6)
            tirada_2[n_i] = dado
        contador_2 = Counter(tirada_2)
        repetida_2 = contador_2.most_common()[0][0]
        tirada_3 = [e for e in tirada_2 if e not in (repetida_2,)]
        resto_2 = [e for e in tirada_2 if e in (repetida_2,)]
        if tirada_2[n_a] != tirada_2[n_a - 1]:
            tirada_3 = tirar()
            resto_2 = []
        for n_s,s in enumerate(tirada_3):
            dado = random.randint(1,6)
            tirada_3[n_s] = dado
        total = resto_1 + resto_2 + tirada_3
        for n_p,p in enumerate(total):
            if total[n_p] == total[n_p - 1]:
                verdad = True
            else:
                verdad = False
                break
        return verdad


N = 100000
G = sum([es_generala(tirar()) for i in range(N)])        
prob = G/N
veces = 1/prob
print(f'\n Usando las reglas originales, tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida en serio mediante {prob:.6f}.')
print(f'En promedio, usando las reglas originales uno debe tirar los dados {veces:.0f} veces para obtener una generala servida.')
  




