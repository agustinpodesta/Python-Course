geringoso = " "

palabra = input('Ingrese una palabra: ')

for c in palabra:
    geringoso = geringoso + c
    if c == 'a':
        geringoso = geringoso + 'pa'
    if c == 'e':
        geringoso = geringoso + 'pe'
    if c == 'i':
        geringoso = geringoso + 'pi'
    if c == 'o':
        geringoso = geringoso + 'po'
    if c == 'u':
        geringoso = geringoso + 'pu'
    
print('La palabra \"{}\" en geringoso es:{}'. format(palabra, geringoso))
