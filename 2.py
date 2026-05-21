"""
Ejercicio 2: Selección de columnas y filtrado básico

Enunciado:

1) Filtra el DataFrame para obtener únicamente las filas donde el Volumen sea mayor o igual a 28,000,000.

2) De ese resultado, selecciona y muestra únicamente la columna Ticker.

"""


import pandas as pd

data={
    'Ticker':['AAPL', 'MSFT', 'GOOG'],
    'Price':[175.50, 420.20, 150.10],
    'Volumen':[50000000, 23000000, 28000000]
}

df_acciones = pd.DataFrame(data)

volumen_alto = df_acciones[df_acciones['Volumen']>=28000000]

print(volumen_alto['Ticker'])

