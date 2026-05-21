"""
Ejercicio 5: Manejo de datos faltantes (Missing Data)

1) Reemplaza los valores NaN de la columna Precio_Cierre utilizando 
la media (promedio) de los días que sí tienen datos.

2) Imprime el DataFrame final para verificar que ya no queden valores nulos.
"""

import pandas as pd
import numpy as np

datos_historicos = {
    'Dia': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'],
    'Precio_cierre': [100.5, np.nan, 102.3, np.nan, 105.0]
}

df_precio = pd.DataFrame(datos_historicos)

df_precio['Precio_cierre'] = df_precio['Precio_cierre'].fillna(df_precio['Precio_cierre'].mean())

print(df_precio)