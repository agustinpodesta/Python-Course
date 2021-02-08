# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 15:14:22 2021

@author: Agustin Podesta
"""


def parse_csv(rows, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV o cualquier iterable en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el
    parámetro select, que debe ser una lista de nombres de las columnas a
    considerar. 
    Para el caso de un archivo sin header, hay que poner has_headers = False y especificar type.
    '''
    if has_headers:
        rows = iter(rows) #Lo convierto en iterador para poder usar la funcion next(), ya que esta solo funciona con iteradores.
        headers = next(rows)
        headers = headers.replace(',',' ')
        headers = list(headers.split())
        # Lee los encabezados
        if select != None:  
            headers = select
        registros = []
        for n_row, row in enumerate(rows):
            row =  row.split(',')
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
            row =  row.split(',')
            if len(row) == 1:
                break
            if not row: #Saltea filas sin datos
                continue
            if types != None:
               row = tuple([func(val) for func,val in zip(types,row)])
               registros.append(row)

    return registros



        
def imprimir_parse_csv(nombre_archivo_camion, nombre_archivo_precios):    
    with open(nombre_archivo_camion) as file_camion_1:
        camion = parse_csv(file_camion_1, types=[str, int, float])
    with open(nombre_archivo_camion) as file_camion_2:
        cajones_lote = parse_csv(file_camion_2, select=['nombre','cajones'], types=[str,int])
    with open(nombre_archivo_precios) as file_precios: 
        precios = parse_csv(file_precios,types=[str,float], has_headers=False)
    return camion, cajones_lote, precios

camion, cajones_lote, precios = imprimir_parse_csv('Data/camion.csv', 'Data/precios.csv')
print(f'{camion} \n\n{cajones_lote} \n\n{precios}')
    
lines = ['name,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']    
camion = parse_csv(lines, types=[str,int,float])
camion





