"""
Ejercicio 8: Cálculo de Retornos Diarios (pct_change)

1) Crea una nueva columna llamada Retorno que contenga el cambio 
porcentual diario de la columna Cierre.

2) Multiplica esa nueva columna por 100 para expresar los retornos 
en formato de porcentaje (por ejemplo, si da 0.012, que se transforme en 1.2).

3) Imprime el DataFrame resultante.
"""


import pandas as pd

datos_fechas = {
    'Fecha': ['2026-01-02', '2026-01-05', '2026-01-06', '2026-01-07'],
    'Cierre': [150.25, 151.10, 149.80, 152.30]
}

df_temporal = pd.DataFrame(datos_fechas)

df_temporal['Fecha'] = pd.to_datetime(df_temporal['Fecha'])

df_temporal.set_index('Fecha', inplace=True)


df_temporal['Retorno'] = df_temporal['Cierre'].pct_change()

df_temporal['Retorno'] = df_temporal['Retorno']*100


print(df_temporal)
