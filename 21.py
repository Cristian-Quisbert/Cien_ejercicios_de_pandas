"""
Ejercicio 21: Creación de Señales de Trading Vectorizadas con np.where

1) Utiliza np.where para crear una nueva columna llamada Posicion.

2) La regla de tu algoritmo será: si el Precio es estrictamente mayor 
que la MA_3, la posición debe ser 1 (indica que compramos). De lo 
contrario, la posición debe ser -1 (indica que vendemos en corto o salimos).

3) Imprime el DataFrame resultante.
"""

import pandas as pd
import numpy as np

datos_estrategia = {
    'Precio': [100, 102, 99, 101, 105, 104],
    'MA_3': [101, 101, 100, 100, 101, 103]
}
df_trading = pd.DataFrame(datos_estrategia)

df_trading['Posicion'] = np.where(df_trading['Precio'] > df_trading['MA_3'], 1, -1)

print(df_trading)