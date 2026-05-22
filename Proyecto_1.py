"""
El Proyecto: Motor de Backtesting Automatizado

Fase 1: ETL y Optimización de Memoria
Convierte la columna 'Ticker' al tipo más eficiente para textos repetidos.
Convierte la columna 'Precio' a un formato flotante de precisión simple (float32).
Pivotea el DataFrame df_raw para pasar de formato largo a formato ancho (Matriz). 
Las filas deben ser la 'Fecha', las columnas los 'Ticker' y los valores el 'Precio'. 
Salva este resultado en un nuevo DataFrame llamado df_precios.
Limpia los valores NaN de df_precios usando el método preferido por los Quants para 
no meter sesgos del futuro.


Fase 2: Cálculos Matemáticos del Mercado
Calcula el Retorno Diario para ambos activos a partir de la matriz limpia de precios 
y guárdalo en un DataFrame llamado df_retornos.


Fase 3: Indicador Técnico y Señales Lógicas (Enfocado en BTC)
Crea un nuevo DataFrame llamado df_btc que contenga únicamente la columna del precio 
de 'BTC' y la columna de su retorno diario 'Retorno_BTC'.
Calcula una Media Móvil de 3 períodos para BTC y agrégala como la columna 'MA_3'.
Genera una columna llamada 'Señal_Teorica': si el precio de BTC es estrictamente mayor 
que su 'MA_3', la señal es 1 (Compra). De lo contrario, la señal es -1 (Venta en corto). 
¡Usa vectorización!

Fase 4: Ejecución y Rendimiento de la Estrategia
Crea la columna 'Señal_Ejecutada' desplazando la señal teórica para eliminar el Look-Ahead Bias.
Calcula el 'Retorno_Estrategia' multiplicando el retorno real de BTC por la señal ejecutada.


Imprime el DataFrame df_btc final completo para auditar el sistema.
"""

import pandas as pd
import numpy as np

# Dirty data
fechas = pd.date_range(start='2026-05-01', periods=10, freq='D').repeat(2)

tickers = ['BTC', 'ETH']*10

precios_sucios = [
    60000, 3000, 61000, 3100, np.nan, np.nan, 59000, 2950, 58500, 2900,
    62000, 3200, 63000, np.nan, 64000, 3350, 63500, 3300, 65000, 3400
]

df_raw = pd.DataFrame({
    'Fecha': fechas,
    'Ticker': tickers,
    'Precio': precios_sucios
})


# ==================================FASE 1==================================
df_cleaned = df_raw.astype({
    'Ticker':'category',
    'Precio': 'float32'
}) 

df_precios = df_cleaned.pivot(index='Fecha', columns='Ticker', values='Precio')

df_precios['BTC'] = df_precios['BTC'].ffill()

df_precios['ETH'] = df_precios['ETH'].ffill()


# ==================================FASE 2==================================

df_retornos = df_precios.pct_change()

# ==================================FASE 3==================================
df_btc = pd.DataFrame({
    'BTC': df_precios['BTC'],
    'Retornos_BTC': df_retornos['BTC']
})

df_btc['MA_3'] = df_btc['BTC'].rolling(window=3).mean()

df_btc['señal_teorica'] = np.where(df_btc['BTC'] > df_btc['MA_3'], 1, -1)


# ==================================FASE 4==================================
df_btc['Señal_ejecutada'] = df_btc['señal_teorica'].shift()

df_btc['Retorno estrategia'] = df_btc['Retornos_BTC'] * df_btc['Señal_ejecutada']

print(df_btc)