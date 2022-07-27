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
import tarsConstruct_debugs
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



options=Options()

options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe' 
#options.binary_location = r'C:\Users\martineztorres.55\AppData\Local\Mozilla Firefox\firefox.exe'
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True 

#downloadpath = r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\Doordash'
#downloadpath = r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\Redbubble'
downloadpath = r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\SUFI'

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
token = '82e99ea2307ff0f22b128ca7f4dffd0db178aee7b69ecc7b70'

def selenium():


	browser.get('https://app.flow.ai/analytics/report')

	wait = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.ID,'1-email')))

	tarsConstruct_debugs.app_login(app=browser,credentials_services=['Flow.ai-Transversal'],usernamefield_id='1-email',passwordfield_name='password',request_token=token)
	browser.find_element_by_name('submit').click()
	def carga(rutaBrain, rutaUser, campanna, subcampanna,today,yesterday,nombre):
		print(nombre)


		### ------------------
		# Inicio de sesion


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
		sleep(20)
		downloads = browser.find_elements_by_xpath("//div[@class='Button_button__1Z21W Export_buttonBody__1TA4x']")
		print(len(downloads))
		for elem in range(len(downloads)-2,len(downloads)):
			downloads[elem].click()
			sleep(10)
			filename = tarsConstruct_debugs.file_download_verify(downloadpath)
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
							read_file2 = pd.read_csv(os.path.join(downloadpath,fileName) , sep="\t",error_bad_lines=False,quoting=csv.QUOTE_NONE,engine="python") 
							read_file2.to_csv(rutaUser+'\\'+nombre+'_'+Datedowload+'_'+fileName, index = False, sep = ',')
							sleep(5)
							zipObj.close()
						except:
							print('Archivo vacio')
							logging.info('archivo vacio')
						os.remove(downloadpath+'\\'+fileName)

				try:
					#print(fileName+" Movido a : "+rutaUser)
					zipObj.close()
					os.remove(filename)
					print(filename + " Removido")
					filename=""
				except:
					print('Error al eliminar el archivo')
					logging.info('Error al eliminar el archivo')
				sleep(5)
	today = datetime.date.today()+ datetime.timedelta(days=1)
	yesterday = datetime.date.today() - datetime.timedelta(days=1)
	Saturday= datetime.date.today() - datetime.timedelta(days=9)
	#lastSunday = datetime.date.today() - datetime.timedelta(days=1)
	
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
		carga(ruta_brain_Enigma,ruta_user_Enigma,'"TP-MAR-COL-PD-Enigma"', '"TP-MAR-COL-PD-Enigma"',today,yesterday,nombre_Enigma)
	except:
		pass
	try:
		carga(ruta_brain_doordash,ruta_user_doordash,'"TP-MAR-COL-PD-DOORDASH"', '"TP-MAR-COL-PD-DOORDASH"',today,yesterday,nombre_doordash)
	except:
		pass
	try:
		carga(ruta_brain_doordash_DX,ruta_user_doordash_DX,'"TP-MAR-COL-PD-DX DOORDASH"', '"TP-MAR-COL-PD-DX DOORDASH"',today,yesterday,nombre_doordash_DX)
	except:
		pass
	try:
		carga(ruta_brain_RedBubble, ruta_user_RedBubble,'"TP-MAR-COL-PD-RedBubble"', '"TP-MAR-COL-PD-RedBubble"',today,yesterday,nombre_RedBubble)
	except:
		pass

	try:
		carga(ruta_brain_SUFI,ruta_user_SUFI,'"TP-LATAM-CO-DEMOS"', '"POC SUFI"',today,yesterday,nombre_SUFI)
	except:
		pass

	if date.today().weekday() == 0:
		try:
			carga(ruta_brain_AT,ruta_user_AT,'"TP-MAR-COL-PD-AT&T"', '"TP-MAR-COL-PD-AT&T"',yesterday,Saturday,nombre_AT)
		except:
			pass	
	browser.close()
selenium()