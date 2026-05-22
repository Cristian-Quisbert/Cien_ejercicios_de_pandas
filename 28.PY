"""
Ejercicio 28: El camino inverso con melt (De formato ancho a largo)

1) Dado que las fechas están en el índice, primero aplica .reset_index(inplace=True) 
a df_ancho para que la fecha vuelva a ser una columna normal llamada 'index'.

2) Aplica pd.melt() configurando 'index' en id_vars, renombra la columna de los tickers 
como 'Ticker' y la de los precios como 'Precio'.

3) Imprime el DataFrame resultante.
"""

import pandas as pd

df_ancho = pd.DataFrame({
    'AAPL': [170, 172, 171],
    'MSFT': [410, 415, 412]
}, index=pd.date_range(start='2026-01-01', periods=3, freq='D'))

df_ancho.reset_index(inplace=True)

df_largo = pd.melt(
    df_ancho, 
    id_vars=['index'], # columna que queda como identificador
    var_name='Ticker', # nombre de la columna nueva 
    value_name='Precio' # nombre de la columna nueva (numeros)
)

print(df_ancho ,"\n")
print(df_largo)