import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np

x = np.array([55.0, 38, 68, 70, 53, 46, 11, 16, 20, 4]) # mismos datos x, y
y = np.array([153.0, 98, 214, 220, 167, 145, 41, 63, 65, 25])
datosxy = pd.DataFrame({'x': x, 'y': y}) # paso los datos a un dataframe

ajus = linear_model.LinearRegression() # llamo al modelo de regresión lineal
ajus.fit(datosxy[['x']], datosxy[['y']]) # ajusto el modelo

grilla_x = np.linspace(start = 0, stop = 70, num = 1000)
grilla_y = ajus.predict(grilla_x.reshape(-1,1)) #El metodo predict de sklearn en este caso, 
                                                #pide que sea un vector de (-1,1)

#Dato: si una matriz es de:
'''
 [[0 1]
 [2 3]
 [4 5]]
 '''
#el reshape (a,b) ordena a la matriz en a filas y b columnas. Para el caso de (-1,1) lo que 
#hace es convertirla en una matriz de columna unica y de la cantidad de filas que requiera la
#matriz:
'''
[[0]
 [1]
 [2]
 [3]
 [4]
 [5]]
'''
#No entiendo muy bien que hace el signo menos, pero si pones (-89,1) da lo mismo.

datosxy.plot.scatter('x','y')
plt.title('ajuste lineal usando sklearn')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()



superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
antigüedad = [50.0, 5.0, 25.0, 70.0]

data_deptos = pd.DataFrame({'alquiler': alquiler, 'superficie': superficie, 'antigüedad': antigüedad})

#Concateno/uno las dos columnas a lo largo del eje x, osea de las filas:
X = pd.concat([data_deptos.superficie,data_deptos.antigüedad], axis = 1)

ajuste_deptos = linear_model.LinearRegression()
ajuste_deptos.fit(X,data_deptos.alquiler)

errores = data_deptos.alquiler - (ajuste_deptos.predict(X))
print(errores)
print("ECM:", (errores**2).mean()) # error cuadrático medio
