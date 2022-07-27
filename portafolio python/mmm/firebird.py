import firebirdsql
import pyodbc
from sqlalchemy import create_engine
import pandas as pd
import urllib
from datetime import datetime, timedelta
import os
import sys

import os.path

import shutil
import fdb

from datetime import datetime


__file__ = os.path.abspath(__file__)
path = os.path.dirname(__file__)
mainpath = os.path.split(path)
sys.path.append(mainpath[0])




fdb.load_api(r'C:/Users/martineztorres.55/Desktop/mios/nnn/fbclient.dll')


token='1a06c9082d19d593cba0c052cd9fcdbaa1355ac898dde9d8d3'

columns=['fecharealizacionexamen',
	'apellidosynombres',
    'identificacion',
    'cargo',
    'edad',
    'tipodeexamen',
    'tipodecertificado',
    'empresa',
    'concepto',
    'concepto2',
    'concepto3',
    'cie10_1',
    'diag_1',
    'cie10_2',
    'diag_2',
    'cie10_3',
    'diag_3',
    'cie10_4',
    'diag_4',
    'cie10_5',
    'diag_5',
    'antecedente_per_patologico',
    'antecedente_per_hospitalario',
    'antecedente_per_quirurgico',
    'antecedente_per_traumatico',
    'antecedente_per_alergico',
    'antecedente_per_toxicoalergico',
    'antecedente_per_farmacologico',
    'antecedente_per_psiquiatrico',
    'antecedente_per_inmunologico'
	]
engine = create_engine("firebird+fdb://USTELCTA:C0nsult4SMSI202@190.0.18.123:3050/D:/SIMEDI/BASE/ConTelCS.FDB",encoding="utf-8")

conn = engine.connect()

print('Conectando con firebird')

DiaAyer = (datetime.now()- timedelta(days=1)).strftime('%Y/%m/%d')

sql_user = 'usrTPTARS'
sql_pw = 'bQyi8*E1fzCW' 

def connect_firebird(DiaAyer=DiaAyer):
    try:
    	element=[]
    	conn = engine.connect()
    	#connection= conn.execute("SELECT * FROM CTACONSALUD('2016/10/13', '2022/01/11')" )
    	
    	connection= conn.execute("SELECT * FROM CTACONSALUD('"+DiaAyer+"','"+DiaAyer+"')")
    	for c in connection:
    		element.append(c)
    		
    	df=pd.DataFrame(element,columns=columns)
    	df=df.astype(str)
    	df.to_excel(r'\\10.151.230.78\Dropbox\Transversal\Proyectos\SST\San Ignacio\\firebird.xlsx',index=False)

    	conn.close()


    except Exception as e:
    	print(e)
    	print('Error sending data to sql')

    send_df_to_sql_139(df, sql_user = sql_user, sql_pw = sql_pw, database = 'BaseSalud2',tlname = 'tbSanIgnacio', server = 'TPCCP-DB139\SQL2016STD', schema = 'dbo', if_exists = 'append', index=None, dtype = None)
    #send_df_to_sql_139(df, sql_user = sql_user, sql_pw = sql_pw, database = 'BaseSalud2',tlname = 'tbSanIgnacio', server = 'TPCCP-DB139\SQL2016STD', schema = 'dbo', if_exists = 'replace', index=None, dtype = None)

def send_df_to_sql_139(dataframe, sql_user, sql_pw, database, tlname, server ,schema,if_exists, index,dtype ):

    tsql_chunksize = 2097 // len(dataframe.columns)
    tsql_chunksize = 1000 if tsql_chunksize > 1000 else tsql_chunksize

    print('SENDING TO DATABASE')
    params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"

                                        "SERVER="+server+";"

                                        "DATABASE="+database+";"

                                        "Trusted_Connection=yes;"

                                        "UID="+sql_user+";"

                                        "PWD="+sql_pw+";"

                                        )

    

    try:
        engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params), encoding="utf-8")
        dataframe.to_sql(name=tlname, schema=schema, if_exists=if_exists, con=engine,
                     index=index, chunksize=tsql_chunksize, dtype=dtype, method='multi')
        engine.dispose()


    except Exception as e:

        traceback.format_exc(e)

        print('Error sending data to sql')




#Eliminar si se consigue un servidor donde se pueda ejecutar diariamente


connect_firebird(DiaAyer)


import holidays_co

DiaAyer = (datetime.now()- timedelta(days=1)).strftime('%Y-%m-%d')
DiaAyer = DiaAyer.split('-')
year=int(DiaAyer[0])

holidays = holidays_co.get_colombia_holidays_by_year(year)

x=[]



for i in holidays:
    x.append(i[0].strftime('%Y-%m-%d'))

if datetime.today().weekday() == 0:
    connect_firebird(DiaAyer = (datetime.now()- timedelta(days=2)).strftime('%Y/%m/%d'))
    connect_firebird(DiaAyer = (datetime.now()- timedelta(days=3)).strftime('%Y/%m/%d'))
    #connect_firebird(DiaAyer = (datetime.now()- timedelta(days=3)).strftime('%Y/%m/%d'))

elif datetime.today().weekday() == 1 and (datetime.now()- timedelta(days=1)).strftime('%Y-%m-%d') in x:
    connect_firebird(DiaAyer = (datetime.now()- timedelta(days=2)).strftime('%Y/%m/%d'))
    connect_firebird(DiaAyer = (datetime.now()- timedelta(days=3)).strftime('%Y/%m/%d'))
    connect_firebird(DiaAyer = (datetime.now()- timedelta(days=4)).strftime('%Y/%m/%d'))

elif datetime.today().weekday() != 1 and (datetime.now()- timedelta(days=1)).strftime('%Y-%m-%d') in x:
    connect_firebird(DiaAyer = (datetime.now()- timedelta(days=2)).strftime('%Y/%m/%d'))

else: pass
