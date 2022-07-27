
import logging
import os
import sys
import pandas as pd
__file__ = os.path.abspath(__file__)
path = os.path.dirname(__file__)
mainpath = os.path.split(path)
sys.path.append(mainpath[0])
import win32com.client as win32
import win32api

from datetime import datetime
import pandas as pd
import tarsConstruct
import logging 
from sqlalchemy.types import String
import sys

from os import remove
import os
import numpy as np
from sqlalchemy import create_engine
from cryptography.fernet import Fernet
import urllib
import traceback


def send_df_to_sql_141(dataframe, sql_user, sql_pw, database, tlname, server ,schema,if_exists, index,dtype ):

    tsql_chunksize = 2097 // len(dataframe.columns)
    tsql_chunksize = 1000 if tsql_chunksize > 1000 else tsql_chunksize
    # f=Fernet(b'drKE9yGc9DGt3azQF0PN6C12VmBPEWTe34My9CSHb_Q=')
    # sql_user=f.decrypt(sql_user)
    # sql_user=sql_user.decode()
    # sql_pw=f.decrypt(sql_pw)
    # sql_pw = sql_pw.decode()
    print('SENDING TO DATABASE')
    params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"

                                        "SERVER="+server+";"

                                        "DATABASE="+database+";"

                                        "Trusted_Connection=yes;"

                                        "UID="+sql_user+";"

                                        "PWD="+sql_pw+";"

                                        "appname=send_df_to_sql_139")

    

    try:
        engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params), encoding="utf-8")
        dataframe.to_sql(name=tlname, schema=schema, if_exists=if_exists, con=engine,
                     index=index, chunksize=tsql_chunksize, dtype=dtype, method='multi')
        engine.dispose()


    except Exception as e:

        traceback.format_exc(e)

        print('Error sending data to sql')



def cubic():
  sql_user = 'usrTPTARS'
  sql_pw = 'bQyi8*E1fzCW' 
  #sql_user = b'gAAAAABhfFWZuvz2l9c2-d19ZVW8zFmtqUgr-aVs-3yLBmDpTFiJPbBTwRHlwIXrqRUAfHgJYSPqclSBYPSB1DNtm3L2S-epww=='
  #sql_pw= b'gAAAAABhfFWZ9mzbJvCB2g-LVV8Wxyjgv29xbHNKhTDgoKYAz8orvKdWv2NRYG7eN9nMb_zWHlega5cHnafN3Qn0AZqzppruvQ=='
  
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

  for item in columnas_total:
      if item in df.columns:
          print("dataframe already contains: "+item)
      else:
          print("adding empty col: "+item)
          df[item] = '-'

  df = df.astype('str')
  for columna in range(len(df["ID CCMS"])):
      df["ID CCMS"][columna]=df["ID CCMS"][columna].strip(".0")
      df["Id Proceso"][columna]=df["Id Proceso"][columna].strip(".0")
      df["Documento"][columna]=df["Documento"][columna].strip(".0")
  for i in df.columns:
          df[i]=df[i].replace('nan',' ',regex=True)


  send_df_to_sql_141(df, sql_user = sql_user, sql_pw = sql_pw, database = 'ActivosOperaciones',tlname = 'tbMovimientoActivosOperaciones', server = 'TPCCP-DB141\SQL2016STD', schema = 'dbo', if_exists = 'replace', index=None, dtype = None)

  from os import remove
  remove(r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.xlsx")
  remove(r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.csv")

def excel():
  df = pd.read_csv(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.csv",encoding='latin-1',low_memory=False)
  df.to_excel(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.xlsx", index=False)
  try:
      excelfile = r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.xlsx"
      visible = True
      excel = win32.DispatchEx('Excel.Application')
      excel.Interactive = False
      excel.Visible = False
      excel.ScreenUpdating = visible
      excel.DisplayAlerts = False
      workbook = excel.Workbooks.Open(excelfile)
      mainsheet= workbook.Worksheets('Sheet1')

      import openpyxl
      book = openpyxl.load_workbook(excelfile)
      sheet = book.worksheets[0]
    

      maxim=len(sheet['A'])
      print(maxim)
      lista  = mainsheet.Range('A1:A'+str(maxim))
      lista.TextToColumns( DataType=1, TextQualifier=1, ConsecutiveDelimiter=True,
      Tab=False, Semicolon=False, Comma=True, Space=False, Other=False)
      excel.ActiveWorkbook.Save()
      
  finally:
          excel.EnableEvents = True
          excel.ScreenUpdating = True
          excel.DisplayAlerts = True
          excel.ActiveWorkbook.Save()
          if visible == False:
            excel.Visible = not visible
          workbook.Close(False)
          excel.Quit()
  cubic()
#excel()
if __name__ == '__main__':
    service = tarsConstruct.TARS_Service(filepath=__file__)
    service.options.headless= False
    service.run_service(func = excel)