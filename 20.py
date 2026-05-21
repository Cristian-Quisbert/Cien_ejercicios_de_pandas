"""
Ejercicio 20: Índices Jerárquicos (MultiIndex)

1) Convierte la columna 'Fecha' a tipo datetime.

2) Configura un índice compuesto (MultiIndex) utilizando las 
columnas 'Fecha' y 'Ticker' en ese orden específico.

3) Ordena el índice del DataFrame utilizando .sort_index().

4) Imprime el DataFrame resultante para ver cómo se estructuran 
jerárquicamente las filas.
"""
import pandas as pd

datos_multi = {
    'Fecha': ['2026-01-01', '2026-01-01', '2026-01-02', '2026-01-02'],
    'Ticker': ['AAPL', 'MSFT', 'AAPL', 'MSFT'],
    'Precio': [170.50, 410.20, 172.00, 412.50]
}
df_panel = pd.DataFrame(datos_multi)

df_panel['Fecha'] = pd.to_datetime(df_panel['Fecha'])

df_panel.set_index(['Fecha', 'Ticker'], inplace=True)

df_panel.sort_index(inplace=True)

print(df_panel)



