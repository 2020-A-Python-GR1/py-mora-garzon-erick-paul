# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 08:00:13 2020

@author: erick
"""

import pandas as pd

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

#primero = df.loc[1035]
#segundo = df.loc[1035, 'artist']

#loc

filtrado_horizontal = df.loc[1035] #serie
print(filtrado_horizontal)
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index)


serie_vertical = df['artist']
print(serie_vertical)
print(serie_vertical.index)

print(df[['artist']])

#print(df.iloc[0])

#filtrado por indice
df_1035 = df[df.index == 1035]

segundo = df.loc[1035] #filtrar por indice (1)
segundo = df.loc[[1035,1036]] #filtrar por arr indice
segundo = df.loc[3:5] #filtrando desde X indice
                        #hasta Y indice
segundo = df.loc[df.index == 1035] # filtrar por arreglo - true false

segundo = df.loc[1035, 'artist'] # 1 indice
segundo = df.loc[1035, ['artist', 'medium']] #varios indices

#print(df.loc[0]) # indice dentro del dataframe
#print(df[0]) # indice dentro del dataframe

#iloc - acceder grupo filas y columnas indices en 0
tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]

tercero = df.iloc[0:10, 0:4] #filtrado indices por rango de indice 0:4





