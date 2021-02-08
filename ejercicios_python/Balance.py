import csv
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

#Aca llamo a la funcion, tomando el valor del archivo deseado
costo=costo_camion('Data/camion.csv')
print('Costo del camion:',costo, '$')



import csv
def leer_camion(nombre_archivo):
    '''Computa todas las cosas que tiene el camion, la cantidad de cajones y su precio'''
    camion=[]
    f = open(nombre_archivo)
    rows=csv.reader(f)
    headers=next(f)
    for row in rows:
        try:
            lote={'nombre':row[0],'cajones':int(row[1]),'precio':float(row[2])}
            camion.append(lote)
        except ValueError:
            print(f'Para la fruta: {row[0]}, falta un valor')
    return camion
    f.close()




def leer_precios(nombre_archivo):
    '''Computa todas las frutas que vende el local y a que precio'''
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
cosas_en_camion=leer_camion('Data/camion.csv') #a
precio_posta=leer_precios('Data/precios.csv') 
ganancia_bruta=0.0
valor_camion=costo_camion('Data/camion.csv')
for a in cosas_en_camion: #for para analizar las cosas en el camion
        claves=precio_posta.keys()
        for clave in claves: #for para leer todas las claves = frutas del negocio
            if a['nombre']==clave: #if la fruta del camion coincide con la del negocio
                ganancia_bruta=ganancia_bruta+precio_posta[clave]*a['cajones']
print('Ganancia bruta del negocio:',ganancia_bruta,'$')
ganancia_neta=ganancia_bruta-valor_camion
print('Ganancia neta del local',ganancia_neta,'$')
