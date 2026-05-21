"""
Ejercicio 7: Convertir a Datetime y establecer el Índice

1) Convierte la columna 'Fecha' a un objeto de tipo datetime de Pandas.

2) Configura esa columna 'Fecha' como el índice (index) del DataFrame.

3) Imprime el DataFrame resultante y fíjate en cómo cambia la estructura 
visual de la tabla (el índice ya no será 0, 1, 2...).
"""

import pandas as pd

datos_fechas = {
    'Fecha': ['2026-01-02', '2026-01-05', '2026-01-06', '2026-01-07'],
    'Cierre': [150.25, 151.10, 149.80, 152.30]
}

df_temporal = pd.DataFrame(datos_fechas)

df_temporal['Fecha'] = pd.to_datetime(df_temporal['Fecha'])

df_temporal.set_index('Fecha', inplace=True)

print(df_temporal)