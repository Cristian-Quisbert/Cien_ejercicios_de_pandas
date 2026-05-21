"""
Ejercicio 1: Creación de un DataFrame y exploración inicial

Enunciado: Crea un DataFrame llamado df_acciones que contenga la siguiente información sobre tres empresas (Apple, Microsoft y Google):

Una columna llamada Ticker con los valores: 'AAPL', 'MSFT', 'GOOG'.

Una columna llamada Precio con los valores: 175.50, 420.20, 150.10.

Una columna llamada Volumen con los valores: 50000000, 23000000, 28000000.

Una vez creado, muestra en pantalla solo las 2 primeras filas del DataFrame.
"""

import pandas as pd

data = {
    'Ticker': ['AAPL', 'MSFT', 'GOOG'],
    'Precio': [175.50, 420.20, 150.10],
    'Volumen': [50000000, 23000000, 28000000],
}

df_acciones = pd.DataFrame(data)

print(df_acciones.head(2))