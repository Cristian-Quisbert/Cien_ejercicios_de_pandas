"""
Ejercicio 23: Desplazamientos temporales con shift (El cálculo de retornos manual)

1) Crea una nueva columna llamada Precio_Ayer usando el método .shift() adecuado.

2) Crea otra columna llamada Retorno_Manual aplicando la fórmula matemática 
utilizando las columnas Precio y Precio_Ayer.

3) Imprime el DataFrame resultante.
"""

import pandas as pd

df_precios = pd.DataFrame({
    'Precio': [100, 105, 103, 108]
}, index=pd.date_range(start='2026-01-01', periods=4, freq='D'))

df_precios['Precio_Ayer'] = df_precios['Precio'].shift(1)

df_precios['Retorno_Manual'] = (df_precios['Precio']-df_precios['Precio_Ayer'])/df_precios['Precio_Ayer']

print(df_precios)

