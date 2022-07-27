import random
import os
import sys
import logging
from time import sleep
import shutil 
from datetime import date, time, datetime, timedelta
from zipfile import ZipFile
import zipfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import json
import tarsConstruct_debugs_
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import numpy as np
import calendar
import holidays_co
from os import remove
import pandas as pd
import win32com.client as win32
import win32api
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from sqlalchemy.types import String
import urllib
import traceback
from sqlalchemy import create_engine


options=Options()

options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe' 
#options.binary_location = r'C:\Users\martineztorres.55\AppData\Local\Mozilla Firefox\firefox.exe'
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True
#downloadpath=r'\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP' 
downloadpath = r'\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Nicaragua\\'
#downloadpath = r'\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Peru\\'

options.set_preference("browser.download.dir", downloadpath)
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/force-download, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet ,\
                                                                application/octet-stream doc xls pdf txt,\
                                                                text/csv,application/x-msexcel,\
                                                                application/excel,application/x-excel,\
                                                                application/vnd.ms-excel,\
                                                                image/png,image/jpeg,text/html,text/plain,text/csv,\
                                                                application/msword,application/xml,\
                                                                application/x-www-form-urlencoded,\
                                                                application/csv,\
                                                                text/tab-separated-values,\
                                                                application/ms-excel')

options.set_preference("browser.helperApps.neverAsk.openFile", 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet ,\
                                                                application/octet-stream doc xls pdf txt,\
                                                                text/csv,application/x-msexcel,\
                                                                application/excel,application/x-excel,\
                                                                application/vnd.ms-excel,\
                                                                image/png,image/jpeg,text/html,text/plain,text/csv,\
                                                                application/msword,application/xml,\
                                                                application/x-www-form-urlencoded,\
                                                                application/csv,\
                                                                text/tab-separated-values, \
                                                                application/ms-excel')
options.set_preference("browser.helperApps.alwaysAsk.force", False)
options.set_preference("browser.download.manager.useWindow", False)
options.set_preference("browser.download.manager.focusWhenStarting", False)
options.set_preference("browser.download.manager.showAlertOnComplete", False)
options.set_preference("browser.download.manager.closeWhenDone", True)
cap["marionette"] = True
browser = webdriver.Firefox(capabilities=cap, executable_path='C:\\Users\\martineztorres.55\\Desktop\\mios\\geckodriver.exe', options=options)

token = 'ab8df721df496ea8d4d98205567b99bac2c90e3a55cbbc6c1e'

def selenium(browser,downloadpath):

    #user='1020739867'
    #tokenpass='1020739867'
    browser.get('http://10.151.232.107/')
    print('Logging into the web site')
    #user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username"]')))
    #user_logging.click()
    #user_logging.send_keys(user) 
    #print('user setted')
    #user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="clave"]')))
    tarsConstruct_debugs_.app_login(app=browser,usernamefield_id='username',passwordfield_id='clave',credentials_services=['ActivosCubic'], request_token=token)
    user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-iniciar-sesion"]')))
    user_logging.click()
    
    link ='http://10.151.232.107/almalogix/scripts/reportes/rep00028.php?frm_id=1299'
    browser.get(link)
    
    user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cod_agencia"]')))
    user_logging.click()

    #user_logging.send_keys('100')
    user_logging.send_keys('301')
    #user_logging.send_keys('218')

    user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sec_operacion"]')))
    user_logging.click()

    #user_logging.send_keys('8')
    user_logging.send_keys('13')
    #user_logging.send_keys('12')

    user_logging.send_keys(Keys.TAB) 
    user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnbtnGenerarReporte"]')))
    user_logging.click()
    
    #sleep(1160)
    sleep(100)
    
    excel()
    #filename = file_download_verify(downpath)
    #path, name = os.path.split(filename)

    browser.quit()





def cubic():
    
    #df=pd.read_excel(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.xlsx")
    df = pd.read_excel(r"\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Nicaragua\ReporteUbicacionSerialesConResponsable.xlsx")
    #df = pd.read_excel(r"\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Peru\\ReporteUbicacionSerialesConResponsable.xlsx")
    
    df=df.rename(columns={'Cód. Identificador':'CodIdentificador',
        "Identificador 1":"Identificador1",
        "Identificador 2":"Identificador2",
        "Cód. Sistema":"CodSistema",
        "Ref. Principal":"RefPrincipal",
        "Descripción":"Descripcion",
        "Nombre Ubicación":"NombreUbicacion",
        "Documento": "IDCCMS",
        "ID CCMS":"Documento",
        #"ID CCMS":"IDCCMS",
        "Id Proceso":"IdProceso",
        "Tipo Proceso":"TipoProceso",
        "Fecha Proceso":"FechaProceso"
        }
        )
    columnas_total = ["CodIdentificador"
                              ,"Identificador1"
                              ,"Identificador2"
                              ,"CodSistema"
                              ,"RefPrincipal"
                              ,"Modelo"
                              ,"Proveedor"
                              ,"Descripcion"
                              ,"NombreUbicacion"
                              ,"Documento"
                              ,"Responsable"
                              ,"IDCCMS"
                              ,"IdProceso"
                              ,"TipoProceso"
                              ,"FechaProceso"
                              ]

    for item in columnas_total:
        if item in df.columns:
            print("dataframe already contains: "+item)
        else:
            print("adding empty col: "+item)
            df[item] = '-'

    df = df.astype('str')

    for columna in range(len(df["IDCCMS"])):
        digitos=len(df["IDCCMS"][columna])

        
        
        df["IDCCMS"][columna]=df["IDCCMS"][columna].strip(".0")     #Descomentar para Ncaragua y Peru
        if len(df["IDCCMS"][columna])==digitos-3:
            df["IDCCMS"][columna]=str(df["IDCCMS"][columna]+'0')
        if len(df["IDCCMS"][columna])==digitos-4:
            df["IDCCMS"][columna]=str(df["IDCCMS"][columna]+'00')
        if len(df["IDCCMS"][columna])==digitos-5:
            df["IDCCMS"][columna]=str(df["IDCCMS"][columna]+'000')
        if len(df["IDCCMS"][columna])==digitos-6:
            df["IDCCMS"][columna]=str(df["IDCCMS"][columna]+'0000')

        

        #print(df["IdProceso"][columna],df["Documento"][columna])
        digitos=len(df["IdProceso"][columna])
        df["IdProceso"][columna]=df["IdProceso"][columna].strip(".0")
        if len(df["IdProceso"][columna])==digitos-3:
            df["IdProceso"][columna]=str(df["IdProceso"][columna]+'0')
        if len(df["IdProceso"][columna])==digitos-4:
            df["IdProceso"][columna]=str(df["IdProceso"][columna]+'00')
        if len(df["IdProceso"][columna])==digitos-5:
            df["IdProceso"][columna]=str(df["IdProceso"][columna]+'000')
        if len(df["IdProceso"][columna])==digitos-6:
            df["IdProceso"][columna]=str(df["IdProceso"][columna]+'0000')
        

        digitos=len(df["Documento"][columna])
        df["Documento"][columna]=df["Documento"][columna].strip(".0")
        if len(df["Documento"][columna])==digitos-3:
            df["Documento"][columna]=str(df["Documento"][columna]+'0')
        if len(df["Documento"][columna])==digitos-4:
            df["Documento"][columna]=str(df["Documento"][columna]+'00')
        if len(df["Documento"][columna])==digitos-5:
            df["Documento"][columna]=str(df["Documento"][columna]+'000')

    
    for i in df.columns:
        df[i]=df[i].replace('nan',' ',regex=True)
    
    #tarsConstruct_debugs_.send_df_to_sql(dataframe=df, tlname='tbMovimientoActivosOperaciones',database='ActivosOperaciones', schema='dbo',server='TPCCP-DB139\SQL2016STD',if_exists='replace',credentials_services=['tars_db139'],request_token=token)
    tarsConstruct_debugs_.send_df_to_sql(dataframe=df, tlname='tbMovimientoActivosOperacionesNicaragua',database='ActivosOperaciones', schema='dbo',server='TPCCP-DB139\SQL2016STD',if_exists='replace',credentials_services=['tars_db139'],request_token=token)
    #tarsConstruct_debugs_.send_df_to_sql(dataframe=df, tlname='tbMovimientoActivosOperacionesPeru',database='ActivosOperaciones', schema='dbo',server='TPCCP-DB139\SQL2016STD',if_exists='replace',credentials_services=['tars_db139'],request_token=token)
    
    #remove(r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.xlsx")
    #remove(r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.csv")
    #remove(r"\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Nicaragua\\ReporteUbicacionSerialesConResponsable.xlsx")
    #remove(r"\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Nicaragua\\ReporteUbicacionSerialesConResponsable.csv")
    #remove(r"\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Peru\\ReporteUbicacionSerialesConResponsable.xlsx")
    #remove(r"\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Peru\\ReporteUbicacionSerialesConResponsable.csv")
    
    print('ok')
    browser.quit()

def excel():

    #df = pd.read_csv(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.csv",encoding='latin-1',low_memory=False)
    #df.to_excel(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.xlsx", index=False)
    df = pd.read_csv(r"\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Nicaragua\\ReporteUbicacionSerialesConResponsable.csv",encoding='latin-1',low_memory=False)
    #df=pd.read_csv(r"\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Peru\\ReporteUbicacionSerialesConResponsable.csv",encoding='latin-1',low_memory=False)
    df.to_excel(r"\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Nicaragua\\ReporteUbicacionSerialesConResponsable.xlsx", index=False)
    #df.to_excel(r"\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Peru\\ReporteUbicacionSerialesConResponsable.xlsx", index=False)
    
    try:
        #excelfile=r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.xlsx"
        excelfile = r"\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Nicaragua\\ReporteUbicacionSerialesConResponsable.xlsx"
        #excelfile = r"\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Peru\\ReporteUbicacionSerialesConResponsable.xlsx"
        visible = True
        excel = win32.DispatchEx('Excel.Application')
        excel.Interactive = False
        excel.Visible = False
        excel.ScreenUpdating = visible
        excel.DisplayAlerts = False#
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


#cubic()   
selenium(browser,downloadpath)
