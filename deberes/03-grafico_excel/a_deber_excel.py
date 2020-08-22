# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:48:07 2020

@author: erick
"""


import pandas as pd
import os
import numpy as np
import sqlite3

path_guardado = "./data/artwork_data.pickle"

df =  pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()

# Excel
path_excel = "./data/artwork_data_excel.xlsx"

num_artistas = sub_df['artist'].value_counts()

writer = pd.ExcelWriter(path_excel,engine='xlsxwriter')

num_artistas.to_excel(writer,sheet_name='Artista')
workbook = writer.book
worksheet = writer.sheets['Artista']

chart = workbook.add_chart({'type': 'column','name':'Artista'})
chart.add_series({
    'name': '=Artista!B1',
    'values':     '=Artista!$B$2:$B$30',
    'categories': '=Artista!$A$2:$A$30',
    'gap':        30,
    'data_labels': {'value': True}
})
chart.set_title({'name': 'Numero de obras por artista'})
chart.set_legend({'none': True})
chart.set_style(4)
chart.set_x_axis({
    'name': 'Artistas',
    'num_font': {
        'name': 'Arial',
        'color': '#00B0F0',
    },
})

chart.set_y_axis({
    'name': 'Cantidad',
    'num_font': {
        'name': 'Arial',
        'color': '#7030A0',
    },
})
worksheet.insert_chart('D2', chart, {'x_scale': 2.0, 'y_scale': 2.0})
writer.save()