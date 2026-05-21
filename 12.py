"""
Ejercicio 12: Agrupación de datos con groupby

1) Agrupa el DataFrame por la columna 'Sector'.

2) Calcula el PER promedio (media) para cada uno de los tres sectores.

3) Imprime el resultado en pantalla.
"""

import pandas as pd

datos_sectores = {
    'Ticker':['AAPL', 'MSFT', 'JPM', 'BAC', 'XOM', 'CVX'],
    'Sector':['Tecnología', 'Tecnología', 'Finanzas', 'Finanzas', 'Energía', 'Energía'],
    'PER': [28.5, 32.1, 12.3, 11.8, 10.5, 9.8]
}

f_multiples = pd.DataFrame(datos_sectores)


df_sectores = f_multiples.groupby('Sector')['PER'].mean()

print(df_sectores)