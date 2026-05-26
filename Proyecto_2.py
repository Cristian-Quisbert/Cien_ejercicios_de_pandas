"""
Proyecto: El Optimizador de Sharpe Vectorizado (Curva Elevada)


"""

import pandas as pd
import numpy as np

np.random.seed(42)
dias = 100
df_retornos = pd.DataFrame({
    'Alfa': np.random.normal(0.001, 0.015, dias),   # Retorno medio bajo, volatilidad baja
    'Beta': np.random.normal(0.002, 0.030, dias),   # Retorno medio alto, volatilidad alta
    'Gamma': np.random.normal(0.0005, 0.008, dias)  # Retorno muy bajo, volatilidad muy baja
}, index=pd.date_range(start='2026', periods=dias, freq='B'))  # 'B' es días hábiles


# media, varianza, cuantas veces


# diminución del peso del df
df_retornos = df_retornos.astype({
    'Alfa':'float32',
    'Beta':'float32',
    'Gamma':'float32'
})

# la formula de sharpe ratio es: Sharpe = Retorno esperado - Retorno Seguro / Desviación estándar 

# Calculo de retorno anualizado promerio de las 3 estrategias
retorno_anual = df_retornos.mean() * 252

# Calculo de la volatilidad anualizada
volatilidad_anual = df_retornos.std() * np.sqrt(252)

# Aplicación del sharpe ratio
Sharpe_ratio = (retorno_anual-0.04)/volatilidad_anual

# df final
df_metricas = pd.DataFrame({
    'Retorno_anual':retorno_anual,
    'Volatilidad_anual':volatilidad_anual,
    'Ratio_sharpe':Sharpe_ratio,
})

# usamos transponer para que se vea mejor
df_metricas = df_metricas.transpose()

print(df_metricas)

# mi conclusión es que la estrategia Gamma es la mejor, tiene un rendimiento muy bueno para tener el sharpe 1.57

