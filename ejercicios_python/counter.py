from collections import Counter

palabra='apapa'
contador_de_letras=Counter(palabra)
contador_de_letras
# Counter({'a': 3, 'p': 2})

#-------------------------------------------------------------------------------

camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]


total_cajones = Counter() #El Counter comienza vacio
for nombre, n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones
    #Aca el Counter sigue vacio, osea que total_cajones[nombre] que en este caso
    #seria total_cajones[Pera], sigue siendo 0. Y se le asigna el valor del
    #numero de cajones. Osea en vez de que por c/letra voy a tener la cantidad
    #de veces que esta aparece, voy a tener por c/fruta, la cantidad de cajones
    #que yo le estoy asignando.

total_cajones
