"""
Ejercicio 17: Reemplazo y limpieza de strings (str.replace)

1) Limpia la columna 'Margen_Neto' eliminando el símbolo de porcentaje (%).

2) Convierte esa columna a tipo numérico decimal (float).

3) Divide el resultado entre 100 para que los márgenes queden expresados 
en formato tanto por uno (es decir, que 25.8 pase a ser 0.258).

4) Imprime el DataFrame final.
"""

import pandas as pd

df_financiero = pd.DataFrame({
    'Ticker': ['AAPL', 'MSFT', 'GOOG'],
    'Margen_neto': ['25.8%', '31.2%', '22.5%']
})

df_financiero['Margen_neto'] = df_financiero['Margen_neto'].str.replace('%','', regex=False).astype(float)

df_financiero['Margen_neto'] = df_financiero['Margen_neto']/100

print(df_financiero)