# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 09:40:33 2021

@author: Agustin Podesta
"""

def incrementar(s):
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s

def listar_secuencias(n):
    inicio = [0]*n
    print(inicio)
    while inicio != [1]*n:
        inicio = incrementar(inicio)
        print(inicio)
    return inicio

listar_secuencias(10)

#La cantidad de listas que se formen va a ser proporcional a 2^n