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


svc_cuadrado = np.square(serie_valor_ciudad)

ciudades_uno = pd.Series({
    "Montanita": 300,
    "Guayaquil": 10000,
    "Quito": 2000
    })

ciudades_dos = pd.Series({
    "Loja": 300,
    "Guayaquil": 10000
    })

ciudades_uno["Loja"] = 0

print(ciudades_uno + ciudades_dos)
print(type(ciudades_uno + ciudades_dos))

ciudades_add = ciudades_uno.add(ciudades_dos)
#.sub()
#.mul()
#.div()



ciud_concat = pd.concat([
    ciudades_uno,
    ciudades_dos
    ])

# ciud_concat_verify = pd.concat([
#     ciudades_uno,
#     ciudades_dos
#     ],
#     verify_integrity = True)

# ciud_append_verify = pd.append([ #append y concat hacen lo mismo
#     ciudades_uno,
#     ciudades_dos
#     ],
#     verify_integrity = True)

ciud_concat_verify2 = pd.concat([
    ciudades_uno,
    ciudades_dos
    ],
    verify_integrity = False)

# ciud_append_verify2 = pd.append([ #append y concat hacen lo mismo
#     ciudades_uno,
#     ciudades_dos
#     ],
#     verify_integrity = False)

ciud_append_verify3 = ciudades_uno.append( #append y concat hacen lo mismo
    ciudades_dos,
    verify_integrity = False)

print(ciudades_uno.max())
print(pd.Series.max(ciudades_uno))
print(np.max(ciudades_uno))

print(ciudades_uno.min())
print(pd.Series.min(ciudades_uno))
print(np.min(ciudades_uno))

print(ciudades_uno.mean())  #promedio
print(ciudades_uno.median())    #mediana
print(np.average(ciudades_uno)) #promedio

print(ciudades_uno.head(2))
print(ciudades_uno.tail(2))


print(ciudades_uno.sort_values(
    ascending = False).head(2))

print(ciudades_uno.sort_values().tail(2))

def calcular(valor_serie):
    if(valor_serie <=1000):
        return valor_serie * 1.05
    if(valor_serie > 1000 and valor_serie <= 5000):
        return valor_serie * 1.10
    if(valor_serie > 5000):
        return valor_serie * 1.15
    
ciudad_calculada = ciudades_uno.map(calcular)


#if else
# cuando no cumple condicion aplica

resultado = ciudades_uno.where(ciudades_uno < 1000,
                   ciudades_uno * 1.05)


series_numeros = pd.Series(['1.0', '2', -3])
print(pd.to_numeric(series_numeros))

# 'integer', 'signed', 'unsigned', 'float'
print(pd.to_numeric(series_numeros, downcast = 'integer'))

series_numeros_err = pd.Series(['no tiene', '1.0', '2', -3])

# ignore, coerce, raise (default)
# print(pd.to_numeric(series_numeros_err))
print(pd.to_numeric(series_numeros_err, errors='ignore'))
print(pd.to_numeric(series_numeros_err, errors='coerce'))











