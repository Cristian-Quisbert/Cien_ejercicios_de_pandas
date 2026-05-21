"""
Ejercicio 11: Desviación Estándar Móvil (Medición de Volatilidad)

1) Crea una nueva columna llamada Vol_4 que calcule la 
desviación estándar móvil de 4 días de la columna Precio.

2) Imprime las primeras 6 filas para observar cuántos NaN
se generan esta vez antes de obtener el primer valor numérico de volatilidad.
"""

import pandas as pd

fechas_largas = pd.date_range(start='2026-01-01', end='2026-01-20', freq='D')
precios_simulados = [100 +i*0.5 for i in range(len(fechas_largas))]

df_historico = pd.DataFrame({'Precio': precios_simulados}, index=fechas_largas)

df_historico['Vol_4'] = df_historico['Precio'].rolling(window=4).std()

print(df_historico.head(6))
