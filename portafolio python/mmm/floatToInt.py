from datetime import datetime
import pandas as pd
import tarsConstruct
import logging 
from sqlalchemy.types import String
import sys
import zipfile
from os import remove
import os
from datetime import datetime
import pandas as pd
import tarsConstruct
import logging 
from sqlalchemy.types import String
import sys

from os import remove
import os

#df = pd.read_excel('summary-COLE21X08408 Teledatos Taxi Jul-21.xlsx')

token='c4a6920c3624b03d8e3c63ef03971e35953287de00054a232f'
df = pd.read_excel('summary-COLE21Y02148 Nearshore Medellin Taxi Jul-21.xlsx')
# print(type(df['Código de empleado del pasajero'][0]),df['Código de empleado del pasajero'][0])
# df['Código de empleado del pasajero']=df['Código de empleado del pasajero'].fillna(int(0))
# for a in (df['Código de empleado del pasajero']):
# 	try:
# 		b=str(a).strip(".0")
# 		df['Código de empleado del pasajero'].replace(a,b.astype(str),regex=True)
# 		print(a, int(a))
# 	except:continue

#print(type(df['Código de empleado del pasajero'][0]),df['Código de empleado del pasajero'][0])

df = df.astype('str')
for i in range(len(df['Código de empleado del pasajero'])):
	df['Código de empleado del pasajero'][i]=str(df['Código de empleado del pasajero'][i]).strip(".0")
	df['Centro de coste del pasajero'][i]=df['Centro de coste del pasajero'][i].strip(".0")
	df['Centro de coste variable'][i]=df['Centro de coste variable'][i].strip(".0")

df.to_excel('fsdfsdf.xlsx')
#tarsConstruct.send_df_to_sql(df, tlname='Table_2', database='Sandbox', schema='dbo', if_exists='replace',credentials_services=['SQL-TPCCP-DB128'], request_token=token)