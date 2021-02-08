# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 12:46:18 2020

@author: Agustin Podesta
"""         
def propagar(vector):
    propagacion=[]
    for n_a,a in enumerate(vector):
        propagacion.append(a)
        if a == 0 and 1 in propagacion[n_a-1:n_a]:
            propagacion[n_a] = 1
        elif a == 0 and 1 in vector[n_a:n_a+2]:
            propagacion[n_a] = 1
        if a == 1: #de aca nos separamos en dos caminos, en si antes del 1 aparecio un -1 o no.
            if -1 not in propagacion[:n_a]:
                for n_b,b in enumerate(propagacion):
                    propagacion[n_b]=1
    print(propagacion)
    for n_c,c in enumerate(propagacion[::-1]):
        print('c es:',c)
        print('anterior',propagacion[::-1][n_c-1])
        if c == 0 and propagacion[::-1][n_c-1] == 1:
            print('HOLA')
            propagacion[-n_c-1] = 1
            print('nueva c:',c)
        elif c == -1:
            break
            
    return propagacion
                
            
propagar([0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0,-1, 0, 0, 1])         
propagar([0, 0, 0, 1, 0, 0,-1, 0, 0, 0, 1])       


x

