# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:53 2020

@author: erick
"""


import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

series_a = pd.Series(
    lista_numeros)

series_b = pd.Series(
    tupla_numeros)

series_c = pd.Series(
    np_numeros)

series_d = pd.Series(
    [True,
     False,
     12,
     12.12,
     "Erick",
     None,
     (1),
     [2],
     {"nombre":"Erick"}
     ])

print(series_d[3])

lista_ciudades = [
    "Ambato",
    "Cuenca",
    "Loja",
    "Quito"]

serie_ciudad = pd.Series(
    lista_ciudades,
    index = [
        "A",
        "C",
        "L",
        "Q"
        ])

print(serie_ciudad[3])
print(serie_ciudad["C"])

valores_ciudad = {
    "Ibarra":9500,
    "Guayaquil":10000,
    "Cuenca":7000,
    "Quito":8000,
    "Loja":3000
    }

serie_valor_ciudad = pd.Series(
    valores_ciudad)

ciudades_menor_5k = serie_valor_ciudad < 5000
print(type(serie_valor_ciudad)) ##series de pandas
print(type(ciudades_menor_5k)) ##series de pandas
print(ciudades_menor_5k)

s5 = serie_valor_ciudad[ciudades_menor_5k]

serie_valor_ciudad = serie_valor_ciudad * 1.1

serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 50

print("Lima" in serie_valor_ciudad)


