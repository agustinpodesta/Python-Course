# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 15:56:45 2021

@author: Agustin Podesta
"""
import random
import numpy as np
def crear_album(figus_total):
    '''Devuelve un álbum (vector) vacío con figus_total espacios para pegar figuritas''' 
    album = np.zeros(figus_total)
    return album

A = crear_album(670)

def album_incompleto(album):
    '''Nos dice si hay al menos un cero en el vector que representa el álbum'''
    verdad = False
    for i in album:
        if i == 0:
            verdad = True
            return verdad
        else:
            continue
    return verdad

B = album_incompleto(A)


def compar_figu(figus_total):
    '''Recibe el número total de figuritas/espacios que tiene el álbum (dado por el parámetro figus_total) y devuelve un número entero aleatorio que representa la figurita que nos tocó. '''
    figurita = random.randint(0,figus_total-1)
    return figurita



def cuantas_figus(figus_total):
    '''dado el tamaño del álbum (figus_total), genere un álbum nuevo, simule su llenado y devuelva la cantidad de figuritas que se debieron comprar para completarlo.'''
    contador = 0
    nuevo_album = A[:].copy()
    while album_incompleto(nuevo_album) == True:
        nuevo_album[compar_figu(figus_total)] += 1
        contador += 1
    return contador


    
N = 100                         
total_figuritas = [cuantas_figus(670) for i in range(N)]
total_figuritas_promedio= np.mean(total_figuritas)
print(f'Se tuvieron que comprar {total_figuritas_promedio} figuritas en promedio para completar el album de {A.size} figuritas')

