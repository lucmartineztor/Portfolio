import firebirdsql
import fdb
import pyodbc
from sqlalchemy import create_engine
import pandas as pd
import urllib
from datetime import datetime, timedelta
import os
import sys

path = os.path.dirname(__file__)
mainpath = os.path.split(path)
sys.path.append(mainpath[0])
import tarsConstruct

def main():
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


    try:
        element=[]
        conn = engine.connect()
        #connection= conn.execute("SELECT * FROM CTACONSALUD('2016/10/13', '2022/01/05')" )
        connection= conn.execute("SELECT * FROM CTACONSALUD('"+DiaAyer+"','"+DiaAyer+"')")
        for c in connection:
            c=(c[0:30])
            #print(c)
            element.append(c)		
        df=pd.DataFrame(element,columns=columns)
        df=df.astype(str)
        df.to_excel(r'\\10.151.230.78\Dropbox\Transversal\Proyectos\SST\San Ignacio\\firebird.xlsx',index=False)
        conn.close()

    except Exception as e:
        print(e)
        print('Error sending data to sql')

    tarsConstruct.send_df_to_sql(dataframe=df, tlname='tbSanIgnacio',database='BaseSalud2', schema='dbo',server='TPCCP-DB139\SQL2016STD', if_exists='append',credentials_services=['cred_serv_139'])

if __name__ == '__main__':
    service = tarsConstruct.selenium_RPA(filepath=__file__)
    service.run_service(func=main)
