"""
Ejercicio 10: Medias Móviles Simples (rolling)

1) Crea una nueva columna llamada MA_3 que calcule la media móvil 
simple de 3 días de la columna Precio.

2) Imprime las primeras 6 filas del DataFrame para comprobar cómo 
se comportan los primeros valores nulos (NaN) y cuándo empieza 
a calcularse la media correctamente.

"""

import pandas as pd

fechas_largas = pd.date_range(start='2026-01-01', end='2026-01-20', freq='D')
precios_simulados = [100 + i*0.5 for i in range(len(fechas_largas))]

df_historico = pd.DataFrame({'Precio': precios_simulados}, index=fechas_largas)

df_historico['MA_3'] = df_historico['Precio'].rolling(window=3).mean()

print(df_historico.head(6))