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
from selenium.webdriver.common.action_chains import ActionChains


options=Options()

options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe' 
#options.binary_location = r'C:\Users\martineztorres.55\AppData\Local\Mozilla Firefox\firefox.exe'
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True


downloadpath = r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice InContact'
#downloadpath=r'\\10.151.230.78\dropbox\Nearshore\Sunrun\3.CRUDOS\Data_studio\Raw_Staff' 
#downloadpath=r'\\10.151.230.78\dropbox\Nearshore\Sunrun\3.CRUDOS\Data_studio\FCR'

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


token ='96e0ab606184887bf718d15d2fbebe794620621ed93618a1db'


# browser.get('https://datastudio.google.com/u/0/reporting/56d89c70-26e8-49e7-b33c-dabd3c60da9c/page/xnWBB/')
# print('Logging into the web site') 
# tarsConstruct_debugs_.app_login(app=browser,usernamefield_id='identifierId',credentials_services=['SunrunDS'], request_token=token)

# user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')))
# user_logging.click()
# sleep(5)


# tarsConstruct_debugs_.app_login(app=browser,usernamefield_id='okta-signin-username',passwordfield_id='okta-signin-password',credentials_services=['SunrunDS'], request_token=token)

# user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="okta-signin-submit"]')))
# user_logging.click()

# sleep(100)

# open_window_elem = browser.find_element_by_id('cdk-describedby-message-ecp-1-89')
# action = webdriver.common.action_chains.ActionChains(browser)
# action.move_to_element_with_offset(open_window_elem, 1, 1)
# action.click()
# action.perform()
def selenium(browser,downloadpath):
	browser.get('https://home-c16.incontact.com/inContact/Default.aspx?brandingProfile=na1')

	tarsConstruct_debugs_.app_login(app=browser,usernamefield_id='ctl00_BaseContent_msl_txtUsername',credentials_services=['SunrunIncontact'], request_token=token)
	user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_BaseContent_btnNext"]')))
	user_logging.click()
	sleep(5)
	tarsConstruct_debugs_.app_login(app=browser,passwordfield_id='mfaPassField',credentials_services=['SunrunIncontact'], request_token=token)


	user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mfaLoginBtn"]')))
	user_logging.click()
	sleep(15)

	user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/app-root/app-home/div/cxone-header/header/div[1]/div/cxone-svg-sprite-icon')))
	user_logging.click()


	user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/app-root/app-home/div/cxone-header/cxone-app-picker/div[1]/div/div[2]/div[4]/div/div[3]/div/span')))
	user_logging.click()

	sleep(15)

	def PreDesigned():



		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/main/cxone-sidebar/div/div/div[2]/div[1]/a/span')))
		user_logging.click()

		sleep(15)

		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/main/div/ui-view-ng-upgrade/ui-view/app-reporting/div/div[2]/div/cxone-grid/div/ag-grid-angular/div/div[2]/div[1]/div[3]/div[2]/div/div/div[4]/div[2]')))
		user_logging.click()

		sleep(15)

		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_ctl00_BaseContent_ReportOptions_ctrlDatePicker_txtDate"]')))
		user_logging.click()

		sleep(5)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/ul/li[2]')))
		user_logging.click()

		sleep(5)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_ctl00_BaseContent_ReportContent_collapsibleOptions_ctl05_Label1"]')))
		user_logging.click()


		sleep(5)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_ctl00_BaseContent_ReportContent_collapsibleOptions_ctl07_ParametersControl_TeamMultiSelect_msTeams_btnAddItem"]')))
		user_logging.click()

		sleep(5)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div[1]/div/div[1]/div[1]/input'))).send_keys('TP')

		sleep(5)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div[1]/div/div[3]/div[2]/div/button[3]')))
		user_logging.click()

		sleep(5)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div[1]/div/div[6]/div[2]/button[1]')))
		user_logging.click()


		sleep(12)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_ctl00_BaseContent_ReportOptions_btnRunReport_ShadowButton"]')))
		user_logging.click()
		sleep(8)

		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_ctl00_BaseContent_ReportContent_reportViewerControl_ctl05_ctl04_ctl00_ButtonImg"]')))
		user_logging.click()

		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/div[4]/div/div/div/div/div[3]/div[2]/div/div[2]/div/span/div/table/tbody/tr[4]/td/div/div/div[3]/table/tbody/tr/td/div[2]/div[1]/a')))
		user_logging.click()


		DiaAyer = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
		DiaAyer = DiaAyer.split('-')
		DiaAyer = str(DiaAyer[1]+DiaAyer[2]+DiaAyer[0])

		sleep(10)

		for i in  os.listdir(downloadpath):
			if 'IC_Reports_AgentSummary.xlsx' in i:
				items = downloadpath+'\\'+i
				print(i)
				
				nombre_nuevo =items[:-5]+'_'+str(DiaAyer)+'.xlsx'
				try:
					remove(nombre_nuevo)
				except: 
					pass
				os.rename(items, nombre_nuevo)
				try:
					remove(archivo)
				except:
					pass
		print('termino funcion PreDesigned')


	def ModelosInforme(valor):
		sleep(10)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ReportTemplateList"]')))
		user_logging.click()
		try:
			user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_ManagerContent_agvsReportTemplates_btnClearSearch"]')))
			user_logging.click()
		except:
			pass
		sleep(15)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_ManagerContent_agvsReportTemplates_tbxSearchText"]'))).send_keys(valor)
		sleep(4)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_ManagerContent_agvsReportTemplates_btnSearch"]')))

		user_logging.click()
		sleep(4)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/div[4]/div/div/div/div[1]/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[3]')))
		user_logging.click()



		sleep(4)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_ManagerContent_ReportTemplateTabContainer_ReportTemplateDetailsPanel_btnRunReport_ShadowButtonSpan"]')))
		user_logging.click()
		print(valor)
		sleep(80)
		print('termino funcion ModelosInforme')


	def DesacrgaDatos():


		sleep(20)
		#user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/app-root/app-home/div/div/main/cxone-sidebar/div/div/div[2]/div[4]/div/div[2]/a[3]/span')))
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataDownload"]')))
		user_logging.click()
		sleep(5)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/div[4]/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[11]/td[2]')))
		user_logging.click()
		sleep(5)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_BaseContent_ReportOptions_ctrlDatePicker_A1"]')))
		user_logging.click()


		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_BaseContent_ReportOptions_chkHeaderRow"]')))
		user_logging.click()

		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_BaseContent_ReportOptions_btnDownload_ShadowButtonSpan"]')))
		user_logging.click()

		sleep(60)

		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/app-root/app-home/div/div/main/cxone-sidebar/div/div/div[2]/div[4]/div/div[2]/a[3]/span')))
		user_logging.click()
		sleep(5)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/div[4]/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div[1]/table/tbody/tr/td[7]/table/tbody/tr/td')))
		user_logging.click()
		sleep(5)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/div[4]/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[10]/td[2]')))
		user_logging.click()
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_BaseContent_ReportOptions_ctrlDatePicker_A1"]')))
		user_logging.click()

		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_BaseContent_ReportOptions_chkHeaderRow"]')))
		user_logging.click()

		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_BaseContent_ReportOptions_btnDownload_ShadowButtonSpan"]')))
		user_logging.click()
		print('termino DesacrgaDatos')
		sleep(60)


		




	def excel(items):


		df = pd.read_csv(items,encoding='latin-1',low_memory=False)
		print('ok')
		items=items[:-4] 
		df.to_excel(items+'_.xlsx', index=False)
		#df = pd.read_csv(r"\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\\TP Reporting CARE Skills Volume_20220801T121720.csv",encoding='latin-1',low_memory=False)
		#df.to_excel(r"\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\\TP Reporting CARE Skills Volume_20220801T121720.xlsx", index=False)
		try:
			excelfile = r"\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\\TP Reporting CARE Skills Volume_20220801T121720.xlsx"
			excelfile=items+'_.xlsx'
			visible = True
			excel = win32.DispatchEx('Excel.Application')
			excel.Interactive = False
			excel.Visible = False
			excel.ScreenUpdating = visible
			excel.DisplayAlerts = False
			workbook = excel.Workbooks.Open(excelfile)
			mainsheet= workbook.Worksheets('Sheet1')


			import openpyxl
			#excelfile = r"\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\\TP Reporting CARE Skills Volume_20220801T121720.xlsx"
			book = openpyxl.load_workbook(excelfile,read_only=False)
			sheet = book.active

			maxim=len(sheet['A'])
			print(maxim)
			lista  = mainsheet.Range('A1:A'+str(maxim))
			lista.TextToColumns( DataType=1, TextQualifier=1, ConsecutiveDelimiter=True,
			Tab=False, Semicolon=False, Comma=True, Space=False, Other=False)
			excel.ActiveWorkbook.Save()
			try:
				mainsheet.getCells().delete_cols(2)
				print('fin')
			except:
				pass

			
			#print(sheets1[1])
			#sheets=book['Sheet1']
			try:
				sheet.delete_cols(15,28)
			except:
				pass
			#sheet.delete_cols(2)
			#print(sheets1[1])
			print('fin')
			book.save(filename = items+'__.xlsx')
			#os.remove(items+'_.xlsx')
			#excel.ActiveWorkbook.Save()
			#book.save(filename = r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\\TP Reporting CARE Skills Volume_20220801T121720.xlsx')

			#excel.ActiveWorkbook.Save()
			
		finally:
			excel.EnableEvents = True
			excel.ScreenUpdating = True
			excel.DisplayAlerts = True
			excel.ActiveWorkbook.Save()
			if visible == False:
				excel.Visible = not visible
			workbook.Close(False)
			excel.Quit()
		
		df = pd.read_excel(items+'__.xlsx')
		#df = pd.read_excel(r"\\10.151.230.78\Dropbox\Transversal\Proyectos\ActivosFijos\ActivosCubic\BACKUP\Peru\\ReporteUbicacionSerialesConResponsable.xlsx")
		#os.remove(items+'.CSV')
		try:
			df=df.rename(columns={'ï»¿Fecha':'Fecha','Promedio de tiempo de gestiÃ³n':'Promedio de tiempo de gestion'})
		except:
			pass
		df=df.drop(['Intervalo 30 minutos'], axis=1)
		#df=df.drop(df.columns[1], axis=1)
		df.to_csv(items+'_Interval.csv', index=False)
		os.remove(items+'__.xlsx')
		os.remove(items+'_.xlsx')




	def archivo_Volume(fecha):
		print('funcion archivo_Volume')
		#fecha = (datetime.now()).strftime('%Y-%m-%d')
		#fecha = fecha.split('-')
		#fecha = str(fecha[0]+fecha[1]+fecha[2])
		print(fecha)
		for i in  os.listdir(downloadpath):
			if 'TP Reporting CARE Skills Volume_'+fecha in i and i.endswith('.CSV'):
				items = downloadpath+'\\'+i
				print('paso a la siguiente función')
				excel(items)



	def PrimerDia(fecha):
		sleep(10)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ReportTemplateList"]')))
		user_logging.click()
		try:
			user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_ManagerContent_agvsReportTemplates_btnClearSearch"]')))
			user_logging.click()
		except:
			pass
		sleep(10)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_ManagerContent_agvsReportTemplates_tbxSearchText"]'))).send_keys('1073743024')
		sleep(3)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_ManagerContent_agvsReportTemplates_btnSearch"]')))

		user_logging.click()
		sleep(3)
		sleep(3)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/div[4]/div/div/div/div[1]/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[3]')))
		user_logging.click()
		sleep(5)
		#user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_ManagerContent_ReportTemplateTabContainer_ReportTemplateDetailsPanel_btnEditDetails_ShadowButton"]')))
		#user_logging.click()
		sleep(5)
		user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl00_ctl00_BaseContent_Content_ManagerContent_ReportTemplateTabContainer_ReportTemplateDetailsPanel_btnRunReport_ShadowButtonSpan"]')))
		user_logging.click()
		sleep(150)
		print('paso a la siguiente función')
		archivo_Volume(fecha)
	try:
		PreDesigned()
	except:
		pass
	ModelosInforme('21248')
	ModelosInforme('21479')
	ModelosInforme('21481')
	ModelosInforme('21516')
	ModelosInforme('21568')
	ModelosInforme('1073742367')

	DesacrgaDatos()

	fecha = (datetime.now()).strftime('%Y-%m-%d')
	print(fecha)
	fecha = fecha.split('-')
	print(fecha)
	Fecha = str(fecha[0]+fecha[1]+fecha[2])

	if Fecha[7]=='8' and Fecha[6]=='0':
		print('paso funcion Primer dia')
		PrimerDia(Fecha)





browser.quit()