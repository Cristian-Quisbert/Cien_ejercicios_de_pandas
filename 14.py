"""
Ejercicio 14: Combinar DataFrames con merge (Uniones tipo SQL)

1) Realiza un merge de tipo inner entre df_precios y df_info usando 
la columna 'Ticker'.

2) Imprime el DataFrame resultante y observa qué pasó con TSLA y NVDA.

"""

import pandas as pd

df_precios = pd.DataFrame({
    'Ticker':['AAPL', 'MSFT', 'JPM', 'TSLA'],
    'Precio':[175.50, 420.20, 180.10, 190.40]
})


df_info = pd.DataFrame({
    'Ticker': ['AAPL', 'MSFT', 'JPM', 'NVDA'],
    'Compañia': ['Apple Inc.', 'Microsoft Corp.', 'JPMorgan Chase', 'NVIDIA Corp.']
})


df_completo = pd.merge(df_precios, df_info, on='Ticker', how='inner')


print(df_completo)