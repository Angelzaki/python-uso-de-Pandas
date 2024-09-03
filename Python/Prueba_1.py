import pandas as pd

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/marketing.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Contar los valores faltantes en la columna "youtube"
missing_values_youtube = df['youtube'].isnull().sum()

print("Número de valores faltantes en la columna 'youtube':", missing_values_youtube)