#Considere si siguiente dataset 

#https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HRAnalyticsJobChangeDataScientists__aug_train.csv

#Cuantas columnas son de tipo object.

#Pregunta

#1.Ninguna de las anteriores 
#2.12
#3.10
#4.14
#5.0

import pandas as pd

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HRAnalyticsJobChangeDataScientists__aug_train.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Obtener los tipos de datos de cada columna
tipos_de_datos = df.dtypes

# Contar las columnas de tipo object
columnas_object = tipos_de_datos[tipos_de_datos == 'object'].count()

print("Número de columnas de tipo object:", columnas_object)

#Respuesta -> 10