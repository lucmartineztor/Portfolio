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
downloadpath = r'C:\Users\martineztorres.55\Desktop\Nueva carpeta'
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

token = 'e6c95dd2e4639e1c0fa27b1701a627e374d9a4ebc22dba2eb8'

def selenium(browser,downloadpath):

	page_name='https://forms.office.com/Pages/DesignPage.aspx#Analysis=true&FormId=r8uPY0y64UOtrlR1yXD-EOn50H1e-4FKkF4025w0DTVUMEJPRlI3M1ZMWURJVjdaTzkxMllMWDQ2Vi4u&Token=4e889610cd2e4b5a96e3925bcb62f7a7'
	credentials=['tars_db139']


	def function(page_name:str):
		
		browser.get(page_name)
		print('Logging into the web site')
		sleep(10)
		browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
		#browser.find_element_by_xpath('/html/body/div[2]/div/main/div[2]/div[4]/input')
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/main/div[2]/div[2]/div/input')))
		#user_logging.click()
		#user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/main/div[2]/div[2]/div/input')))
		user_logging.send_keys('martineztorres.55@nlsa.teleperformance.com')
		browser.find_element_by_xpath('/html/body/div[2]/div/main/div[2]/div[4]/input').click()


		browser.switch_to.default_content()
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
		user_logging.send_keys('Admin2021*')
		browser.find_element_by_xpath('//*[@id="idSIButton9"]').click() 
		sleep(10)
		browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[10]/div/div/div/div[3]/div[2]/div/button').click()
		sleep(20)
	
	
	def pandas_(tlname, database,server,credentials_services):
		files=[]
		items = os.listdir(downloadpath)
		print(items)
		for i in items:	
			if 'TP Volunteer' in i:
				files.append(i)
		print(files)

		df1 = pd.read_excel(r'C:\Users\martineztorres.55\Desktop\Nueva carpeta\\'+files[0])
		#df1 = df1.assign(Eres_profesional='')
		#df1 = df1.assign(Cuál_es_tu_profesión='')
		#df1 = df1.rename(columns = {"Eres_profesional":"profesional",
			#"Cuál_es_tu_profesión": "profesion"})
		df2 = pd.read_excel('C:\\Users\\martineztorres.55\\Desktop\\Nueva carpeta\\'+files[1])
		#df2=  df2.rename(columns={'Name':'Nombre',"¿Eres profesional?":"profesional",
			#"¿Cuál es tu profesión?": "profesion"} )
	  #--------------------------------------------------------------

	  #Cambios de nombre de columnas

	  #--------------------------------------------------------------
		columns=[]
		for i in df1.columns:
			columns.append(i)
		values1 = df1[columns]
		print(columns)
		values2=df2[columns]
		# columns=[]
		# for i in df2.columns:
		# 	columns.append(i)
		# print(columns)
		dataframe=[values1, values2]
		df =pd.concat(dataframe)
		#print(df.duplicated())
		df=df.drop_duplicates()
		df=df.drop(['ID','Nombre','Correo electrónico'], axis=1)
		#df.to_excel(r'C:\Users\martineztorres.55\Desktop\Nueva carpeta\TP Volunteer.xlsx',index=False)
		df=df.rename(columns={'Hora de inicio':'HoraDeInicio',
		    "Hora de finalización":"HoraDeFinalizacion",
		    #"Correo electrónico":"CorreoElectronico",
		    "Nombre completo":"NombreCompleto",
		    "Cédula o identificación nacional":"CedulaOIdentificacionNacional",
		    "CCMS ID":"CCMSID",
		    "Correo electrónico2":"CorreoElectronico",
		    "País de residencia":"PaisDeResidencia",
		    "Ciudad de residencia":"CiudadDeResidencia",
		    "Dirección completa (incluir barrio, torre y apartamento)":"DireccionCompleta",
		    "Cargo (Agente, Supervisor, ACCM)":"Cargo",
		    "Celular- teléfono móvil":"NumeroContacto",
		    "¿Cuántos años/meses de experiencia tienes trabajando como voluntario?":"TiempoExperienciaVoluntariado",
		    "Cuál es el área en la que más te interesa trabajar en el voluntariado?":"AreaDeInteresVoluntariado",
		    "¿Te refirió algún voluntario de TP ?":"ReferidoDesdeTP?",
		    "Cédula del voluntario que te refirió":"CedulaDeQuienRefirio",
		    "Comentarios y sugerencias":"ComentariosSugerencias",
		    "¿Eres profesional?":"profesional",
			"¿Cuál es tu profesión?": "profesion"

		    }
		    )
		columnas_total = []
		print(df.columns)
		for i in df.columns:
			columnas_total.append(i)
		
		                          

		for item in columnas_total:
		    if item in df.columns:
		        print("dataframe already contains: "+item)
		    else:
		        print("adding empty col: "+item)
		        df[item] = '-'
		
		df = df.astype('str')

		for columna in range(len(df["CCMSID"])):
			try:
				#df["Edad"][columna]=df["Edad"][columna].strip(".0")
				df["Edad"][columna]=df["Edad"][columna].str.strip(".0")         
			except:
				pass

		for i in df.columns:
			df[i]=df[i].replace('nan',' ',regex=True)
		#df.to_excel(r'C:\Users\martineztorres.55\Desktop\Nueva carpeta\TP Volunteer().xlsx',index=False)

		
		tarsConstruct_debugs_.send_df_to_sql(dataframe=df, tlname=tlname,database=database, schema='dbo',server=server, if_exists='append',credentials_services=credentials_services, request_token=token)
		#remove('C:\\Users\\martineztorres.55\\Desktop\\Nueva carpeta\\'+files[0])
		#remove('C:\\Users\\martineztorres.55\\Desktop\\Nueva carpeta\\'+files[1])


	tlname='tbtpVoluntary'
	database='tpVoluntary'
	server='TPCCP-DB139.teleperformance.co\SQL2016STD'
	credentials_services=['tars_db139']
	function(page_name)
	pandas_(tlname, database,server,credentials_services)
selenium(browser,downloadpath)
browser.quit()
