# vigilante.py

def vigilar(filename):
    '''
    Abre el archivo filenamw, va al final de este, y espera nuevos datos. 
    Aquellos datos cuyo volumen sean mayores que 1000 salen en pantalla.
    Aclaracion: para que el programa funcione, es necesario que antes este
    ejecutandose indefinidamente el archivo Data/mercadolog.csv.
    '''

    import os
    import time
    
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
    
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        yield line   # Aclaracion: lo que hace el yield es devolver el valor 
                     # de line, como si fuera un return, con la excepcion de
                     # que la funcion no termina, sino que continua el ciclo
                     # while. Mientras continua, constantemente le esta 
                     # pasando al ciclo for de abajo un nuevo valor de line.
                     # Anteriormente cometi el error de colocar el yield 
                     # arriba del if, y en ese caso, como le podia devolver
                     # las line con valor vacio, se producia un error de list 
                     # out of range a la hora de definir el precio y el volumen.
               
        
 
if __name__ == '__main__':
    import informe
    
    camion = informe.leer_camion('C:/ejercicios_python/Data/camion.csv')
    
    for line in vigilar('C:/ejercicios_python/Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if nombre in camion:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')