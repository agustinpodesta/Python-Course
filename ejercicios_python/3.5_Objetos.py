# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 10:38:08 2020

@author: Agustin Podesta
"""
#Ejercicio 3.15
types = [str, int, float]

import csv
f = open('C:\ejercicios_python/Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

types[1](row[1]) * types[2](row[2])

r = list(zip(types,row))
r

converted = []
for func,val in r:
    converted.append(func(val))
    
converted

converted[1]*converted[2]

#Lo de antes puede hacerse con comprension de listas de la siguiente manera:
converted = [s[0](s[1]) for s in r]
converted
#O asi:
converted= [func(val) for func, val in r]
converted
#O asi:
converted= [func(val) for func, val in zip(types,row)]
converted

#Ejercicio 3.16
headers
converted
dict(zip(headers,converted))

#Usando comprension de listas:
{clave:valor for clave, valor in zip(headers, converted)}
#O si no tuviera el converted:
{clave:func(val) for clave, func, val in zip(headers,types,row)}

#Ejercicio 3.17
f = open('C:\ejercicios_python/Data/dowstocks.csv')
rows = csv.reader(f)
headers=next(rows)
row = next(rows)
headers
row

types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
converted
record = dict(zip(headers,converted))
record
record['name']

x = '6/11/2007'
y = [s for s in x]
y


#Convertir fecha de '6/11/2007' a una tupla (6, 11, 2007)
x='6/11/2007'
dia = x[0]
mes = x[2:4]
año = x[5:]

