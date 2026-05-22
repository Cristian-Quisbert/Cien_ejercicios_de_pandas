"""
Ejercicio 30: Relleno inteligente de nulos financieros (ffill e interpolate)

1) Crea una nueva columna llamada Precio_FFILL aplicando el método .ffill() 
sobre la columna Precio_Sucio.

2) Crea otra columna llamada Precio_Interpolado aplicando el método .interpolate() 
sobre la columna Precio_Sucio.

3) Imprime el DataFrame resultante.

4) Observa con atención las diferencias lógicas entre los valores que generó 
.ffill() y los que generó .interpolate() en las fechas que tenían nulos.
"""

import pandas as pd
import numpy as np

df_mercado = pd.DataFrame({
    'Precio_sucio': [100,101.5,np.nan,np.nan,102,103.5]


}, index=pd.date_range(start='2026-05-01', periods=6, freq='D'))

df_mercado['Precio_FFILL'] = df_mercado['Precio_sucio'].ffill()

df_mercado['Precio_interpolado'] = df_mercado['Precio_sucio'].interpolate()

print(df_mercado)