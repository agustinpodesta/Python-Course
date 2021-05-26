from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split


iris_dataset = load_iris()
# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)

def arboles_decision():
    '''
    1) Separar los datos en dos conjuntos: train y test.
    2) Definir un clasificador clf y entrenarlo con los datos de training.
    3) Evaluar el clasificador con los datos de testing.
    '''
    
    X_train, X_test, y_train, y_test = train_test_split(
        iris_dataset['data'], iris_dataset['target'])
    
    #Creamos una instancia de la clase DecisionTreeClassifier
    from sklearn.tree import DecisionTreeClassifier
    clf = DecisionTreeClassifier()
    
    #Y la entrenamos con los datos de entrenamiento
    clf.fit(X_train, y_train)
    
    return clf.score(X_test, y_test)

#%%

def vecinos_decision():
    '''
    1) Separar los datos en dos conjuntos: train y test.
    2) Definir un clasificador knn y entrenarlo con los datos de training.
    3) Evaluar el clasificador con los datos de testing.
    '''
    
    X_train, X_test, y_train, y_test = train_test_split(
        iris_dataset['data'], iris_dataset['target'])
    
    #Creamos una instancia de la clase KNeighborsClassifier
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors = 1) 
    
    #Y la entrenamos con los datos de entrenamiento
    knn.fit(X_train, y_train)
    
    return knn.score(X_test, y_test)

#%%

def forest_decision():
    '''
    1) Separar los datos en dos conjuntos: train y test.
    2) Definir un clasificador rff y entrenarlo con los datos de training.
    3) Evaluar el clasificador con los datos de testing.
    '''
    
    X_train, X_test, y_train, y_test = train_test_split(
        iris_dataset['data'], iris_dataset['target'])
    
    #Creamos una instancia de la clase RandomForestClassifier
    from sklearn.ensemble import RandomForestClassifier
    rff = RandomForestClassifier() 
    
    #Y la entrenamos con los datos de entrenamiento
    rff.fit(X_train, y_train)
    
    return rff.score(X_test, y_test)



#%%


N = 100

resultado_arboles = sum([arboles_decision() for i in range(N)])
promedio_arboles = resultado_arboles / N

resultado_vecinos = sum([vecinos_decision() for i in range (N)])
promedio_vecinos = resultado_vecinos / N

resultado_forest = sum([forest_decision() for i in range (N)])
promedio_forest = resultado_forest / N

print("Test set score arboles: {:.2f}".format(promedio_arboles))
print("Test set score vecinos: {:.2f}".format(promedio_vecinos))
print("Test set score forest: {:.2f}".format(promedio_forest))

#Vemos que generalmente utilizando el clasificador del vecino mas cercano da un score mayor.

