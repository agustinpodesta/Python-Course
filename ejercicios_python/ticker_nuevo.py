# ticker.py
    
from vigilante import vigilar
import csv
import formato_tabla

#%%

def filtrar_datos(filas, nombres):
    '''
    Aclaracion: es importante antes conocer el
    indice de la palabra que se quiere filtrar
    '''
    for fila in filas:
        if fila[0] in nombres:
            yield fila

#%%

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

#%%

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

#%%

# La funcion hace_dicts fue sacada ya que para que formato_tabla funcione,
# los datos que uno le pasa tienen que estar en formato lista, no dict. Es
# Por eso que tambien tuve que cambiar la funcion filtrar_datos para que 
# funcione para una lista en lugar de un diccionario, aunque quede mas feo. 

#def hace_dicts(rows, headers):
    #for row in rows:
        #yield dict(zip(headers, row))

#%%

def parsear_datos(lines):
    rows = csv.reader(lines)
    #rows = elegir_columnas(rows, [0, 1, 2])
    rows = ((row[index] for index in [0, 1, 2]) for row in rows)
    # La siguiente seria el reemplazo de la funcion cambiar_tipo, pero
    # nose porque estaria mal; sigue el mismo patron que la anterior.
    rows = ((func(val) for func, val in zip([str, float, float], row)) for row in rows)
    rows = cambiar_tipo(rows, [str, float, float])
    return rows

#%%

def ticker(camion_file, log_file, fmt):
    import informe
    camion = informe.leer_camion(camion_file)
    lines = vigilar(log_file) #Vigilar es el productor
    
    rows = parsear_datos(lines) #La salida de la función vigilar() fué usada
                                #como entrada a la función csv.reader() (que
                                #habíamos usado para leer un archivo del
                                #disco) y el resultado es una secuencia de
                                #filas "parseadas", separadas por las comas.
    
    rows = (row for row in rows if row[0] in camion)  #Filtro los datos a aquellos que estan
                                                      #en el archivo camion.csv.                              
    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for nombre, precio, volumen in rows:
        rowdata = [ nombre, f'{precio:0.2f}', f'{volumen:0.2f}' ]
        formateador.fila(rowdata)

