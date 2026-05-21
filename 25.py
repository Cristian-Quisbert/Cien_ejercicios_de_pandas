"""
Ejercicio 25: Diferencias consecutivas con diff

1) Crea una nueva columna llamada Variacion_Volumen utilizando el método .diff().

2) Imprime el DataFrame final.
"""

import pandas as pd

df_volumen = pd.DataFrame({
    'Volumen':[50000, 52000, 48000, 65000]
},index=pd.date_range(start='2026-01-01', periods=4, freq='D'))

df_volumen['Variacion_Volumen'] = df_volumen['Volumen'].diff()

print(df_volumen)
