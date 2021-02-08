import csv
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

#Aca llamo a la funcion, tomando el valor del archivo deseado
leer=leer_precios('Data/precios.csv')
print(leer)
