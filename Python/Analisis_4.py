import pandas as pd

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HeartDisease2022.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Contar las ocurrencias de cada categoría de SmokerStatus
smoker_status_counts = df['SmokerStatus'].value_counts(normalize=True) * 100

# Imprimir los porcentajes
print(smoker_status_counts)

# Obtener la categoría con el mayor porcentaje
most_common_smoker_status = smoker_status_counts.idxmax()
print("La categoría de SmokerStatus con el mayor porcentaje es:", most_common_smoker_status)