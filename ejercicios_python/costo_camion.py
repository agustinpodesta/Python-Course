import csv
import informe_funciones as informe

def costo_camion(nombre_archivo):
    # Computa el precio total del camion (cajones*precio) de un archivo
    suma=0
    '''
    f = open(nombre_archivo)
    rows=csv.reader(f)
    headers=next(rows)
    '''
    for n_row,row in enumerate(informe.leer_camion(nombre_archivo)):
        '''
        record=dict(zip(headers,row))
        print(record)
        '''
        try:
            ncajones=int(row['cajones'])
            precio=float(row['precio'])
            suma=suma+ncajones*precio
        # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Row {n_row}: No puede interpretar{row}')
    return suma
    f.close()

def main(lista):
    file_name = lista[0]
    nombre_archivo_camion = lista[1]
    print('\nCosto total:', costo_camion(nombre_archivo_camion), '$')
    return None

if __name__ == '__main__': #'Es este archivo esta siendo corrido directamente por python, o esta siendo importado?'
    main(['costo_camion.py', 'Data/camion.csv'])
