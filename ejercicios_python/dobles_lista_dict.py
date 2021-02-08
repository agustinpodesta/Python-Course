l = [{'a': 123, 'b': 1234},
        {'a': 3222, 'b': 1234},
        {'a': 123, 'b': 1234}]

seen = set() #lo que hace set() es convertirte cualquier cosa en un diccionario y encima eliminar los duplicados
             #Ej. nombres = ['Naranja', 'Manzana', 'Naranja']. set(nombres) = {'Manzana', 'Naranja'} 
new_l = []
for d in l: #veamos diccionario {} por diccionario. El primero es d = {'a': 123, 'b': 1234}
    t = tuple(d.items()) #.items() lo que hace es obtener pares (clave,valor),
                         #por lo que en este caso te queda t = dict_items([('a', 123), ('b', 1234)])
                         #y luego el tuple() lo convierte en tupla. Por lo que t=(('a', 123), ('b', 1234))    
    print(t)
    if t not in seen:
        seen.add(t)
        print(seen) #{(('a', 123), ('b', 1234))}
        new_l.append(d)
        print(new_l) #d sigue siendo {'a': 123, 'b': 1234}, por lo que aca queda [{'a': 123, 'b': 1234}]

print (new_l)


#Todas las salidas:

#1 vuelta
#(('a', 123), ('b', 1234))
#{(('a', 123), ('b', 1234))}
#[{'a': 123, 'b': 1234}]

#2 vuelta
#(('a', 3222), ('b', 1234))
#{(('a', 3222), ('b', 1234)), (('a', 123), ('b', 1234))}
#[{'a': 123, 'b': 1234}, {'a': 3222, 'b': 1234}]

#3 vuelta
#(('a', 123), ('b', 1234))

#Resultado
#[{'a': 123, 'b': 1234}, {'a': 3222, 'b': 1234}]
