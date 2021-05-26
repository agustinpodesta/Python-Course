#informe.py

import csv
from fileparse import parse_csv
import formato_tabla
from lote import Lote
from camion import Camion
#%%

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
    ''' 
    Computa todas las cosas que tiene el camion, la cantidad de cajones
    y su precio
    
    Pos: Devuelve una lista de instancias de la clase Lote, del modulo lote.py
    '''
    
    with open(nombre_archivo) as rows: #Esto hay que hacerlo porque ahora estamos usando un 
                                       #parse_csv que no posee el with open() adentro. Por 
                                       #lo que hay que agregarlo c/vez que lo queramos usar.                            
        camion_dicts = parse_csv(rows, types = [str, int, float])
        camion_lote = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return Camion(camion_lote)

#%%

def leer_precios(nombre_archivo):
    ''' Computa todas las frutas que vende el local y a que precio'''
    with open(nombre_archivo) as rows:
        return dict(parse_csv(rows,types = [str,float], has_headers = False))

#%%    

def hacer_informe(camion, precios):
    ''' 
    Crea una lista de tuplas dada una lista de lotes en un camión
    y un diccionario de precios nuevos.
    '''
    lista = []
    for cam in camion:
        claves = precios.keys()
        for clave in claves:
            if cam.nombre == clave:
                tupla = (clave, cam.cajones, cam.precio, precios[clave] - cam.precio)
                lista.append(tupla)
    return lista

#%%

def balance(nombre_archivo_camion, nombre_archivo_precios):
    ''' 
    Calcula el balance del negocio, es decr, la diferencia entre lo que
    costó el camion y lo que se recaudo con la venta.     
    '''
    cosas_en_camion = leer_camion(nombre_archivo_camion) #a
    precio_posta = leer_precios(nombre_archivo_precios)
    ganancia_bruta = 0.0
    for a in cosas_en_camion: #for para analizar las cosas en el camion
            claves = precio_posta.keys()
            for clave in claves: #for para leer todas las claves, que son las frutas del negocio
                if a.nombre == clave: #if la fruta del camion coincide con la del negocio
                    ganancia_bruta += precio_posta[clave]*a.cajones
    return ganancia_bruta

#%%

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla a partir una lista de tuplas con (nombre, cajones, precio, cambio) 
    '''
    formateador.encabezado(['Nombre', 'Cajones', 'Precio', 'Cambio'])
    #headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    #print('%10s %10s %10s %10s' % headers)
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)
    #for r in data_informe:
        #print('%10s %10d %10.2f$ %10.2f$' % r)
    return None

#%%

def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):        
    '''
    Crea un informe a partir de un archivo que posee la carga de un camión
    y otro que posee los precios de venta. El formato predeterminado de
    salida es txt.
    Alternativas: csv o html.
    '''
    # Lee los archivos con datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea el informe con los datos de camion y precios
    data_informe = hacer_informe(camion, precios)
        
    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)


#%%

def main(argumentos):
    if len(argumentos) not in {3,4}:
        raise IndexError('Es necesario especificar: archivo_camion, archivo_precios, fmt(opcional)')
    nombre_archivo_camion = argumentos[1]
    nombre_archivo_precios = argumentos[2]
    fmt = 'txt' #El formato predeterminado de salida es txt.
    if len(argumentos) == 4:
        fmt = argumentos[3]
    return informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt)

#%%
    
if __name__ == '__main__':
    import sys
    main(sys.argv)

