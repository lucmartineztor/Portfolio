import os
import datetime
import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from sqlalchemy import create_engine
import logging
import shutil
import pyotp
import sys
import win32com.client
__file__ = os.path.abspath(__file__)
path = os.path.dirname(__file__)
mainpath = os.path.split(path)
sys.path.append(mainpath[0])
import pandas as pd
import tarsConstruct
import win32com.client as win32
import win32api

from datetime import datetime
import pandas as pd
import logging 
from sqlalchemy.types import String
import sys

from os import remove
import os
import numpy as np
from sqlalchemy import create_engine
import urllib
import traceback


''' Webscrapping para la descarga de archivos csv para la cuenta de activos cubic Nicaragua y Peru'''

	
def selenium(browser,downpath):
	
	'''
	Inicio de sesion para la cuenta de activos cubic de Nicaragua o Peru, con las credenciales que se manejan en TARS y el posterior

	ingreso del numero de las cuentas para realizar la descarga del documento ReporteUbicacionSerialesConResponsable.csv para cada pais.

	Finamente se realiza el cambio de la ruta del archivo descargado a la url asignada

	'''

	#-------------------------------------------------------------------

	#Inicio de sesion

	#-------------------------------------------------------------------
	browser.get('http://10.151.232.107/')
	tarsConstruct.app_login(app=browser,usernamefield_id='username',passwordfield_id='clave',credentials_services=['ActivosCubic'])
	user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-iniciar-sesion"]')))
	user_logging.click()

	link ='http://10.151.232.107/almalogix/scripts/reportes/rep00028.php?frm_id=1299'
	browser.get(link)

	#----------------------------------------------------------------------

	#Ingreso de numero de cuenta para cada pais y descarga del archivo

	#----------------------------------------------------------------------

	user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cod_agencia"]')))
	user_logging.click()

	user_logging.send_keys('100')
	#user_logging.send_keys('301')
	#user_logging.send_keys('218')

	user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sec_operacion"]')))
	user_logging.click()

	user_logging.send_keys('8')
	#user_logging.send_keys('13')
	#user_logging.send_keys('12')

	user_logging.send_keys(Keys.TAB)
	time.sleep(5)
	user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnbtnGenerarReporte"]')))
	user_logging.click()

	time.sleep(1000)

	#-----------------------------------------------------------------

	#Envio del archivo a la ruta de descarga 

	#-----------------------------------------------------------------

	filename = tarsConstruct.file_download_verify(downpath)

	final_destiny = r'\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\\'
	#final_destiny = r'\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Nicaragua\\'
	#final_destiny = r'\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Peru\\'

	path, name = os.path.split(filename)
	shutil.move(filename,final_destiny+name)
	excel()
	browser.quit()



def cubic():

	'''

	Lectura y consumo del archivo ReporteUbicacionSerialesConResponsable.csv, con cambios en los nombres de las columnas

	y posterior eliminacion de archivos ReporteUbicacionSerialesConResponsable.csv y ReporteUbicacionSerialesConResponsable.xlsx


	'''

	#--------------------------------------------------------

	#Lectura del archivo

	#--------------------------------------------------------

	df=pd.read_excel(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.xlsx")
	#df = pd.read_excel(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\Nicaragua\\ReporteUbicacionSerialesConResponsable.xlsx")
	#df = pd.read_excel(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\Peru\\ReporteUbicacionSerialesConResponsable.xlsx")

	#--------------------------------------------------------------

	#Cambios de nombre de columnas

	#--------------------------------------------------------------

	df=df.rename(columns={'Cód. Identificador':'CodIdentificador',
		"Identificador 1":"Identificador1",
		"Identificador 2":"Identificador2",
		"Cód. Sistema":"CodSistema",
		"Ref. Principal":"RefPrincipal",
		"Descripción":"Descripcion",
		"Nombre Ubicación":"NombreUbicacion",
		#"Documento": "IDCCMS",
		#"ID CCMS":"Documento",
		"ID CCMS":"IDCCMS", #Para Peru, activar este y desactivar los dos anteriores
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

#-------------------------------------------------

#Limpieza de datos

#-------------------------------------------------

	df = df.astype('str')
	for columna in range(len(df["IDCCMS"])):
		digitos=len(df["IDCCMS"][columna])
		#df["IDCCMS"][columna]=df["IDCCMS"][columna].strip(".0")
		#if len(df["IDCCMS"][columna])==digitos-3:
		#	df["IDCCMS"][columna]=str(df["IDCCMS"][columna]+'0')
		#if len(df["IDCCMS"][columna])==digitos-4:
		#	df["IDCCMS"][columna]=str(df["IDCCMS"][columna]+'00')
		#if len(df["IDCCMS"][columna])==digitos-5:
		#	df["IDCCMS"][columna]=str(df["IDCCMS"][columna]+'000')
		#if len(df["IDCCMS"][columna])==digitos-6:
		#	df["IDCCMS"][columna]=str(df["IDCCMS"][columna]+'0000')

		digitos=len(df["IdProceso"][columna])
		df["IdProceso"][columna]=df["IdProceso"][columna].strip(".0")

		if len(df["IdProceso"][columna])==digitos-3:
			df["IdProceso"][columna]=str(df["IdProceso"][columna]+'0')
		if len(df["IdProceso"][columna])==digitos-4:
			df["IdProceso"][columna]=str(df["IdProceso"][columna]+'00')
		if len(df["IdProceso"][columna])==digitos-5:
			f["IdProceso"][columna]=str(df["IdProceso"][columna]+'000')
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

	#-------------------------------------------------------

	#Consumo de datos y eliminacion de archivos

	#-------------------------------------------------------

	tarsConstruct.send_df_to_sql(dataframe=df, tlname='tbMovimientoActivosOperaciones',database='ActivosOperaciones', schema='dbo',server='TPCCP-DB141\SQL2016STD', if_exists='replace',credentials_services=['tars_DB141'])
	#tarsConstruct.send_df_to_sql(dataframe=df, tlname='tbMovimientoActivosOperacionesNicaragua',database='ActivosOperaciones', schema='dbo',server='TPCCP-DB141\SQL2016STD', if_exists='replace',credentials_services=['tars_DB141'])
	#tarsConstruct.send_df_to_sql(dataframe=df, tlname='tbMovimientoActivosOperacionesPeru',database='ActivosOperaciones', schema='dbo',server='TPCCP-DB141\SQL2016STD', if_exists='replace',credentials_services=['tars_DB141'])


	remove(r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.xlsx")
	remove(r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.csv")
	#remove(r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\Nicaragua\\ReporteUbicacionSerialesConResponsable.xlsx")
	#remove(r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\Nicaragua\\ReporteUbicacionSerialesConResponsable.csv")
	#remove(r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\Peru\\ReporteUbicacionSerialesConResponsable.xlsx")
	#remove(r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\Peru\\ReporteUbicacionSerialesConResponsable.csv")


def excel():

	'''

	Paso del archivo .csv a .xlsx para cambiar su delimitacion por comas, a columnas 

	'''

	#-------------------------------------------------------

	#Lectura de .csv y creacion del archivo en formato a xlsx, en la misma ruta

	#-------------------------------------------------------
	df = pd.read_csv(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.csv",encoding='latin-1',low_memory=False)
	df.to_excel(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.xlsx", index=False)
	#df = pd.read_csv(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\Nicaragua\\ReporteUbicacionSerialesConResponsable.csv",encoding='latin-1',low_memory=False)
	#df.to_excel(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\Nicaragua\\ReporteUbicacionSerialesConResponsable.xlsx", index=False)
	#df = pd.read_csv(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\Peru\\ReporteUbicacionSerialesConResponsable.csv",encoding='latin-1',low_memory=False)
	#df.to_excel(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\Peru\\ReporteUbicacionSerialesConResponsable.xlsx", index=False)

#-----------------------------------------------

#Cambio de valores separados por coma a columnas

#-----------------------------------------------

	try:
		excelfile = r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.xlsx"
		#excelfile = r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\Nicaragua\\ReporteUbicacionSerialesConResponsable.xlsx"
		#excelfile = r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\Peru\\ReporteUbicacionSerialesConResponsable.xlsx"
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


if __name__ == '__main__':
	service = tarsConstruct.TARS_Service(filepath=__file__)
	#service.options.headless= False
	service.run_service(func = selenium)