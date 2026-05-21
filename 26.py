"""
Ejercicio 26: Ventanas móviles personalizadas con .rolling().apply()

1) Crea una nueva columna llamada Rango_Movil_3D.

2) Aplica un .rolling() con una ventana de 3 periodos.

3) Usa .apply() junto con una función lambda x: ... para calcular la 
diferencia entre el máximo de esa ventana (x.max()) y el mínimo de esa 
ventana (x.min()). Asegúrate de incluir raw=True.

4) Imprime el DataFrame resultante.
"""

import pandas as pd
import numpy as np

df_datos = pd.DataFrame({
    'Precio': [100, 105, 102, 108, 107, 115]
}, index=pd.date_range(start='2026-01-01', periods=6, freq='D'))

df_datos['Rango_Movil_3D'] = df_datos['Precio'].rolling(window=3).apply(lambda x: x.max()-x.min(), raw=True)

print(df_datos)