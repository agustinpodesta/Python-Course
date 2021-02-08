# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 11:29:01 2021

@author: Agustin Podesta
"""

import informe
informe.main(['informe.py', 'Data/camion.csv', 'Data/precios.csv'])

import costo_camion
costo_camion.costo_camion('Data/camion.csv')
#Como la funcion costo_camion no esta dentro de la funcion main(), puede importarse exitosamente, e imprime el return de la funcion que es 47671.15.

costo_camion.main(['costo_camion.py', 'Data/camion.csv'])
#Aca estamos diciendo que el archivo/modulo costo_camion pasa a ser main, por lo que se ejecuta lo que esta dentro de la funcion main() del archivo/modulo costo_camion.