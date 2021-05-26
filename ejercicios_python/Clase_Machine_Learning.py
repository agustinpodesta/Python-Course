from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris_dataset = load_iris()
# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
# y hacemos una matriz de gráficos de dispersión, asignando colores según la especie
pd.plotting.scatter_matrix(iris_dataframe, c = iris_dataset['target'], figsize = (15, 15), marker = 'o', hist_kwds = {'bins': 20}, s = 60, alpha = 0.8)

#En este caso usaremos el 75% de los datos para entrenar y el 25% restante para evaluar. Osea 
#que los primeros dos valores que devuelve train_test_split son el 75% y el 25% respectivamente,
#de los datos del primer argumento dentro de la funcion. Mientras que con el segundo
#argumento pasa lo mismo, primero devuelve el 75% y luego el 25%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state = 0)

#Creamos una instancia de la clase KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)

#Y la entrenamos con los datos de entrenamiento
knn.fit(X_train, y_train)

#Ahora lo podemos usar para predecir la clase de una nueva flor a partir de sus cuatro medidas:
X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new.shape:", X_new.shape)

#Grafiquemos este nuevo punto en rojo y veamos su relación con los datos de entrenamiento en dos de los atributos.
plt.scatter(X_train[:, 1], X_train[:, 3], c = y_train)
plt.scatter(X_new[:, 1], X_new[:, 3], c = 'red')

#Acá se ve que el punto rojo esta cerca de la clase "setosa". 
#Utilicemos ahora el algoritmo knn entrenado para clasificar el punto X_new
prediction = knn.predict(X_new)
print("Predicción:", prediction)
print("Nombre de la Especie Predicha:", iris_dataset['target_names'][prediction])

#Finalmente, usemos el 25% de los datos etiquetados que nos guardamos para evaluar
#cuán bien funciona nuestro clasificador.
y_pred = knn.predict(X_test)
print("Predicciones para el conjunto de Test:\n", y_pred)
print("Etiquetas originales de este conjunto:\n", y_test)

#Se ve que coinciden todos salvo el último. Podemos medir el éxito calculando la fracción
#de clasificaciones bien hechas (calculamos el promedio de "1 si está bien, 0 si está mal")
print(y_pred == y_test)
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))

#O, directamente, usando el método score que ya viene en el clasificador, donde en el primer
#argumento pones lo que queres evaluar, y en el segundo con que valores queres compararlos:
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))

