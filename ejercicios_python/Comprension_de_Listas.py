# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:31:32 2020

@author: Agustin Podesta
"""
import csv
def leer_camion(nombre_archivo):
    camion=[]
    f = open(nombre_archivo)
    rows=csv.reader(f)
    headers=next(rows)
    for n_row,row in enumerate(rows,start=1):
        record=dict(zip(headers,row)) #Esto es para combinar el encabezado del archivo con los datos de cada fila.
        try: #Aca lo que hago es asignarle las claves a cada valor
            lote={'nombre':record['nombre'],'cajones':int(record['cajones']),'precio':float(record['precio'])}            
            camion.append(lote) #por cada fila que recorra, se la agrega a la lista 'camion'
        except ValueError:
            print(f'Para la fruta: {row[0]}, falta un valor')
    return camion
    f.close()

#Aca uso el record aunque no hace falta, podria no usarlo y en registro iria: registro={'nombre':fila[0],'cajones':int(fila[1]),'precio':float(fila[2])}. En realidad el record nos salva
#para cuando necesito que mi funcion siga funcionando a pesar de que le pasaste un archivo con un formato de columnas completamente diferente al de antes, que no es el caso.   

def leer_precios(nombre_archivo):    
    precios={}
    f=open(nombre_archivo)
    rows=csv.reader(f)
    for row in rows:
        try:
            #A conitnuacion se va a agregar un valor a la biblioteca por c/loop 
            precios[row[0]]=float(row[1])  #biblioteca_vacia['clave']=valor
        except IndexError:
            return precios
    f.close()
    
# Ejercicio 3.10
nums = [1,2,3,4]
cuadrados = [x*x for x in nums]
cuadrados
dobles = [2*x for x in nums if x>2]
dobles 

# Ejercicio 3.11
camion=leer_camion('C:\ejercicios_python\Data/fecha_camion.csv')
costo=sum(x['cajones']*x['precio'] for x in camion)
costo

precios = leer_precios('C:\ejercicios_python\Data/precios.csv')
valor = sum([ s['cajones'] * precios[s['nombre']] for s in camion ])
valor
#s['nombre'] for s in camion: 'Lima', 'Naranja', 'Caqui', etc.  
#precios[s['nombre']]: precios['Lima']=40.22 , precios['Naranja']= 106.28 , etc. 

#Ejercicio 3.12
mas100 = [s for s in camion if s['cajones'] > 100]
mas100

myn = [s for s in camion if s['nombre'] in {'Mandarina','Naranja'}]
myn

costo10k = [s for s in camion if s['precio'] * s['cajones'] > 10000]
costo10k

#Ejercicio 3.13
nombre_cajones = [tuple(s.values())[0:2] for s in camion]
nombre_cajones 
# o se puede hacer (Mas conveniente):
nombre1_cajones=[(s['nombre'] , s['cajones']) for s in camion]
nombre1_cajones

nombres={s['nombre'] for s in camion}
nombre #Valores unicos!

stock = {nombre: 0 for nombre in nombres}
stock

#Crear un diccionario
for s in camion:
    stock[s['nombre']] +=s['cajones']
stock

camion_precios={nombre:precios[nombre] for nombre in nombres}
camion_precios
#Esto significa que: en el primer loop, a nombre=Lima le agregue un ':precios[Lima]' que es igual a 40.22 para Lima.

f= open('C:\ejercicios_python\Data/fecha_camion.csv')
rows = csv.reader(f)
headers=next(rows)
select=['nombre', 'cajones', 'precio']
indices= [headers.index(s) for s in select]
row = next(rows)
record = {ncolumna:row[index] for ncolumna, index in zip(select, indices)}
record
#ncolumna='nombre' , row[index=0]='Lima'

camion=[{ncolumna:row[index] for ncolumna, index in zip(select, indices)} for row in rows]
camion


