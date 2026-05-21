"""
Ejercicio 18: Transformaciones personalizadas con apply y lambda

1) Crea una nueva columna llamada Perfil_Riesgo.

2) Utiliza .apply() junto con una función lambda 
para asignar la etiqueta 'Alta Volatilidad' si el 
valor es mayor o igual a 0.30, y 'Baja Volatilidad' si es menor a 0.30.

3) Imprime el DataFrame resultante.
"""


import pandas as pd

df_riesgo = pd.DataFrame({
    'Ticker': ['TSLA', 'JNJ', 'NVDA', 'PG'],
    'Volatilidad': [0.45, 0.15, 0.52, 0.12]
})

df_riesgo['Perfil_riesgo'] = df_riesgo['Volatilidad'].apply(lambda x: 'Alta volatilidad' if x>0.29 else 'Baja volatilidad')

print(df_riesgo)
