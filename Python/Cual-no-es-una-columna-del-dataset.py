#Considere el dataset : 

#https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HRAnalyticsJobChangeDataScientists__aug_train.csv

#Diga usted cual no es una columna del dataset.

#Pregunta 5 Respuesta

#1.city_development_index
#2.y
#3.last_new_job
#4.company_size
#5.training_hours



import pandas as pd

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HRAnalyticsJobChangeDataScientists__aug_train.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Mostrar las primeras 5 filas para tener una idea de las columnas
print(df.head())

# Obtener una lista de todas las columnas
columnas = df.columns.tolist()
print("\nLas columnas del dataset son:", columnas)


#Respusta -> 2.y 