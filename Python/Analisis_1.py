import pandas as pd

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/Car%20details%20v3.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Obtener los tipos de datos de cada columna
tipos_de_datos = df.dtypes

# Contar las columnas de tipo object
columnas_object = tipos_de_datos[tipos_de_datos == 'object'].count()

print("Número de columnas de tipo object:", columnas_object)