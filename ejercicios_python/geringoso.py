cadena=input("ingese una cadena: ")     
largo=len(cadena)                                   
inicio=0                                                    
cadena_final=""                                                      
caracter=""                                               
while inicio < largo:                                 
    if cadena[inicio] in "a":                                                                    
        caracter="apa"                                 
    elif cadena[inicio] in "e":                  
        caracter="epe"
    elif cadena[inicio] in "i":                  
        caracter="ipi"
    elif cadena[inicio] in "o":
        caracter="opo"
    elif cadena[inicio] in "u":
        caracter="upu"
    else:                                                  
        caracter=cadena[inicio]                 
    cadena_final+= caracter                                 
    inicio+=1                                       
 
print(cadena)                                     
print(cadena_final)                                          
input()
