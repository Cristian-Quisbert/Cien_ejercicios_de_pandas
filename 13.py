"""
Ejercicio 13: Agregaciones múltiples con agg

1) Agrupa el DataFrame por 'Sector'.

2) Utiliza el método .agg() para calcular, en una sola línea de código, 
la media (mean) y la desviación estándar (std) únicamente de la columna 'PER'.

3) Imprime el resultado.
"""

import pandas as pd

datos_avanzados = {
    'Ticker': ['AAPL', 'MSFT', 'JPM', 'BAC', 'XOM', 'CVX'],
    'Sector': ['Tecnología', 'Tecnología', 'Finanzas', 'Finanzas', 'Energía', 'Energía'],
    'PER': [28.5, 32.1, 12.3, 11.8, 10.5, 9.8],
    'Div_Yield': [0.5, 0.8, 2.5, 3.1, 4.2, 4.5]
}

df_analisis = pd.DataFrame(datos_avanzados)


agrupado = df_analisis.groupby('Sector')['PER'].agg(['mean', 'std'])

print(agrupado)

