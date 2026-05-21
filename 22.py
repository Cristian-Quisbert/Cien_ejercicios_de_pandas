"""
Ejercicio 22: Múltiples condiciones complejas con np.select

1) Crea una lista de condiciones utilizando operadores lógicos:
Condición de Venta: Precio > Banda_Superior
Condición de Compra: Precio < Banda_Inferior

2) Crea una lista de resultados: la venta debe valer -1 y la compra debe valer 1.

3) Utiliza np.select para generar la columna Señal. Si el precio está dentro de las 
bandas (no cumple ninguna condición), el valor por defecto debe ser 0.

4) Imprime el DataFrame resultante.
"""

import pandas as pd
import numpy as np

datos_bandas = {
    'Precio': [100, 105, 96, 101, 112, 94],
    'Banda_Superior': [110, 110, 110, 110, 110, 110],
    'Banda_Inferior': [95, 95, 95, 95, 95, 95]
}
df_bandas = pd.DataFrame(datos_bandas)

condiciones = [
    df_bandas['Precio'] > df_bandas['Banda_Superior'],
    df_bandas['Precio'] < df_bandas['Banda_Inferior'],
]

resultados = [-1,1]

df_bandas['Señal'] = np.select(condiciones, resultados, default=0)

print(df_bandas)