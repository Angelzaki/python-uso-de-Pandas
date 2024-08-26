#Considere el siguiente dataset : 

#https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HRAnalyticsJobChangeDataScientists__aug_train.csv

#Con respecto a la columna city, cuantas observaciones posee el valor city_160

#Pregunta 

#1. 4355
#2. 845
#3. 1336
#4. 1
#5. 3




import pandas as pd

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HRAnalyticsJobChangeDataScientists__aug_train.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Contar las observaciones con "city_160"
count_city_160 = df[df['city'] == 'city_160'].shape[0]

print("Número de observaciones en city_160:", count_city_160)