#Ejercicio 2.22
import csv
def leer_parque(nombre_archivo, parque):
    lista=[]
    f=open(nombre_archivo, encoding="utf-8")
    rows=csv.reader(f)
    headers=next(rows)
    for n_row,row in enumerate(rows,start=1):
        record=dict(zip(headers,row)) #Esto es para combinar el encabezado del archivo con los datos de cada fila.
        if record['espacio_ve']==parque: #Si es que la columna de espacio_ve coincide con el parque que yo le señalé, que entre al bucle
            try: #Aca lo que hago es asignarle las claves a cada valor
                arboles={'long':float(record['long']),'lat':float(record['lat'])
                      ,'id_arbol':int(record['id_arbol']),'altura_tot':int(record['altura_tot']),
                      'diametro':int(record['diametro']), 'inclinacio':int(record['inclinacio']),
                      'id_especie':int(record['id_especie']),'nombre_com':record['nombre_com'],
                      'nombre_cie':record['nombre_cie'],'tipo_folla':record['tipo_folla'],
                      'espacio_ve':record['espacio_ve'],'ubicacion':record['ubicacion'],
                      'nombre_fam':record['nombre_fam'],'nombre_gen':record['nombre_gen'],
                      'origen':record['origen'],'coord_x':float(record['coord_x']),
                      'coord_y':float(record['coord_y'])
                        }            
                lista.append(arboles) #por cada fila que recorra, se la agrega a la lista
            except ValueError:
                print(f'Parael arbol: {row[7]}, falta un valor')
        else:
            continue
    return lista
    f.close()

#Aca llamo a la funcion, tomando el valor del archivo deseado
arboleda=leer_parque('Data/arbolado_en_espacios_verdes.csv','ANDES, LOS')
print('Lectura:', arboleda,'\n')




#Ejercicio 2.23. Funcion que que toma la lista anterior de árboles y devuelve el conjunto de especies que figuran en la lista.
def especies(lista_arboles):
    conjuntos=[]
    for n_row,row in enumerate (lista_arboles,start=1):
        try:
            conjunto={'Especie':row['nombre_com']}
            conjuntos.append(conjunto)
        except ValueError:
                print(f'Parael arbol: {row[7]}, falta un valor')
    return conjuntos
    f.close()

conjunto_de_especies=especies(arboleda)
seen= set()
new_l = []
for d in conjunto_de_especies:
      t = tuple(d.items())
      if t not in seen:
          seen.add(t)
          new_l.append(d)  

print('Conjunto de especies:\n',new_l)
            



#Ejercicio 2.24. Funcion que dada una lista, devuelve un diccionario en el que las especies son las claves que tienen como valores asociados la cantidad de ejemplares en esa especie en la lista dada.
def contar_ejemplares(lista_arboles):
    from collections import Counter
    total_arboles= Counter()
    conjuntos=[]
    for n_row,row in enumerate (lista_arboles,start=1):
        try:
            total_arboles[row['nombre_com']] += 1
            conjunto={row['nombre_com']:total_arboles[row['nombre_com']]}
            conjuntos.append(conjunto)
        except ValueError:
                print(f'Parael arbol: {row[7]}, falta un valor')
    print('\n Top 5:',total_arboles.most_common(5),'\n')
    return conjuntos
    f.close()

contador_ejemplares= contar_ejemplares(arboleda)
print('Arboles contados:',contador_ejemplares)



#Ejercicio 2.25. Funcion que dada una lista de árboles como la anterior y una especie de árbol, devuelve una lista con las alturas de los ejemplares de esa especie en la lista. 
def obtener_alturas(lista_arboles, especie):
    conjuntos=[]
    maximo=0.0
    suma=0.0
    n_suma=0
    for n_row,row in enumerate (lista_arboles,start=1):
        if row['nombre_com']== especie: #Si es que la columna de 'nombre_com' coincide con la especie que yo le señalé, que entre al bucle
            try:
                conjunto={'Altura':row['altura_tot']}
                conjuntos.append(conjunto)
                altura=row['altura_tot']
                while altura > maximo:
                    maximo=altura
                suma=suma+row['altura_tot']
                n_suma=n_suma+1
            except ValueError:
                print(f'Parael arbol: {row[7]}, falta un valor')
        else:
            continue
    print('\n El maximo es:',maximo)
    promedio=suma/n_suma
    print('\n El promedio es:',round(promedio,2))
    return conjuntos
    f.close()

especie='Jacarandá'
alturas_arboles=obtener_alturas(arboleda,especie)
print(f'\n Altura de los arboles de la especie {especie}: {alturas_arboles}')



#Ejercicio 2.26. Funcion que dada una lista de árboles como la anterior y una especie de árbol, devuelve una lista con las inclinaciones de los ejemplares de esa especie.
def obtener_inclinaciones(lista_arboles, especie):
    conjuntos=[]
    for n_row,row in enumerate (lista_arboles,start=1):
        if row['nombre_com']== especie: #Si es que la columna de 'nombre_com' coincide con la especie que yo le señalé, que entre al bucle
            try:
                 conjunto={'Inclinacion':row['inclinacio']}
                 conjuntos.append(conjunto)
            except ValueError:
                print(f'Parael arbol: {row[7]}, falta un valor')
        else:
            continue
    return conjuntos
    f.close()

especie='Jacarandá'
angulos=obtener_inclinaciones(arboleda,especie)
print(f'\n Inclinacion de los arboles de la especie {especie}: {angulos}')



#Ejercicio 2.27. Funcion que combina las funciones especies() y obtener_inclinaciones() y dada una lista de árboles devuelva la especie que tiene el ejemplar más inclinado y su inclinación.
def especimen_mas_inclinado(lista_arboles):
    angulo_max=0
    conjunto_de_especies=especies(arboleda)
    for n_row,row in enumerate (conjunto_de_especies,start=1):
        especie=row['Especie']
        angulos=obtener_inclinaciones(arboleda, especie)
        for n_fila,fila in enumerate (angulos,start=1):
            angulo=fila['Inclinacion']
            if angulo > angulo_max:
                angulo_max=angulo
                especie_alfa=especie
    print(f'\n El arbol mas inclinado pertenece a la especie {especie_alfa}')
    return angulo_max
    f.close()

el_mas_inclinado=especimen_mas_inclinado(arboleda)
print('\n Este posee una inclinacion de', el_mas_inclinado,'grados')


#Ejercicio 2.28. Funcion que combina las funciones anteriores y dada una lista de árboles devuelva la especie que en promedio tiene el ejemplar más inclinado y su promedio calculado.
"""
def especie_promedio_mas_inclinada(lista_arboles):
    from collections import Counter
    promedio_max=0.0
    suma_counter=Counter()
    contador=Counter()
    conjunto_de_especies=especies(arboleda)
    suma=0.0
    n_suma=0
    for n_row,row in enumerate (conjunto_de_especies,start=1):  #Aca entra a especies()
        especie=row['Especie']
        angulos=obtener_inclinaciones(arboleda, especie)
        for n_fila,fila in enumerate (angulos,start=1): #Aca entra a obtener_inclinaciones() dentro de una especie (aquella que tome row['Especie'])
            angulo=fila['Inclinacion']
            suma += angulo
            n_suma=n_suma+1
        suma_counter[angulo] += suma
        print(suma[row])
        contador[row['Especie']] +=list((dict()).items())        #promedio= Counter({'Lapacho': 1.4166666666666667})
        promedio_dict=list((dict(contador)).items())   # [('Lapacho', 1.4166666666666667)]                                         
        if promedio_dict[0][1] > promedio_max:         #promedio_dict[0]=('Lapacho', 1.4166666666666667)   promedio_dict[0][1]=1.4166666666666667   
            promedio_max=promedio_dict[0][1]
            especie_alfa=especie
      
        
           
    print(f'\n El arbol mas inclinado en promedio pertenece a la especie {especie_alfa}')
    return promedio_max
    f.close()

el_mas_inclinado_prom=especie_promedio_mas_inclinada(arboleda)
print('\n Este posee un promedio de inclinacion de', round(el_mas_inclinado_prom),'grados')    

"""

#3.6 Arbolado porteño y comprensión de listas

#Ejercicio 3.18. Lectura de todos los árboles
def leer_arboles(nombre_archivo):
    ''' Funcion que lee el archivo indicado y devuelve una lista de diccionarios
        con la información de todos los árboles en el archivo. '''
    f=open(nombre_archivo, encoding="utf-8")
    rows=csv.reader(f)
    headers=next(rows)
    headers
    row = next(rows)
    types = [float, float, int, float, float, int, int, str, str, str, str, str, str, str, str, float, float]   
    indices = [headers.index(ncolumna) for ncolumna in headers]
    record = [{ncolumna: func(row[index]) for ncolumna, func, index in zip(headers,types, indices)} for row in rows] #Aca si estuvieramos usando lo de converted func(row[index]) = func(val)
    return record

arboleda = leer_arboles('C:\ejercicios_python/Data/arbolado_en_espacios_verdes.csv')
arboleda

#Ejercicio 3.19. Lista de altos de Jacarandá
H = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] in {'Jacarandá'}]

#Ejercicio 3.20. Lista de altos y diámetros de Jacarandá
H_diam = [(arbol['altura_tot'],arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] in {'Jacarandá'}]
H_diam[0]
H_diam[1]
len(H_diam)
H_diam[3254]
print(H_diam)
#Ejercicio 3.21. Diccionario con medidas
def medidas_de_especies(species,file):
    H_diam_general = {especie:[(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] in especie] for especie in especies}
    # H_diam_general = [{arbol['nombre_com']:(arbol['altura_tot'], arbol['diametro'])} for arbol in arboleda if arbol['nombre_com'] in especies]
    return H_diam_general

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']    
diccionario = medidas_de_especies(especies,arboleda)
print(len(diccionario))
print(diccionario['Palo borracho rosado'][9])
10517-3255-4112
#%% GRAFICOS

# Ejercicio 4.29: Histograma de altos de Jacarandás
def histograma(nombre_archivo):
    import os
    import matplotlib.pyplot as plt
    os.path.join(nombre_archivo) #Esto se usa a la hora de emplear archivos, los cuales no se encuentran en el codigo.
    arboleda = leer_arboles(nombre_archivo)
    altos = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] in {'Jacarandá'}]
    grafico = plt.hist(altos, bins = 25)
    return grafico

a_ver_que_sale1 = histograma('C:\ejercicios_python/Data/arbolado_en_espacios_verdes.csv')


#Ejercicio 4.30: Scatterplot (diámetro vs alto) de Jacarandás
#H = alturas de los Jacarandas.
#D = diametros de los Jacarandas
D = [arbol['diametro'] for arbol in arboleda if arbol['nombre_com'] in {'Jacarandá'}]
import matplotlib.pyplot as plt
plt.scatter(D,H)

#Otra forma
import numpy as np
vector = np.array(H_diam)
vector_H = vector[0:len(vector), 0]
vector_D = vector[0:len(vector),1]
plt.scatter(vector_D,vector_H, c= vector_D, cmap='Spectral', alpha=0.9)

plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")

#Ejercicio 4.31: Scatterplot para diferentes especies
import os
import matplotlib.pyplot as plt
import numpy as np

os.path.join('Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles('C:\ejercicios_python/Data/arbolado_en_espacios_verdes.csv')
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)

medidas_Euc = np.array(medidas['Eucalipto'])
medidas_Euc_X = medidas_Euc[0:len(medidas_Euc),1] 
medidas_Euc_Y = medidas_Euc[0:len(medidas_Euc),0]
plt.scatter(medidas_Euc_X,medidas_Euc_Y, c= 'green', alpha=0.9, edgecolor='black',linewidth=1)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Eucaliptos")
# plt.xlim(0,20) 
# plt.ylim(0,20) 

medidas_Palo = np.array(medidas['Palo borracho rosado'])
medidas_Palo_X = medidas_Palo[0:len(medidas_Palo),1]
medidas_Palo_Y = medidas_Palo[0:len(medidas_Palo),0]
plt.scatter(medidas_Palo_X,medidas_Palo_Y, c= 'cyan', alpha=0.9, edgecolor='black',linewidth=1)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Palo borracho rosado")

medidas_Jaca = np.array(medidas['Jacarandá'])
medidas_Jaca_X = medidas_Jaca[0:len(medidas_Jaca),1]
medidas_Jaca_Y = medidas_Jaca[0:len(medidas_Jaca),0]
plt.scatter(medidas_Jaca_X,medidas_Jaca_Y, c= 'magenta', alpha=0.9, edgecolor='black',linewidth=1)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandá")

#Si quiero graficar muchos en un mismo grafico, lo unico que tengo que hacer es correrlos al mismo tiempo. 



