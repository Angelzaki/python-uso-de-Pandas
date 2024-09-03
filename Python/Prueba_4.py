import pandas as pd

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/student-por.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Calcular la mediana de la columna "age"
median_age = df['age'].median()

print("La mediana de la edad es:", median_age)