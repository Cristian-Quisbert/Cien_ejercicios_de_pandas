"""
Ejercicio 19: Agrupación temporal con resample

1) Aplica .resample() para agrupar los datos en periodos de 5 días 
(el código de frecuencia para 5 días es '5D').

2) Calcula el precio máximo alcanzado en cada uno de esos bloques de 5 días.

3) Imprime el resultado.
"""

import pandas as pd
import numpy as np

fechas = pd.date_range(start='2026-01-01', periods=15, freq='D')
precios = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]


df_precio = pd.DataFrame({'Precio': precios}, index=fechas)

df_cinco_dias = df_precio['Precio'].resample('5D').max()

print(df_cinco_dias)