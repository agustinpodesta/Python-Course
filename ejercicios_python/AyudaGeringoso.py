cadena=input("ingese una cadena: ")       #que solicite un string como entrada 
largo=len(cadena)                                    #para obtener el largo asi no cometemos errores
inicio=0                                                     #es una variable necesaria para comparar en un bucle   
cadena_final=""                                                      # Le será de utilidad crear en este problema un string vacío ‘’  
caracter=""                                               #valor que tomará dependiendo de que letra sea 
while inicio < largo:                                  #inicia el bucle en 0 y lo compara con el largo, se repetirá mientras sea menor   
    if cadena[inicio] in "aeo":                     #Para acceder a un elemento de un string utilice los corchetes [] donde inicio se irá incrementando
                                                               #además uso in para ver si es a, e ,o  
        caracter="+"                                   # si es caracter vale "+"  
    elif cadena[inicio] in "iu":                    #otra comparación, pero ahora con los valores pedidos i u
        caracter="-"                                   #por supuesto si es igual ahora caracter vale "-"    
    else:                                                  #sino 
        caracter=cadena[inicio]                 #sigue cada letra igual  
    cadena_final+= caracter                                 # Recuerde que el operador + etc, bien a la cadena vacia le agrego el valor que tiene caracter
    inicio+=1                                            #debo incrementar el valor inicial de inicio para que llegue a ser igual que el largo de la caden
 
print(cadena)                                        #optativo, la cadena original
print(cadena_final)                                             #resultado que finalmente se va a imprimir.(lo pedido, así que es obligatorio)
input()
