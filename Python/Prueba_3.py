import pandas as pd
import numpy as np

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/crop_production.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Calcular el percentil 16 de la columna "Area"
percentil_16_area = np.percentile(df['Area'], 16)

print("El percentil 16 de la variable Area es:", percentil_16_area)