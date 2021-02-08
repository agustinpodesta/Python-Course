frase = 'Los hermanos sean unidos porque ésa es la ley primera'
palabras = frase.split()
palabrerio=''
unir=[] #Esto se pone asi y no con '' porque el .append solo se puede aplicar a listas, es decir [], ya que '' es un string.
for i in palabras:
    if i[-2:]=='os':
        palabrerio=i[0:len(i)-2]+'es'
    else:
        palabrerio=i
    unir.append(palabrerio)
    total=' '.join(unir)

print(total)
