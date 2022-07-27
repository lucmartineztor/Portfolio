import tarsConstruct
import os
import sys
import logging
from time import sleep
import shutil
from datetime import date, time, datetime, timedelta
import zipfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.firefox.options import Options
import numpy as np
import calendar
from zipfile import ZipFile
import zipfile
from os import remove


__file__ = os.path.abspath(__file__)
path = os.path.dirname(__file__)
mainpath = os.path.split(path)
sys.path.append(mainpath[0])


def selenium(browser, downloadpath):
	try:
		globaltime =  datetime.now()  #get the date of today
		dayvalue = globaltime.strftime('%Y-%m-%d')  #format of date
		dateM3 = globaltime - timedelta(days=1) #get date -3

		logging.info('Se ejecuto el codigo')
		browser.get('https://www.seadc.ccms.teleperformance.com/ccms-bin/home.pl')
		logging.info('Inicia Sesion')
		print('Inicia Sesion')
		webdriver = WebDriverWait(browser, 40).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="loginname"]')))
		sleep(1)
		token= 'b853fe7ef4bf125714c72dea8636d31d98f0679e4f46af0b98'
		tarsConstruct.app_login(app=browser,
			credentials_services=['CCMS Disney-Star'],usernamefield_xpath='//*[@id="loginname"]',passwordfield_xpath='//*[@id="password"]')
		

		DiaAyer = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
		sleep(10)
		browser.find_element_by_xpath('//*[@id="submit"]').click() 
		sleep(5)
		browser.find_element_by_xpath('/html/body/div[2]/div[2]').click() 
		sleep(2)
		browser.find_element_by_xpath('/html/body/div[1]/div[3]/ul[1]/li[4]/span').click() 
		sleep(2)
		browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[4]/ul[6]/li[5]/ul/li[4]/a').click() 
		sleep(2)
		browser.find_element_by_xpath('/html/body/div[5]/ul[3]/li[2]/a').click() 
		sleep(3)


		select = Select(browser.find_element_by_id('ui-monitor_widget_target_company_ident'))
		select.select_by_visible_text('Teleperformance BR Brazil')

		sleep(2)
		select = Select(browser.find_element_by_id('ui-monitor_widget_target_client_ident'))
		select.select_by_visible_text('Disney Streaming Services')

		sleep(2)

		select = Select(browser.find_element_by_id('ui-monitor_widget_monitor_ident'))


		#--------------------------- cambio de csv para descargar-------------------




		#select.select_by_visible_text('Quality Form Disney+ Tier 1 v1')
		#select.select_by_visible_text('Quality Form Disney+ Tier 2 v1')
		select.select_by_visible_text('SoMe Disney+ Quality Form v4')




		sleep(2)


		browser.find_element_by_xpath('/html/body/div[6]/form/fieldset[6]/div[1]/select/option[1]').click()
		sleep(2)
		browser.find_element_by_xpath('//*[@id="start_date"] ').clear()
		sleep(2)
		browser.find_element_by_xpath('//*[@id="start_date"] ').send_keys(DiaAyer)
		sleep(2)
		browser.find_element_by_xpath('//*[@id="end_date"] ').clear()
		sleep(2)
		browser.find_element_by_xpath('//*[@id="end_date"] ').send_keys(DiaAyer)
		sleep(2)
		browser.find_element_by_xpath('/html/body/div[6]/form/fieldset[7]/div/input').click()
		sleep(5)
		#browser.quit()

		sleep(10)
		logging.info('Finaliza proceso descarga reporte')
		
		#def send_csv():
		logging.info('Envio de csv a ruta')
		print('Envio CSV a rutA')
		
		print(downloadpath)
		downloadpath=downloadpath+'\\'
		print(downloadpath)
		#for i in os.listdir(r'\\10.151.230.78\dropbox\Nearshore\Disney+\Crudos\QA\\'):
			#if i.endswith('.csv'):
				#try:
					#remove(r'\\10.151.230.78\dropbox\Nearshore\Disney+\Crudos\QA\QA\\'+i)
				#except:
					#pass	

		#for i in os.listdir(r'\\10.151.230.78\dropbox\Nearshore\Disney+\Crudos\QAT2\\'):
			#if i.endswith('.csv'):
				#try:
					#remove(r'\\10.151.230.78\dropbox\Nearshore\Disney+\Crudos\QA\QAT2\\'+i)
				#except:
					#pass	

		for i in os.listdir(r'\\10.151.230.78\dropbox\Nearshore\Disney+\Crudos\QA\QASoMe\\'):
			if i.endswith('.csv'):
				try:
					remove(r'\\10.151.230.78\dropbox\Nearshore\Disney+\Crudos\QA\QASoMe\\'+i)
				except:
					pass	

		def send_csv():

			for i in  os.listdir(downloadpath):

				if 'form_data_export' in i and i.endswith('zip'):

					with ZipFile(downloadpath+i,'r') as zipObj:

						carpetas=zipObj.namelist()

						for file in carpetas:

							if 'rollup' in file:

								with zipObj.open(file) as zf, open(downloadpath+'rollup', 'wb') as f:

									shutil.copyfileobj(zf, f)

								os.rename(downloadpath+'rollup', downloadpath+'FormBr D.csv')
					

			#----------------------------cambio de ruta de envio csv--------------------------------------
			#shutil.move(downloadpath+'FormBr D.csv',r'\\10.151.230.78\\dropbox\\Nearshore\\Disney+\\Crudos\\QA\\') 
			#shutil.move(downloadpath+'FormBr D.csv',r'\\10.151.230.78\dropbox\Nearshore\Disney+\Crudos\QAT2\\') 
			shutil.move(downloadpath+'FormBr D.csv',r'\\10.151.230.78\dropbox\Nearshore\Disney+\Crudos\QA\QASoMe') 


			#----------------------- Stored Procedure ---------------------------
			#for i in os.listdir(r'\\10.151.230.78\\dropbox\\Nearshore\\Disney+\\Crudos\\QA\\'):
			#	if i.endswith('.csv'):
			#		tarsConstruct.spExec("[Disney].[dbo].[spImportQA_ColBR]", server='10.151.230.23\\scnear', credentials_services=['SCNEAR'])

			#for i in os.listdir(r'\\10.151.230.78\dropbox\Nearshore\Disney+\Crudos\QAT2\\'):
			#	if i.endswith('.csv'):
			#		tarsConstruct.spExec("[Disney].[dbo].[spImportQAT2]", server='10.151.230.23\\scnear', credentials_services=['SCNEAR'])

			for i in os.listdir(r'\\10.151.230.78\dropbox\Nearshore\Disney+\Crudos\QA\QASoMe\\'):
				if i.endswith('.csv'):
					tarsConstruct.spExec("[Disney].[dbo].[spImportQASoMe]", server='10.151.230.23\\scnear', credentials_services=['SCNEAR'])	
			browser.quit()
			sys.exit()



		send_csv()
	except Exception as e:
		print(e)
	

#----------------------- Stored Procedure ---------------------------


			

if __name__ == '__main__':
	#profilepath = path + '\\' + 'ds_DisneyPlus_Brazil_T1_v1'
	#profilepath = path + '\\' + 'ds_DisneyPlus_Brazil_T2_v1'
	profilepath = path + '\\' + 'ds_DisneyPlus_Brazil_SoMe'
	shutil.rmtree(profilepath, ignore_errors=True, onerror=None)
	service = tarsConstruct.TARS_Service(filepath=__file__)
	service.fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip; charset=utf-8")
	service.fp.set_preference("browser.helperApps.neverAsk.openFile","application/zip; charset=utf-8")
	service.run_service(func=selenium)