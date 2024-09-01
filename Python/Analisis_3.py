import pandas as pd

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/Churn_Subscription_Service.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Contar las ocurrencias de cada género
gender_counts = df['Gender'].value_counts()

# Imprimir los resultados
print(gender_counts)

# Obtener el género con más observaciones
most_common_gender = gender_counts.idxmax()
print("El género con más observaciones es:", most_common_gender)