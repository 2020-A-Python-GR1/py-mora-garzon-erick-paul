# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:38:43 2020

@author: erick
"""
import pandas as pd

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

serie_artistas_dup = df['artist']

artistas = pd.unique(serie_artistas_dup)

print(type(artistas)) # numpy array

print(artistas.size)
print(len(artistas))

blake = df['artist'] == 'Blake, William' # Serie

print(blake.value_counts())

df_blake = df[blake] #dataframe
