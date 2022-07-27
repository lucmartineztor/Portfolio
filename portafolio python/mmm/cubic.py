from datetime import datetime
import pandas as pd
import tarsConstruct_debugs_
#import tarsConstruct
import logging 
from sqlalchemy.types import String
import sys
import zipfile
from os import remove
import os
import numpy as np
import urllib
import traceback
from sqlalchemy import create_engine
import tarsConstruct_debugs



sql_user = 'usrTPTARS'
sql_pw= 'bQyi8*E1fzCW'
token= 'f23bda4a9ecb63d93d08d06e49bc46a0420c50ab60aacf85ca'

df = pd.read_excel(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.xlsx")

columnas_total = ["Cód. Identificador"
                            ,"Identificador 1"
                            ,"Identificador 2"
                            ,"Cód. Sistema"
                            ,"Ref. Principal"
                            ,"Modelo"
                            ,"Proveedor"
                            ,"Descripción"
                            ,"Nombre Ubicación"
                            ,"Documento"
                            ,"Responsable"
                            ,"ID CCMS"
                            ,"Id Proceso"
                            ,"Tipo Proceso"
                            ,"Fecha Proceso"
                            ]

#df.insert(1,'Fecha de carga',datetime.now().strftime('%Y-%m-%d'))
#print(df.columns.values)
for item in columnas_total:
    if item in df.columns:
        print("dataframe already contains: "+item)
    else:
        print("adding empty col: "+item)
        df[item] = '-'

df = df.astype('str')
# for columna in range(len(df["ID CCMS"])):
#     df["ID CCMS"][columna]=df["ID CCMS"][columna].strip(".0")
#     df["Id Proceso"][columna]=df["Id Proceso"][columna].strip(".0")
#     df["Documento"][columna]=df["Documento"][columna].strip(".0")
# for i in df.columns:
#         df[i]=df[i].replace('nan',' ',regex=True)


#tarsConstruct_debugs.send_df_to_sql_139(df, sql_user = sql_user, sql_pw = sql_pw, database = 'ActivosOperaciones',tlname = 'Table_1', server = 'TPCCP-DB141\SQL2016STD', schema = 'dbo', if_exists = 'replace', index=None, dtype = None)

#tarsConstruct_debugs.send_df_to_sql_139(df, sql_user = sql_user, sql_pw = sql_pw, database = 'ActivosOperaciones',tlname = 'Table_1', server = 'TPCCP-DB139\SQL2016STD', schema = 'dbo', if_exists = 'append', index=None, dtype = None)

tarsConstruct_debugs_.send_df_to_sql(dataframe=df, tlname='tbMovimientoActivosOperaciones',database='ActivosOperaciones', schema='dbo',server='TPCCP-DB141.teleperformance.co\SQL2016STD', if_exists='replace',credentials_services=['tars_DB141'], request_token=token)

from os import remove
#remove(r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.xlsx")
#remove(r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.csv")
