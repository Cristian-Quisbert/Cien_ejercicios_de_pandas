"""
Ejercicio 16: Ranking de activos (rank)

1) Crea una nueva columna llamada Rank_Rendimiento.

2) Utiliza el método .rank() para asignar el puesto 1 
a la criptomoneda con el mayor retorno, el puesto 2 a la 
siguiente, y así sucesivamente (orden descendente).

3) Imprime el DataFrame ordenado visualmente por esa nueva 
columna de menor a mayor ranking usando .sort_values('Rank_Rendimiento').
"""


import pandas as pd

df_cripto = pd.DataFrame({
    'Cypto': ['BTC', 'ETH', 'SOL', 'ADA', 'DOT'],
    'Retorno_diario':[1.2, -0.5, 4.8, -2.1, 0.3]
})


df_cripto['Rank_Rendimiento'] = df_cripto['Retorno_diario'].rank(ascending=False)

df_cripto.set_index('Rank_Rendimiento', inplace=True)

df_cripto = df_cripto.sort_values('Rank_Rendimiento')

print(df_cripto)