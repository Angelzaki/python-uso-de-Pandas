#Considere el siguiente dataset 

#https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HRAnalyticsJobChangeDataScientists__aug_train.csv

#Cual es el maximo valor de la columna city_development_index

#Pregunta 

#1. 0.949
#2. 949
#3. -0.949
#4. 1949
#5. 1.949


import pandas as pd

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HRAnalyticsJobChangeDataScientists__aug_train.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Encontrar el valor máximo de city_development_index
max_city_development_index = df['city_development_index'].max()

print("El valor máximo de city_development_index es:", max_city_development_index)