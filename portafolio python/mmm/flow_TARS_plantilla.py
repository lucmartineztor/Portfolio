import tarsConstruct
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
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import numpy as np
import calendar
import pandas as pd
from os import remove
from datetime import date
import datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import csv

__file__ = os.path.abspath(__file__)
path = os.path.dirname(__file__)
mainpath = os.path.split(path)
sys.path.append(mainpath[0])



def selenium(browser,downloadpath):
	

	'''
	Descarga de crudos de Flow.ia

	[PROCESO]

	1. 	Ingreso a la pagina:
		Ingreso a la pagina de flow.ai con credenciales de Flow.ai-Transversal
	
	2.	Seleccion de filtros:
		Consiste en seleccionar los filtros correspondiente  para las campañas TP Latam- CO-DEMOS, Doordash,Doordash DX, AT&T, Enigma y Redbubble con sus respectivas
		subcampañas.La información debe descargarse a día vencido, filtrando -2 días  y día en curso, Deben descargarse dos datas, en la pestaña export y export legacy.

	3.	Export de data
		Para exportar la data legacy y la data export, se ingresan las fechas y se solicita la exportacion de ambos datos,
		luego se actualiza la pagina, se obtienen elementos by class por medio de find_elements_by_xpath luego se realiza un ciclo para dar click a los 2 ultimos elementos
		Se verifica la descarga y se buscan los archivos que son relevantes de cada zip (Export = Brain_events,  Export legacy = Users)
		finalmente se mueven a la ruta y se termina el RPA



	[RAISE]

		1. En caso de que algun archivo no se encuentre en el zip
		2. en caso de que se modifique la ubicacion de algun elemento en la pagina2
		3. Si no se remueve el archivo descargado, se puede generar un error de consistencia



	[METODOS]
	1. def carga():

		seleccion de filtros de acuerdo a campañas y fechas y descarga de los archivos a sus rutas correspondientes

	

	'''


	###############################

	#Ingreso a la pagina 

	###############################

	browser.get('https://app.flow.ai/analytics/report')

	wait = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID,'1-email')))

	tarsConstruct.app_login(app=browser,credentials_services=['Flow.ai-Transversal'],usernamefield_id='1-email',passwordfield_name='password')
	browser.find_element_by_name('submit').click()
	
	########################################
	#METODOS
	#######################################

	def carga(browser,downloadpath,rutaBrain, rutaUser, campanna, subcampanna,today,yesterday,nombre):
		print(nombre)

		'''

		[SUMMARY]
		
		Metodo para seleccion de filtros de acuerdo a la campaña (con sus respectivas fechas), la descarga de los archivos .zip y cambio de ruta de los archivos User.csv y brain_events.csv
		a las especificadas para cada caso
		

		[Args]
			browser(webdriver): Elemento del webdriver
			downloadpath: ruta de envio de tars por defecto
			rutaBrain(str) : ruta de envio de archivo brain_events.csv
			rutaUser: ruta de envio de archivo user.csv
			campanna(str): nombre del filtro en html de la campaña (filtro)
			subcampanna(str): nombre del filtro  en html de la sucampaña (filtro)
			today(date), yesterday(date): fechas que el filtro debe seleccionar
			nombre(str): nombre de la campaña
		
		[RAISE]
			1.Cambios en la configuracion de la pagina
			2.Tiempo de carga que exceda lo esperado
			3.Cambios en el nombre o la esctuctura de los archivos brain_events.csv y user.csv
			4.Cambios en los permisos o nombres de las rutas
			
		'''

		###################################

		#Seleccion de filtros

		###################################

		WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.CLASS_NAME,"Active_organisationName__1ujPh"))).click()
		sleep(2)


		WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH,'//div[contains(text(),'+str(campanna)+')]'))).click()
		WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.CLASS_NAME,'Active_agentName__ilsUt'))).click()
		WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH,'//div[contains(text(),'+str(subcampanna)+')]'))).click()

		sleep(5)
		WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH,'//div[contains(text(),"Analytics Beta")]'))).click()
		sleep(5)
		WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH,'//a[contains(text(),"Export")]'))).click()
		sleep(5)
		WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div/section[2]/div/main[2]/div/div[3]/div[1]/div[1]/div[2]/div'))).click()
		sleep(5)
		WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[2]/div[1]/div'))).click()
		WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div/section[2]/div/main[2]/div/div[3]/div[2]/div[2]/div'))).click()
		WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH,'//option[@value="custom"]'))).click()
		sleep(5)
		date = yesterday.strftime("%m/%d/%Y")+today.strftime("%m/%d/%Y")
		print (date) 
		WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.ID,'startDate'))).send_keys(date)
		sleep(5)
		WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH,'//*[contains(text(),"export legacy")]'))).click()
		sleep(5)
		WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div/section[2]/div/main[2]/div/div[3]/div[2]/div[2]/div'))).click()
		sleep(5)
		WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div[6]/div[2]/div[2]/div'))).click() 
		sleep(20)
		browser.refresh()
		sleep(5)
		Datedowload = today.strftime('%d%m%Y%H%M%p')
		sleep(5)
		downloads = browser.find_elements_by_xpath("//div[@class='Button_button__1Z21W Export_buttonBody__1TA4x']")
		print(len(downloads))


		#################################

		#Export de data

		################################

		for elem in range(len(downloads)-2,len(downloads)):
			downloads[elem].click()
			sleep(10)
			filename = tarsConstruct.file_download_verify(downloadpath)
			with ZipFile(filename, 'r') as zipObj:
			# Get a list of all archived file names from the zip
				listOfFileNames = zipObj.namelist()
				print(listOfFileNames)
				# Iterate over the file names
				for fileName in listOfFileNames:
				# Check filename endswith csvS
					if fileName == 'brain_events.csv':
						zipObj.extract(fileName, downloadpath)
						sleep(10)
						print(fileName+ " extraido en: "+downloadpath)
						sleep(5)
						
						try:
							read_file = pd.read_csv(os.path.join(downloadpath,fileName) , sep="\t",error_bad_lines=False, quoting=csv.QUOTE_NONE,engine="python")
							read_file.to_csv(rutaBrain+'\\'+nombre+'_'+Datedowload+'_'+fileName, index = False, sep = ',') 
							sleep(5)
							zipObj.close()
						except:
							print('Archivo vacio')
							logging.info('archivo vacio')

						#print(fileName+" Movido a : "+rutaBrain)
						os.remove(downloadpath+'\\'+fileName)                  
					
					if fileName == 'Users.csv':
						zipObj.extract(fileName, downloadpath)
						sleep(10)
						print(fileName+ " extraido en: "+downloadpath)
						sleep(5)

						try:
							read_file2 = pd.read_csv(os.path.join(downloadpath,fileName) , sep="\t",error_bad_lines=False, quoting=csv.QUOTE_NONE,engine="python") 
							read_file2.to_csv(rutaUser+'\\'+nombre+'_'+Datedowload+'_'+fileName, index = False, sep = ',')
							sleep(5)
							zipObj.close()
						except:
							print('Archivo vacio')
							logging.info('archivo vacio')
						os.remove(downloadpath+'\\'+fileName)
				
				try:
					#print(fileName+" Movido a : "+rutaUser)
					os.remove(filename)
					print(filename + " Removido")
					filename=""
				except:
					print('Error al eliminar el archivo')
					logging.info('Error al eliminar el archivo')
				sleep(5)
	
	###################################
	#VARIABLES DE CONFIGURACION
	##################################

	today = datetime.date.today() + datetime.timedelta(days=1)
	yesterday = datetime.date.today() - datetime.timedelta(days=1)
	Saturday= datetime.date.today() - datetime.timedelta(days=9)
	

	ruta_brain_doordash = r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\Doordash\Brain_Events'
	ruta_user_doordash = r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\Doordash\Users'
	nombre_doordash = 'Doordash'

	ruta_brain_doordash_DX = r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\Doordash DX\Brain_Events'
	ruta_user_doordash_DX = r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\Doordash DX\Users'
	nombre_doordash_DX = 'Doordash_DX'

	ruta_brain_RedBubble=r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\Redbubble\Brain_Events'
	ruta_user_RedBubble=r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\Redbubble\Users'
	nombre_RedBubble='Redbubble'

	ruta_brain_SUFI=r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\SUFI\Brain_Events'
	ruta_user_SUFI= r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\SUFI\Users'
	nombre_SUFI ='SUFI'

	ruta_brain_AT=r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\AT&T\Brain_Events'
	ruta_user_AT=r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\AT&T\Users'
	nombre_AT = 'AT&T'

	ruta_brain_Enigma=r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\Enigma\Brain_Events'
	ruta_user_Enigma=r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\Enigma\Users'
	nombre_Enigma = 'Enigma'

	try:
		carga(browser,downloadpath,ruta_brain_Enigma,ruta_user_Enigma,'"TP-MAR-COL-PD-Enigma"', '"TP-MAR-COL-PD-Enigma"',today,yesterday,nombre_Enigma)
	except:
		pass
	try:
		carga(browser,downloadpath,ruta_brain_doordash_DX,ruta_user_doordash_DX,'"TP-MAR-COL-PD-DX DOORDASH"', '"TP-MAR-COL-PD-DX DOORDASH"',today,yesterday,nombre_doordash_DX)
	except:
		pass
	try:
		carga(browser,downloadpath,ruta_brain_doordash,ruta_user_doordash,'"TP-MAR-COL-PD-DOORDASH"', '"TP-MAR-COL-PD-DOORDASH"',today,yesterday,nombre_doordash)
	except:
		pass
	try:
		carga(browser,downloadpath,ruta_brain_RedBubble, ruta_user_RedBubble,'"TP-MAR-COL-PD-RedBubble"', '"TP-MAR-COL-PD-RedBubble"',today,yesterday,nombre_RedBubble)
	except:
		pass

	try:
		carga(browser,downloadpath,ruta_brain_SUFI,ruta_user_SUFI,'"TP-LATAM-CO-DEMOS"', '"POC SUFI"',today,yesterday,nombre_SUFI)
	except:
		pass
	if date.today().weekday() == 0:
		try:
			carga(browser,downloadpath,ruta_brain_AT,ruta_user_AT,'"TP-MAR-COL-PD-AT&T"', '"TP-MAR-COL-PD-AT&T"',yesterday,Saturday,nombre_AT)
		except:
			pass
	#browser.close()


if __name__ == '__main__':
	service = tarsConstruct.TARS_Service(filepath=__file__)
	#service.options.headless= False
	service.run_service(func = selenium)