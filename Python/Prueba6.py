import pandas as pd
from sklearn.linear_model import GeneralizedLinearRegressor

# Cargar los datos
data = pd.read_csv("hotel_data.csv")

# Separar las variables predictoras y la variable objetivo
X = data.drop('children', axis=1)  # Suponiendo que 'children' es la columna objetivo
y = data['children']

# Dividir los datos en entrenamiento y prueba (opcional)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y ajustar el modelo
glm_poisson = GeneralizedLinearRegressor(family='Poisson')
glm_poisson.fit(X_train, y_train)