import csv
import sys
#sys.argv lo que hace es agarrar los argumentos que escribiste en el Command prompt y te los mete en una lista. Por ejemplo, si yo escribo: python costo_camion.py
#print(sys.argv)=['costo_camion.py'] y en ese caso solo tengo 1 argumento. Si yo escribo python costo_camion.py 1 2 3, print(sys.argv)=['costo_camion.py','1','2','3'] y en este caso
#tengo 4 argumentos. 
def costo_camion(nombre_archivo):
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
#como lo que yo escribo en el cmd es: python camion_commandline.py Data/camion.csv, este tiene 2 argumentos, que son las dos ultimas palabras 
if len(sys.argv)==2:
    nombre_archivo=sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'
#Aca llamo a la funcion, tomando el valor del archivo deseado
costo=costo_camion(nombre_archivo)
print(f'Costo total: {costo} $')
