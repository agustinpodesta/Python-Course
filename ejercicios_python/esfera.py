import math
pi=math.pi
#ojo que aca cuando uno pone un numero en el input,
#te lo carga como un caracter o string, asi que hay que pasarlo a float
radio=float(input('ingrese el radio de la esfera:'))
volumen=(4/3)*pi*radio**3
print('su volumen es:',volumen)

