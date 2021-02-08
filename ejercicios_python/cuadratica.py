# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:32:14 2021

@author: Agustin Podesta
"""
import numpy as np
def cuadratica(a,b,c):
    x1 = (-b + np.sqrt(b**2 - (4*a*c)))/(2*a)
    x2 = (-b - np.sqrt(b**2 - (4*a*c)))/(2*a)
    return x1,x2

binomial = cuadratica(1,-0.455,2.25*10**-3)
print(binomial)