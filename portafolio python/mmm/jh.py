
# tokenTars='c262da70cbfb4be98af1db14f2563ff70eff47b72cff07cc95'
# import tarsConstruct
# df = tarsConstruct.SQL_query_to_df(tokenTars,'TPCCP-DB128.teleperformance.co\\SQL2016STD',['SQL-TPCCP-DB128'],'''select account
#     , LOB
#     , wave
#     , hire_date
#     , headcount
#     , tp_client_id
#     , nPeopleViewTotal
# from [PRE_S&H].[Staffing].[vwSH_Agents_Total_Pre_V4]''')
# for i in range(len(df['tp_client_id'])):
# 	if df['tp_client_id'][i]==20216176:
# 		print(df['wave'][i])
# print(len(set(df['tp_client_id'])))
# #print(len(array(df['tp_client_id'].unique())))
# print(df.columns)

# icimsLists=[]
# for i in df['tp_client_id'].head():
# 	if i is not icimsLists:
# 		icimsLists.append(i)
# 	else:
# 		pass



# icimsLists = df['tp_client_id'].head().unique()

# print(icimsLists)



# for i in range(len(df['tp_client_id'])):
# 	for j in icimsLists:
# 		if df['tp_client_id'][i]==j:
# 			print('Para id=',j,'se tenia un estimado de',df['headcount'][i],'y se contrataron',df['nPeopleViewTotal'][i])

# icimsList = df['icims'].unique()
 
# for i in range(len(df['icims'])):
#     if df['icims'][i] in icimsList:
#         print(df['wave'][i])


from os import remove
import random
import os
import sys
from time import sleep
import shutil 
from datetime import date, time, datetime, timedelta
from zipfile import ZipFile
import zipfile
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.firefox.options import Options
# import json
# import tarsConstruct_debugs
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import numpy as np
# import calendar
# import holidays_co

# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# DiaAyer = (datetime.now()).strftime('%Y-%m-%d')
# DiaAyer = DiaAyer.split('-')
# year=int(DiaAyer[0])

# holidays = holidays_co.get_colombia_holidays_by_year(year)

# x=[]



# for i in holidays:
# 	x.append(i[0].strftime('%Y-%m-%d'))

# if (datetime.now()).strftime('%Y-%m-%d') not in x:

# 	options=Options()

# 	options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe' 
# 	cap = DesiredCapabilities().FIREFOX
# 	cap["marionette"] = True
# 	downloadpath=r"\\10.151.230.78\Dropbox\Panamericano\Bancolombia\Cobranza\RPAs\Informe Telefonos Adminfo\\"

# 	options.set_preference("browser.download.dir", downloadpath)
# 	options.set_preference("browser.download.folderList", 2)
# 	options.set_preference("browser.download.manager.showWhenStarting", False)
# 	options.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/force-download, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet ,\
# 	                                                                application/octet-stream doc xls pdf txt,\
# 	                                                                text/csv,application/x-msexcel,\
# 	                                                                application/excel,application/x-excel,\
# 	                                                                application/vnd.ms-excel,\
# 	                                                                image/png,image/jpeg,text/html,text/plain,text/csv,\
# 	                                                                application/msword,application/xml,\
# 	                                                                application/x-www-form-urlencoded,\
# 	                                                                application/csv,\
# 	                                                                text/tab-separated-values,\
# 	                                                                application/ms-excel')

# 	options.set_preference("browser.helperApps.neverAsk.openFile", 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet ,\
# 	                                                                application/octet-stream doc xls pdf txt,\
# 	                                                                text/csv,application/x-msexcel,\
# 	                                                                application/excel,application/x-excel,\
# 	                                                                application/vnd.ms-excel,\
# 	                                                                image/png,image/jpeg,text/html,text/plain,text/csv,\
# 	                                                                application/msword,application/xml,\
# 	                                                                application/x-www-form-urlencoded,\
# 	                                                                application/csv,\
# 	                                                                text/tab-separated-values, \
# 	                                                                application/ms-excel')
# 	options.set_preference("browser.helperApps.alwaysAsk.force", False)
# 	options.set_preference("browser.download.manager.useWindow", False)
# 	options.set_preference("browser.download.manager.focusWhenStarting", False)
# 	options.set_preference("browser.download.manager.showAlertOnComplete", False)
# 	options.set_preference("browser.download.manager.closeWhenDone", True)
# 	cap["marionette"] = True
# 	browser = webdriver.Firefox(capabilities=cap, executable_path='C:\\Users\\martineztorres.55\\Desktop\\mios\\geckodriver.exe', options=options)

# 	token = 'a12cf43f970918bb8139c4f3b2ad621677f3f298b1310d8f81'
# 	flag= 0
# 	try:
# 		for i in  os.listdir(downloadpath):
# 			if 'Informe' in i and i.endswith(".zip"):
# 				remove(downloadpath+i)
# 	except:
# 		pass

# 	while flag<=5:

# 		try:

# 		#================================= Iniciar Sesiòn ==================================================

# 			browser.get('https://adminfoflex.bancolombia.com.co/vsmart/index.php')        
# 			browser.maximize_window()

# 			tarsConstruct_debugs.app_login(app=browser,request_token=token,credentials_services=['AdminfoflexCBZ'],usernamefield_id='usuario',passwordfield_id='clave')
# 			sleep(2)

# 			browser.find_element_by_xpath('/html/body/div[4]/div/form/div[3]/div[5]/button').click() 
# 			logging.info('Ingreso a la app web sin problema')

# 			try:
# 			    webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div[3]/div/a[2]'))).click()
# 			    logging.info('Selecciono informe principal')
# 			except:
# 			    logging.info('No selecciono informe principal')
# 			try:
# 				webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div[2]/div[3]/table/tbody/tr[2]/td[2]')))
# 				browser.find_element_by_xpath('/html/body/div[10]/div[2]/div[3]/table/tbody/tr[2]/td[2]').click() 
# 				logging.info('Selecciono tipo de datos')
# 			except:
# 				logging.info('No selecciono tipo de datos')

# 			try:
# 			    browser.get('https://adminfoflex.bancolombia.com.co/vsmart/index.php?rtr=informes&ctr=InformesControlador&acc=&nom_programa=inf_direc')
# 			    logging.info('Cargo pantalla para cargar las variables')
# 			except:
# 			    logging.info('No cargo pantalla para cargar las variables')
# 			sleep(2)
			 
# 			# primera parte



# 			#sleep(2)
# 			webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_agrupador"]/a/span[2]'))).click() 
# 			# #sleep(2)
# 			webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/div/input'))).send_keys('Detalle En Pantalla')
# 			# #sleep(2)
# 			webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/ul/li/div'))).click()





# 			# #sleep(2)
# 			webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_col"]'))).click() 
# 			# #sleep(2)
# 			webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/div/input'))).send_keys('Código Abogado')
# 			# #sleep(2)
# 			webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/ul/li/div'))).click() 
# 			#sleep(2)

# 			webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="valor"]'))).send_keys(50617)

# 			webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="btnAgregarCriterio"]'))).click()


# 			#================================= Selecion el tercer filtro ==================================================

# 			webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_col"]'))).click() 
# 			# # #sleep(2)
# 			webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/div/input'))).send_keys('Fecha Gestion Telefono')
# 			# # #sleep(2)
# 			webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/ul/li/div'))).click() 

# 			webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="btnCalendario"]'))).click()





# 			#=================================Escoger fecha en Calendario =================================

# 			#webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div[1]/div[1]/select'))).send_keys('Octubre')

# 			#webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div[1]/div[1]/select'))).send_keys('2021')



# 			DiaAyer = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
# 			DiaAyer = DiaAyer.split('-')
# 			year, month, day=int(DiaAyer[0]),int(DiaAyer[1]),int(DiaAyer[2])

# 			calendar.setfirstweekday(6)



# 			def get_week_of_month(year, month, day):
# 			    x = np.array(calendar.monthcalendar(year, month))
# 			    week_of_month = np.where(x==day)[0][0] + 1
# 			    n=np.where(x[week_of_month-1] == day)
# 			    return week_of_month, x, day, int(n[0])


# 			week_of_month, x, day, n = get_week_of_month(year,month,day)




# 			webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/table[1]/tbody[1]/tr['+str(week_of_month)+']/td['+str(n+1)+']/a[1]'))).click()

# 			webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="btnAgregarCriterio"]'))).click()


# 			# tercera parte
# 			#=================================Generar descargas==================================================

# 			sleep(3)
# 			webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="add_tab"]'))).click() 

# 			sleep(5)
# 			webdriver = WebDriverWait(browser, 150).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/a[3]'))).click() 

			
# 			sleep(180)
__file__ =  os.path.abspath(__file__) #get the path of file
print(__file__)
path = os.path.dirname(__file__) #get the folder of file
print(path) #print the path of folder


downloadpath='C:\\Users\\martineztorres.55\\Downloads\\'

token='4835ec9fb4e9fbdbe7ae90b84999005eba149f272bc8a249ab'



for i in  os.listdir(downloadpath):
	import tarsConstruct_debugs_
	if 'form_data_export' in i and i.endswith('zip'):
		items = downloadpath+i
		password=None
		archivo_zip = zipfile.ZipFile(items)
		#path= os.path.dirname(archivo_zip)
		#print(path)
		carpetas=archivo_zip.namelist()
		for i in os.listdir(r'\\10.151.230.78\\dropbox\\Nearshore\\Disney+\\Crudos\\QA\\'):
			if i.endswith('.csv'):
				tarsConstruct_debugs_.spExec("[Disney].[dbo].[spImportQA_ColBR]", server='10.151.230.23\\scnear',request_token=token, credentials_services=['SCNEAR'])

		for i in os.listdir(downloadpath):

			if 'form_data_export' in i and i.endswith('zip'):

				with ZipFile(downloadpath+i) as zipObj:

					carpetas=zipObj.namelist()

					for file in carpetas:

						if 'rollup' in file:

							with zipObj.open(file) as zf, open(downloadpath+'rollup', 'wb') as f:

								shutil.copyfileobj(zf, f)

							os.rename(downloadpath+'rollup', downloadpath+'_FormBr D.csv')
		
					


		#archivo_zip.extract(archivo_csv, path=downloadpath)
		#os.rename(downloadpath+'rollup\\'+archivo_csv[7:], downloadpath+'rollup\\'+'_FormBr D.csv')
		

		#----------------------------cambio de ruta de envio csv--------------------------------------
		#shutil.move(downloadpath+'_FormBr D.csv',r'\\10.151.230.78\\dropbox\\Nearshore\\Disney+\\Crudos\\QA\\') #Cambiar el segundo downloadpath (solo el segundo) por la ruta de extraccion
		#shutil.move(downloadpath+'rollup\\'+'_FormBr D.csv',r'\\10.151.230.78\dropbox\Nearshore\Disney+\Crudos\QAT2\\') #Cambiar el segundo downloadpath (solo el segundo) por la ruta de extraccion
		#shutil.move(downloadpath+'rollup\\'+'_FormBr D.csv',r'\\10.151.230.78\dropbox\Nearshore\Disney+\Crudos\QA\QASoMe') #Cambiar el segundo downloadpath (solo el segundo) por la ruta de extraccion
		import tarsConstruct_debugs_

		archivo_zip.close()
		
		#rmdir(downloadpath+"rollup")

		# for i in  os.listdir(downloadpath):
		# 	if 'form_data_export' in i and i.endswith('zip'):
		# 		remove(i)