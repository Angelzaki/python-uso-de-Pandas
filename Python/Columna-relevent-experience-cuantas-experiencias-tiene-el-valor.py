#Para el siguiente dataset 

#https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HRAnalyticsJobChangeDataScientists__aug_train.csv

#Para la columna relevent_experience, cuantas observaciones tiene el valor : No relevent experience.

#Pregunta 

#1. 19158
#2. 5366
#3. 13792
#4. Ninguna de las anteriores 
#5. 14


import pandas as pd

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HRAnalyticsJobChangeDataScientists__aug_train.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Print the columns of the dataframe to inspect the column names
print(df.columns)

# Contar las observaciones con "No relevant experience"
count_no_relevant_experience = df[df['relevent_experience'] == 'No relevent experience'].shape[0]

print("Número de observaciones con 'No relevant experience':", count_no_relevant_experience)

#Respusta -> 2. 5366