# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:31:45 2021

@author: Agustin Podesta
"""
import random
def generador_punto():
    x = random.random()
    y = random.random()
    return x,y

ver = generador_punto()

def pi(x):
    if x[0]**2 + x[1]**2 < 1:
        verdad = True
    else:
        verdad = False
    return verdad

epa = pi(ver)

N = 1000000
M = sum([pi(generador_punto()) for i in range(N)])
pi = 4*(M/N)
print(f'Realizando una simulacion de {N} veces, entre ellas, {M} veces los puntos cayeron dentro del circulo unitario')
print(f'Con este se obtuvo un valor de pi = {pi:.7f}')


