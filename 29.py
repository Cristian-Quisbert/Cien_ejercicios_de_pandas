"""
Ejercicio 29: Optimización de tipos de datos para ahorrar memoria (astype)

1) Antes de hacer cambios, ejecuta print(df_pesado.info()) para observar el 
uso de memoria actual de la consola.

2) Utiliza .astype() para transformar la columna 'Ticker' al tipo 'category' 
y la columna 'Precio' al tipo 'float32'.

3) Vuelve a ejecutar print(df_pesado.info()) sobre el mismo DataFrame optimizado.

4) Compara los resultados en la salida.
"""

import pandas as pd

df_pesado = pd.DataFrame({
    'Ticker': ['AAPL', 'AAPL', 'MSFT', 'MSFT'] * 25000, # 100,000 filas
    'Precio': [170.50, 171.20, 410.10, 412.30] * 25000
})

print(df_pesado.info())

df_liviano = df_pesado.astype({'Ticker': 'category', 'Precio': 'float32'})

print(df_liviano.info())