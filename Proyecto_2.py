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
Retorno_Anualizado_Promedio_Alfa = df_retornos['Alfa'].mean()*252
Retorno_Anualizado_Promedio_Beta = df_retornos['Beta'].mean()*252
Retorno_Anualizado_Promedio_Gamma = df_retornos['Gamma'].mean()*252
retorno_anual = df_retornos.mean()

# Calculo de la volatilidad anualizada
Volatilidad_Anualizada_Promedio_Alfa = df_retornos['Alfa'].std() * np.sqrt(252)
Volatilidad_Anualizada_Promedio_Beta = df_retornos['Beta'].std() * np.sqrt(252)
Volatilidad_Anualizada_Promedio_Gamma = df_retornos['Gamma'].std() * np.sqrt(252)
volatilidad_anual = df_retornos.std() * np.sqrt(252)

# Aplicación del sharpe ratio
Sharpe_Alfa = (Retorno_Anualizado_Promedio_Alfa - 0.04) / (Volatilidad_Anualizada_Promedio_Alfa)
Sharpe_Beta = (Retorno_Anualizado_Promedio_Beta - 0.04) / (Volatilidad_Anualizada_Promedio_Beta)
Sharpe_Gamma = (Retorno_Anualizado_Promedio_Gamma - 0.04) / (Volatilidad_Anualizada_Promedio_Gamma)
Sharpe_ratio = (retorno_anual-0.04)/volatilidad_anual

# df final
df_metricas = pd.DataFrame({
    'Alfa':retorno_anual,
    'Volatilidad_anual':volatilidad_anual,
    'Ratio_sharpe':Sharpe_ratio
    'Indicador':['Retorno_anual', 'Volatilidad_anual','Ratio_Sharpe']
})

df_metricas.set_index('Indicador', inplace=True)


print(df_metricas)


