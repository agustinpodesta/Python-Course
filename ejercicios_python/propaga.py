# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 10:52:25 2020

@author: Agustin Podesta
"""


def propagar_al_vecino(l):
    condicion = False
    largo = len(l)
    for n_i , i in enumerate(l):
        if i == 1 and n_i < largo-1 and l[n_i+1] == 0: 
#Esto es para ver si un 1 tiene ADELANTE un 0, para convertirlo en un 1, pero tiene la 
#condicion de que si ese 1 es el ultimo numero de la lista (n_i < largo-1), no entra 
#en el if. Ya que de no poner esto, el l[n_i+1] == 0 me daria un 'List out of range'.
            l[n_i+1] = 1
            condicion = True
        if i == 1 and n_i > 0 and l[n_i-1] == 0:
#Esto es para ver si un 1 tiene ATRAS un 0, para convertirlo en un 1, pero tiene la 
#condicion de que si ese 1 es el primer numero de la lista (n_i > 0), no entra 
#en el if. Ya que de no poner esto, el l[n_i-1] == 0 me daria un 'List out of range'.
            l[n_i-1] = 1
            condicion = True
        else:
            continue
    return condicion
    
def propagar(l):
    m = l.copy()
    veces = 0
    while propagar_al_vecino(l): 
#Esto es sinonimo de decir "mientras que propagar_al_vecino(l) == True, que entre al while"
#propagar_al_vecino(l) es True o False dependiendo de la variable "condicion", ya que esto es
#lo que devuelve la funcion.
        veces += 1
    print(f'Lista introducida: {m}')
    print(f'Lista obtenida: {l}')
    print(f'la funcion: propagar_al_vecino, fue repetida {veces} veces')
    return m
        
propagar([0,0,0,0,1])
propagar([1,0,0,0,0])
            
            
#%%
#OTRA FORMA PIOLA. Inspirada en el auto fantastico.
def propagar_a_derecha(l):
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1:
            if l[i+1]==0:
                l[i+1] = 1
    return l
#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]
# propagar_a_derecha(l[::-1]) aplica a la funcion para l = [1, 1, 1, 0, -1, 1, 1, 1, 1, -1, 0, 0, 0]
# y de esa forma ese 0 en la posicion 3, se cambia por un 1. Y luego a la lista resultante
# la invierte devuelta y entonces queda el resultado final.
#%
def propagar(l):
    ld=propagar_a_derecha(l)
    lp = propagar_a_izquierda(ld)
    return lp
#%%
l = [0,0,0,0,1]
m = l.copy()
print("Estado original:  ",l)
print("Porpagando...")
lp=propagar(l)
print("Estado original:  ",m)
print("Estado propagado: ",lp)



