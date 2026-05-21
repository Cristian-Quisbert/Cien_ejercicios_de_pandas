"""
Ejercicio 24: Prevenir el sesgo de anticipación (Look-Ahead Bias) con shift

1) Crea una columna llamada Señal_Ejecutada desplazando Señal_Teorica 1 
día hacia adelante usando .shift(1). Esto garantiza que la señal calculada 
el día 1 se aplique en el mercado el día 2.

2) Calcula el retorno de tu estrategia en una nueva columna llamada 
Retorno_Estrategia multiplicando Retorno_Activo por Señal_Ejecutada.

3) Imprime el DataFrame.
"""

import pandas as pd

df_backtest = pd.DataFrame({
    'Retorno_Activo': [0.02, -0.01, 0.03, 0.01],
    'Señal_Teorica': [1, 0, 1, 1]
}, index=pd.date_range(start='2026-01-01', periods=4, freq='D'))

df_backtest['Señal_Ejecutada'] = df_backtest['Señal_Teorica'].shift(1)

df_backtest['Retorno_Estrategia'] = df_backtest['Señal_Ejecutada'] * df_backtest['Retorno_Activo']

print(df_backtest)