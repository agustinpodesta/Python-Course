# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 11:49:23 2021

@author: Agustin Podesta
"""

import csv
from fileparse import parse_csv
def costo_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones*precio) de un archivo'''
    suma=0
    f = open(nombre_archivo)
    rows=csv.reader(f)
    headers=next(f)
    for row in rows:
        try:
            suma=suma+int(row[1])*float(row[2])
        except ValueError:
            print(f'Para la fruta: {row[0]}, falta un valor')
    return suma
    f.close()

#%%

 
def leer_camion(nombre_archivo):
    # Computa todas las cosas que tiene el camion, la cantidad de cajones y su precio
    
    '''
    camion=[]
    f = open(nombre_archivo)
    rows=csv.reader(f)
    headers=next(f)
    for row in rows:
        try:
            lote={'nombre':row[0],'cajones':int(row[1]),'precio':float(row[2])}
            camion.append(lote)
        except ValueError:
            print(f'Para la fruta: {row[0]}, falta un valor')
    '''
    return parse_csv(nombre_archivo, types = [str, int, float])
    f.close()




#%%


def leer_precios(nombre_archivo):
    # Computa todas las frutas que vende el local y a que precio
    '''
    precios={}
    f=open(nombre_archivo)
    rows=csv.reader(f)
    for row in rows:
        try:
            A conitnuacion se va a agregar un valor a la biblioteca por c/loop 
            precios[row[0]] = float(row[1])  #biblioteca_vacia['clave']=valor

        except IndexError:
            '''
    return dict(parse_csv(nombre_archivo,types = [str,float], has_headers = False))
    f.close()



#%%    

def hacer_informe(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    lista = []
    for cam in camion:
        claves = precios.keys()
        for clave in claves:
            if cam['nombre'] == clave:
                tupla = (clave, cam['cajones'], cam['precio'], precios[clave] - cam['precio'])
                lista.append(tupla)
    return lista

    
#O tambien:

#print('%10s %10s %10s %10s' % ('Nombre', 'Cajones', 'Precio', 'Cambio'))
#print('---------- ---------- ---------- ----------')    
#for nombre, cajones, precio, cambio in informe:
#    print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f}$ {cambio:>10.2f}')

#%%

def balance(nombre_archivo_camion, nombre_archivo_precios):
    cosas_en_camion=leer_camion(nombre_archivo_camion) #a
    precio_posta=leer_precios(nombre_archivo_precios)
    ganancia_bruta=0.0
    for a in cosas_en_camion: #for para analizar las cosas en el camion
            claves=precio_posta.keys()
            for clave in claves: #for para leer todas las claves, que son las frutas del negocio
                if a['nombre'] == clave: #if la fruta del camion coincide con la del negocio
                    ganancia_bruta += precio_posta[clave]*a['cajones']
    return ganancia_bruta



def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    informe = hacer_informe(nombre_archivo_camion, nombre_archivo_precios)
    print('%10s %10s %10s %10s' % ('Nombre', 'Cajones', 'Precio', 'Cambio'))
    print('---------- ---------- ---------- ----------')
    for r in informe:
        print('%10s %10d %10.2f$ %10.2f$' % r)
    #print(f'\nCosto del camion: {costo_camion(nombre_archivo_camion)} $')
    #print(f'Ganancia bruta del negocio: {balance(nombre_archivo_camion, nombre_archivo_precios)} $')
    ganancia_neta = balance(nombre_archivo_camion, nombre_archivo_precios)-costo_camion(nombre_archivo_camion)
    #print(f'Ganancia neta del local: {ganancia_neta:.2f} $')
    return None

informe_camion('Data/camion.csv','Data/precios.csv')
    

    
    

    
