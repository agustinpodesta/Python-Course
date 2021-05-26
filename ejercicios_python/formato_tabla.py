# formato_tabla.py

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.         
        '''
        raise NotImplementedError()
        
    def fila(self, rowdata):
        ''' 
        Crea una unica fila de datos de la tabla.
        '''
        raise NotImplementedError()
        
#%%
        
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT.
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end = '')
        print()
        print(('-'*10 + ' ')*len(headers))
    
    def fila(self, row_data):
        for d in row_data:
            print(f'{d:>10s}', end = '')
        print()

#%%

class FormatoTablaCSV(FormatoTabla):
    '''
    Genera una tabla en formato CSV.
    '''
    def encabezado(self, headers):
        print(','.join(headers))
        
    def fila(self, row_data):
        print(','.join(row_data))
        
#%%

class FormatoTablaHTML(FormatoTabla):
    '''
    Genera una tabla en formato HTML.
    '''
    def encabezado(self, headers):
        print('<tr><th>', end = '')
        for h in headers:
            if headers[-1] != h:
                print(''.join([ h + '</th><th>']), end = '') 
            else:
                print(''.join([ h + '</th></tr>']))
            
    def fila(self, row_data):
      print('<tr><td>', end = '')
      for h in row_data:
        if row_data[-1] != h:
            print(''.join([ h + '</td><td>']), end = '') 
        else:
            print(''.join([ h + '</td></tr>']))

#%%

def crear_formateador(nombre):
    '''
    Permite crear un objeto formateador dado un tipo
    de salida (txt, csv, o html).
    '''
    if nombre == 'txt':
        formateador = FormatoTablaTXT()
    elif nombre == 'csv':
        formateador = FormatoTablaCSV()
    elif nombre == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {nombre}')
    return formateador

#%%

def imprimir_tabla(data_archivo, columnas, formateador):
    '''
    Imprime una tabla, a partir de una lista de atributos 
    especificados por el usuario (puede elegir entre 'nombre',
    'cajones', y 'precio'). El formato predeterminado de
    salida es txt.
    Alternativas: csv o html.
    '''
    formateador.encabezado(columnas)
    for i in data_archivo:
        rowdata = [getattr(i, colname) for colname in columnas]
        for n_s,s in enumerate(rowdata): #Hay que pasar todo a string
            if type(s) == int:
                rowdata[n_s] = str(rowdata[n_s])
            elif type(s) == float:
                rowdata[n_s] = f'{rowdata[n_s]:0.2f}'
        formateador.fila(rowdata)
        




   
