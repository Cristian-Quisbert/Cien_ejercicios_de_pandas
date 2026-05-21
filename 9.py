"""
Ejercicio 9: Filtrado por Fechas (Slicing Temporal)

1) Realiza un corte (slice) utilizando .loc para extraer únicamente los días que van 
desde el 5 de enero de 2026 hasta el 12 de enero de 2026 (ambos inclusive).

2) Guarda ese resultado en un nuevo DataFrame llamado df_recorte e imprímelo en pantalla.
"""

import pandas as pd

fechas_largas = pd.date_range(start='2026-01-01', end='2026-01-20', freq='D')
precios_simulados = [100 + i*0.5 for i in range(len(fechas_largas))]

df_historico = pd.DataFrame({'Precio': precios_simulados}, index=fechas_largas)

df_recorte = df_historico.loc['2026-01-05':'2026-01-12']


print(df_recorte)
