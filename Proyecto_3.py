"""
Calculador de Drawdowns (Racha de Pérdidas)
El Drawdown es una medida de la caída máxima desde un pico hasta un valle
en una serie de tiempo de precios o rendimientos. Es una métrica importante
para evaluar el riesgo de una inversión o estrategia de trading.

1) Calculamos la evolución del capital partiendo de un dólar:
Capital = (1 + Retorno1) x (1 + Retorno2) x ... x (1 + RetornoN) = .cumprod(1 + Retornos)

2) Calculamos el máximo historico del capital hasta cada punto en el tiempo:
Pico = Capital.cummax()

3) Calculams la caída porcentual desde el pico actual:
Drawdown = (Capital - Pico) / Pico

4) El Maximum Drawdown será el valor mínimo del Drawdown a lo largo del tiempo
"""

import pandas as pd
import numpy as np

df_estrategia = pd.DataFrame({
    'Retorno': [0.02, 0.03, -0.05, -0.04, 0.01, 0.05, -0.08, -0.02, 0.03, 0.04, -0.01, 0.02, -0.03, 0.01, 0.02]
}, index=pd.date_range(start='2026-03-01', periods=15, freq='D'))

