# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 15:42:25 2021

@author: Agustin Podesta
"""

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


def comprar_paquete(figus_total, figus_paquete):
    '''Recibe el número total de figuritas/espacios que tiene el álbum (dado por el parámetro figus_total) y devuelve un número entero aleatorio que representa la figurita que nos tocó. '''
    paquete = []
    for i in range (figus_paquete):
        figurita = random.randint(0,figus_total-1)
        paquete.append(figurita)
    return paquete
      


#D = comprar_paquete(10,5)

def cuantos_paquetes(figus_total, figus_paquete):
    '''dado el tamaño del álbum (figus_total), genere un álbum nuevo, simule su llenado y devuelva la cantidad de figuritas que se debieron comprar para completarlo.'''
    contador = 0
    nuevo_album = A[:].copy()
    while album_incompleto(nuevo_album) == True:
        for i in comprar_paquete(figus_total, figus_paquete):
            nuevo_album[i] += 1
        contador += 1
    return contador

#C = cuantos_paquetes(10,5)
    
N = 100                         
total_paquetes = [cuantos_paquetes(670,5) for i in range(N)]
total_paquetes_promedio= np.mean(total_paquetes)
print(f'Se tuvieron que comprar {total_paquetes_promedio} paquetes en promedio para completar el album de {A.size} figuritas')

#%% GRAFICO
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete: #Si el paquete, que es una lista, se queda vacio [], va a pasar a ser False.
            album[paquete.pop()] = 1 #Aca .pop() devuelve la ultima carta del paquete y se la saca al paquete. Y el album en la posicion de esa figurita pasa a ser 1.
        figus_pegadas = (album>0).sum() #Ej: album = [1,0,2], album>0 = [True, False, True], (album>0).sum() = 2
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas
#Aca "historia_figus_pegadas" seria mi funcion Y, que depende de "paquete" que seria mi X, el cual va variando en cada loop, segun la funcion comprar_paquete que esta mas arriba. 

figus_total = 670
figus_paquete = 5

import matplotlib.pyplot as plt
plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()

#%% ESTADISTICA

#Ejercicio: Probabilidad de completar el álbum con 850 paquetes o menos.

total_paquetes_850 = [e for e in total_paquetes if (e<=850)]
proba_850 = len(total_paquetes_850)/N
print(f'La probabilidad de completar el álbum con 850 paquetes o menos es de: {proba_850}')

#Otra forma parecida es convertir la lista "total_paquetes" en un array y a ese aplicarle la condicion de >= 850, que me va a devolver un array de booleanos los cuales se pueden sumar y luego dividir por N.
n_paquetes_hasta_llenar=np.array(total_paquetes)
booleanos = (n_paquetes_hasta_llenar <= 850).sum()
booleanos/N

#Ejercicio: Plotear el histograma
plt.hist(total_paquetes, bins =25)

#Ejercicio: estimar cuántos paquetes habría que comprar para tener una chance del 90% de completar el álbum.
proba_90_percent = 0.9
# proba_90_percent = len(total_paquetes_90_percent)/N
# Siendo N = 1000, deberia comprar 900 paquetes para tener una chance del 90% de completar el álbum.

#Ejercicio: Repetí suponiendo que no hay figuritas repetidas en un paquete. ¿Cuánto cambian las probabilidades?
#Se tuvieron que comprar 935.68 paquetes en promedio para completar el album de 670 figuritas
#La probabilidad de completar el álbum con 850 paquetes o menos es de: 0.32
#Esto se logra cambiando solo la funcion "comprar_paquete" de esta manera.
"""
def comprar_paquete(figus_total, figus_paquete):
    '''Recibe el número total de figuritas/espacios que tiene el álbum (dado por el parámetro figus_total) y devuelve un número entero aleatorio que representa la figurita que nos tocó. '''
    paquete = []
    restart = True
    while restart:
        for i in range (figus_paquete):
            figurita = random.randint(0,figus_total-1)
            paquete.append(figurita)
        if len(paquete) == len(set(paquete)):
            return paquete
        else: 
            restart = True
            paquete = []   
"""
           
#Antes necesitaba 949 - 955 figus para completar el album, y la proba de completarlo con 850 era de 0.307 - 0.298 
#Mientras que con este cambio se necesitan aprox 938 figus y la proba es de 0.34.
#Es logico que aumente.

