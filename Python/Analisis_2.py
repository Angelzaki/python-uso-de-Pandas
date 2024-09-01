import pandas as pd

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/Churn_Subscription_Service.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Obtener los valores únicos de la columna PaymentMethod
unique_payment_methods = df['PaymentMethod'].unique()

# Contar los valores únicos
num_unique_payment_methods = len(unique_payment_methods)

print("Número de valores únicos en PaymentMethod:", num_unique_payment_methods)