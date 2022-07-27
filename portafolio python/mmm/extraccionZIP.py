import zipfile
import pandas as pd
import os
from datetime import date, time, datetime, timedelta
from time import sleep
from os import remove


import calendar

calendar.setfirstweekday(6)


import numpy as np

def get_week_of_month(year, month, day):
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] + 1
    n=np.where(x[week_of_month-1] == day)
    return week_of_month, x, day, int(n[0])


week_of_month, x, day, n = get_week_of_month(2022,2,23)
print(week_of_month, x, day, n)

# for i in  os.listdir("C:\\Users\\martineztorres.55\\Downloads\\"):
# 	if 'Informe' in i:
# 		items = "C:\\Users\\martineztorres.55\\Downloads\\"+i
# 		j=i.split('.')
# 		k=i.split('_')
		
# 		password=None
# 		ruta_extraccion=r"\\10.151.230.78\Dropbox\Panamericano\Bancolombia\Cobranza\RPAs\Informe Telefonos Adminfo\\"
# 		#ruta_extraccion=r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\"
# 		archivo_zip = zipfile.ZipFile(items)
# 		h=archivo_zip.namelist()
# 		archivo_zip.extractall(pwd=password, path=ruta_extraccion)
		
# 		DiaAyer = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
# 		DiaAyer = DiaAyer.split('-')
# 		DiaAyer = str(DiaAyer[0]+DiaAyer[1]+DiaAyer[2])
# 		item= k[0]+'_ telefonos_'+DiaAyer
		

# 		sleep(20)
# 		archivo = ruta_extraccion+str(j[0])+'.csv'
# 		nombre_nuevo = ruta_extraccion+str(item)+'.csv'
		
# 		os.rename(archivo, nombre_nuevo)

# 		if day != 6:
# 			ruta_extraccion=r"\\10.151.230.78\Dropbox\Panamericano\Bancolombia\Cobranza\RPAs\Informe Compromisos Adminfo\\"
# 			archivo_zip = zipfile.ZipFile(items)
# 			h=archivo_zip.namelist()
# 			archivo_zip.extractall(pwd=password, path=ruta_extraccion)
			
# 			DiaAyer = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
# 			DiaAyer = DiaAyer.split('-')
# 			DiaAyer = str(DiaAyer[0]+DiaAyer[1]+DiaAyer[2])
# 			item= k[0]+'_compromisos_'+DiaAyer
			

# 			sleep(20)
# 			archivo = ruta_extraccion+str(j[0])+'.csv'
# 			nombre_nuevo = ruta_extraccion+str(item)+'.csv'
			
# 			os.rename(archivo, nombre_nuevo)



# 	#import excel_select

# 	#import cubic
# from os import remove|
# 	#try:
# 		#remove(r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.csv")
# 		#remove("C:\\Users\\martineztorres.55\\Downloads\\ReporteUbicacionSerialesConResponsable.xlsx")
# 	#except:
# 		#pass
# try:

	
# 	print()
# 	number_files = len(os.listdir(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\"))
# 	k=number_files
# 	print(number_files)
# 	for i in  os.listdir(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\"):
# 		if "ReporteUbicacionSerialesConResponsable" in i and i.endswith("zip"):
# 			while k>=0:
# 				remove(r"\\10.151.230.78\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\"+i)
# 				k=k-1
# except:pass

# from os import remove
# remove(r"\\10.151.230.78\\Dropbox\\Transversal\\Proyectos\\ActivosFijos\\ActivosCubic\\BACKUP\\ReporteUbicacionSerialesConResponsable.xlsx")
# import random
# import os
# import sys
# import logging
# from time import sleep
# import shutil 
# from datetime import date, time, datetime, timedelta
# from zipfile import ZipFile
# import zipfile
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
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
# options = Options()

# #cap = DesiredCapabilities().FIREFOX
# #cap["marionette"] = False
# options.binary_location = r'C:\Users\martineztorres.55\AppData\Local\Mozilla Firefox\firefox.exe' 
# #browser = webdriver.Firefox(capabilities=cap,executable_path='C:\\Users\\martineztorres.55\\Desktop\\mios\\geckodriver.exe',options=options)

# browser = webdriver.Firefox(executable_path='C:\\Users\\martineztorres.55\\Desktop\\mios\\geckodriver.exe')

# token = '98153602ec8a5ea0b4824fed4726d0086b014c8cc8a2efd296'

# #================================= Iniciar Sesiòn ==================================================

# browser.get('https://adminfoflex.bancolombia.com.co/vsmart/index.php')        
# browser.maximize_window()

# tarsConstruct_debugs.app_login(app=browser,request_token=token,credentials_services=['AdminfoflexCBZ'],usernamefield_id='usuario',passwordfield_id='clave')
# sleep(2)

# browser.find_element_by_xpath('/html/body/div[4]/div/form/div[3]/div[5]/button').click() 
# logging.info('Ingreso a la app web sin problema')

# try:
#     webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div[3]/div/a[2]'))).click()
#     logging.info('Selecciono informe principal')
# except:
#     logging.info('No selecciono informe principal')
# try:
# 	webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div[2]/div[3]/table/tbody/tr[2]/td[2]')))
# 	browser.find_element_by_xpath('/html/body/div[10]/div[2]/div[3]/table/tbody/tr[2]/td[2]').click() 
# 	logging.info('Selecciono tipo de datos')
# except:
# 	logging.info('No selecciono tipo de datos')

# try:
#     browser.get('https://adminfoflex.bancolombia.com.co/vsmart/index.php?rtr=informes&ctr=InformesControlador&acc=&nom_programa=inf_direc')
#     logging.info('Cargo pantalla para cargar las variables')
# except:
#     logging.info('No cargo pantalla para cargar las variables')
# sleep(2)
 
# # primera parte



# #sleep(2)
# webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_agrupador"]/a/span[2]'))).click() 
# # #sleep(2)
# webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/div/input'))).send_keys('Detalle En Pantalla')
# # #sleep(2)
# webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/ul/li/div'))).click()





# webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_col"]'))).click() 
# # # #sleep(2)
# webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/div/input'))).send_keys('Fecha Gestion Telefono')
# # # #sleep(2)
# webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/ul/li/div'))).click() 
# #sleep(2)
# webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="btnCalendario"]'))).click()

# webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div[1]/div[1]/select'))).send_keys('Octubre')

# webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div[1]/div[1]/select'))).send_keys('2021')




from datetime import date, time, datetime, timedelta
DiaAyer = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
DiaAyer = DiaAyer.split('-')
year, month, day=int(DiaAyer[0]),int(DiaAyer[1]),int(DiaAyer[2])
print(year,month,day)





# webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/table[1]/tbody[1]/tr['+str(week_of_month)+']/td['+str(n+1)+']/a[1]'))).click()


#webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div[2]/button'))).click()

# import holidays_co
# holidays = holidays_co.get_colombia_holidays_by_year(2021)

# x=[]
# for i in holidays:
# 	x.append(i[0].strftime('%Y-%m-%d'))

# if (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d') in x:
# 	print('ok')