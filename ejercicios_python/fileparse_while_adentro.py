# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 18:20:35 2021

@author: Agustin Podesta
"""

import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV o cualquier iterable en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el
    parámetro select, que debe ser una lista de nombres de las columnas a
    considerar. 
    Para el caso de un archivo sin header, hay que poner has_headers = False y especificar type.
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        if has_headers:
            # Lee los encabezados
            headers = next(rows)
            if select != None:  
                headers = select
            registros = []
            for n_row, row in enumerate(rows):
                if not row: #Saltea filas sin datos
                    continue
                if types != None:
                   try: 
                       row = [func(val) for func,val in zip(types,row)]
                       registro = dict(zip(headers, row))
                       registros.append(registro)
                   except ValueError as e:
                       if silence_errors == False:
                           print(f'Row {n_row+1}: No pude convertir {row}')
                           print(f'Row {n_row+1}: Motivo: {e}')    
                
        elif has_headers == False and select:
            raise RuntimeError('Para seleccionar, necesito encabezados')
        else:
            if select != None:  
                headers = select
            registros = []
            for row in rows:
                if not row: #Saltea filas sin datos
                    continue
                if types != None:
                   row = tuple([func(val) for func,val in zip(types,row)])
                   registros.append(row)

        return registros
        
def imprimir_parse_csv(nombre_archivo_camion, nombre_archivo_precios):    
    camion = parse_csv(nombre_archivo_camion, types=[str, int, float])
    cajones_lote = parse_csv(nombre_archivo_camion, select=['nombre', 'cajones'], types=[str, int])
    precios = parse_csv(nombre_archivo_precios, types=[str,float], has_headers=False)
    return camion, cajones_lote, precios

camion, cajones_lote, precios = imprimir_parse_csv('Data/camion.csv', 'Data/precios.csv')
print(f'{camion} \n\n{cajones_lote} \n\n{precios}')
    
camion = parse_csv('Data/missing.csv', types = [str, int, float], silence_errors = True)
camion
