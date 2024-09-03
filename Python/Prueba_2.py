import pandas as pd

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/crop_production.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Contar el total de observaciones
total_observations = len(df)

# Contar los valores faltantes en la columna "Production"
missing_values_production = df['Production'].isnull().sum()

# Calcular el porcentaje de valores faltantes
percentage_missing = (missing_values_production / total_observations) * 100

print("Porcentaje de valores faltantes en la columna 'Production':", percentage_missing, "%")