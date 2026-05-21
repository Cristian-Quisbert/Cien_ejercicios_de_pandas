"""
Ejercicio 4: Estadísticos descriptivos básicos

Enunciado:

1) Calcula y guarda en una variable el precio máximo de las acciones.

2) Calcula y guarda en otra variable el volumen total de todas las acciones combinadas.

3) Imprime ambos resultados con un mensaje claro (por ejemplo: "El precio máximo es: ...").

"""

import pandas as pd

data = {
    'Ticker': ['AAPL', 'MSFT', 'GOOG'],
    'Precio': [175.50, 420.20, 150.10],
    'Volumen': [50000000, 23000000, 28000000],
}

df_acciones = pd.DataFrame(data)

precio_max = df_acciones['Precio'].max()

volumen_total = df_acciones['Volumen'].sum()

print(
    f'El precio máximo es: {precio_max}\nEl volumen total es: {volumen_total}' 
    
)
