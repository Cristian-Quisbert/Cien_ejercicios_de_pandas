"""
Ejercicio 6: Métodos de Imputación Financiera (ffill y bfill) (forward and backward)

1) Modifica el DataFrame para que los valores faltantes se rellenen con el último 
precio disponible (el del día anterior). Es decir, el Martes debería tomar el precio
del Lunes, y el Jueves el del Miércoles.

2) Imprime el resultado final.
"""

import pandas as pd
import numpy as np

datos_historicos = {
    'Dia': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'],
    'Precio_Cierre': [100.5, np.nan, 102.3, np.nan, 105.0]
}

df_precios = pd.DataFrame(datos_historicos)

df_precios['Precio_Cierre'] = df_precios['Precio_Cierre'].ffill()

print(df_precios)

