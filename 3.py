"""
Ejercicio 3: Creación de columnas calculadas (Operaciones vectorizadas)

Enunciado:

1) Utiliza el DataFrame df_acciones (asegúrate de que las columnas se llamen igual, 
ya que en tu código anterior cambiaste 'Precio' por 'Price').

2) Crea una nueva columna llamada Market_Cap que sea el resultado de multiplicar la 
columna de precio por la columna Volumen.

3) Muestra el DataFrame completo para ver la nueva columna calculada.

"""

import pandas as pd

data = {
    'Ticker': ['AAPL', 'MSFT', 'GOOG'],
    'Precio': [175.50, 420.20, 150.10],
    'Volumen': [50000000, 23000000, 28000000],
}

df_acciones = pd.DataFrame(data)

df_acciones['Market_Cap'] = df_acciones['Precio'] * df_acciones['Volumen']

print(df_acciones)


