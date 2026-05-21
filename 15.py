"""
Ejercicio 15: Concatenación de datos con concat

1) Concatena ambos DataFrames verticalmente en uno nuevo
llamado df_operaciones_diarias.

2) Asegúrate de que el índice se resetee de forma limpia 
para que vaya consecutivamente desde el 0 hasta el 3 
(evitando que se repitan los índices originales).

3) Imprime el resultado.
"""

import pandas as pd

df_mañana = pd.DataFrame({
    'Ticker':['AAPL', 'MSFT'],
    'Acciones':[10, 5],
    'Operación':['Compra', 'Compra']
})

df_tarde = pd.DataFrame({
    'Ticker':['GOOG', 'AAPL'],
    'Acciones':[15, 2],
    'Operación':['Compra', 'Venta']
})


df_operaciones_diarias = pd.concat([df_mañana ,df_tarde], ignore_index=True)


print(df_operaciones_diarias)