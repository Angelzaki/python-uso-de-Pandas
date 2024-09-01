import pandas as pd
import numpy as np

# URL del dataset
url = 'https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HeartDisease2022.csv'

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Calcular el percentil 66 de la altura
percentil_66 = np.percentile(df['HeightInMeters'], 66)

print("El percentil 66 de la altura es:", percentil_66)