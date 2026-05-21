"""
Ejercicio 27: Pivotar tablas con pivot (De formato largo a ancho)

1) Aplica el método .pivot() para transformar df_largo en un nuevo DataFrame llamado df_ancho.

2) El resultado debe tener las fechas como índice, una columna para AAPL, otra columna 
para MSFT y los precios como los valores internos.

3) Imprime el DataFrame resultante.
"""

import pandas as pd

datos_largos = {
    'Fecha': ['2026-01-01', '2026-01-01', '2026-01-02', '2026-01-02', '2026-01-03', '2026-01-03'],
    'Ticker': ['AAPL', 'MSFT', 'AAPL', 'MSFT', 'AAPL', 'MSFT'],
    'Precio': [170, 410, 172, 415, 171, 412]
}
df_largo = pd.DataFrame(datos_largos)

df_ancho = df_largo.pivot(index='Fecha', columns='Ticker', values='Precio')

print(df_largo)
print(df_ancho)