from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns

iris_dataset = load_iris()
# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
iris_dataframe['target'] = iris_dataset['target']
sns.pairplot(data = iris_dataframe, hue = 'target', diag_kind="hist", palette="viridis")