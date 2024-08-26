#Para el siguiente dataset :

#https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HRAnalyticsJobChangeDataScientists__aug_train.csv

#Cual no es un posible valor de la columna company_size

#Pregunta 

#1. 500-999
#2. 5000-9999
#3. 10050+
#4. 50-99
#5. 1000-4999

import pandas as pd

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HRAnalyticsJobChangeDataScientists__aug_train.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Obtener los valores únicos de la columna company_size
unique_company_sizes = df['company_size'].unique()

print("Los valores únicos de la columna company_size son:")
print(unique_company_sizes)

#Respuesta -> 3. 10050+