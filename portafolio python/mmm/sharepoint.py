from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File 
import io
import pandas as pd
import openpyxl 
import tarsConstruct_debugs_

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



sql_user = 'usrTPTARS'
sql_pw = 'bQyi8*E1fzCW' 


client_id='martineztorres.55@nlsa.teleperformance.com'
client_secret= 'Admin2021*'
url='https://teleperformance.sharepoint.com/sites/StockActivos-Forecast/Shared%20Documents/General/Actualizaci%C3%B3n%20Forecast/Usuarios%20Forecast%202021l.xlsx?web=1'

ctx_auth = AuthenticationContext(url)
if ctx_auth.acquire_token_for_user(client_id,client_secret):
  ctx = ClientContext(url, ctx_auth)
  web = ctx.web
  ctx.load(web)
  ctx.execute_query()
  print("Authentication successful")

response = File.open_binary(ctx, url)


# # #save data to BytesIO stream

bytes_file_obj = io.BytesIO()
bytes_file_obj.write(response.content)
bytes_file_obj.seek(0) #set file object to start

df = pd.read_excel(bytes_file_obj,sheet_name = None)


df = df['Forecast']
df.to_excel('sdffdfgdf.xlsx',index = False, header=False)
df = pd.read_excel('sdffdfgdf.xlsx')
for i in df.columns:
    df[i]=df[i].replace('nan',' ',regex=True)


#df["Efectividad ejecucion"]=df["Efectividad ejecucion"].replace(np.nan,-999)



df = df.astype('str')


# for columna in range(len(df["Margen Error"])):
# 	digitos=len(df["Margen Error"][columna])
# 	try:
# 		df["Margen Error"][columna]=df["Margen Error"][columna].strip('.0')
# 	except:
# 		pass
# 	if len(df["Margen Error"][columna])==digitos-4:
# 		df["Margen Error"][columna]=df["Margen Error"][columna]+'00'
# 	df["Indicador Eficiencia Proveedores"][columna]=df["Indicador Eficiencia Proveedores"][columna].strip(".0")

# 	df["Efectividad ejecucion"][columna]=int(float(df["Efectividad ejecucion"][columna]))






send_df_to_sql_141(df, sql_user = sql_user, sql_pw = sql_pw, database = 'LogisticsScorecard',tlname = 'tbForecast', server = 'TPCCP-DB04\SCBACK', schema = 'dbo', if_exists = 'append', index=None, dtype = None)

#token= 'e6c95dd2e4639e1c0fa27b1701a627e374d9a4ebc22dba2eb8'
#tarsConstruct_debugs_.send_df_to_sql(dataframe=df, tlname='Forecast',database='LogisticsScorecard', schema='dbo',server='TPCCP-DB04\SCBACK',if_exists='replace',credentials_services=['tars_db139'],request_token=token)
