# import random
import os
import sys
import logging
# from time import sleep
import shutil 
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


# options = Options()
# options.binary_location = r'C:\Users\martineztorres.55\AppData\Local\Mozilla Firefox\firefox.exe' 


# browser = webdriver.Firefox(executable_path='C:\\Users\\martineztorres.55\\Desktop\\mios\\geckodriver.exe', firefox_options=options) 
# token = '658690608c9d6bfb7a2a7ca0d9aee0efa9a10182b825a0acba'

# #================================= Iniciar Sesiòn ==================================================
# try:
#     browser.get('https://adminfoflex.bancolombia.com.co/vsmart/index.php')        
#     browser.maximize_window()
#     tarsConstruct_debugs.app_login(app=browser,request_token=token,credentials_services=['AdminfoflexCBZ'],usernamefield_id='usuario',passwordfield_id='clave')
#     sleep(2)
#     browser.find_element_by_xpath('/html/body/div[4]/div/form/div[3]/div[5]/button').click() 
#     logging.info('Ingreso a la app web sin problema')
# except:
#         logging.info('No Ingreso a la app web, problema') 

# #=================================Selecion para el informe==================================================
# try:
#     webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div[3]/div/a[2]'))).click()
#     logging.info('Selecciono informe principal')
# except:
#     logging.info('No selecciono informe principal')     

# #=================================Selecion para el tipo de datos==================================================
# try:
#     webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div[2]/div[3]/table/tbody/tr[2]/td[2]')))
#     browser.find_element_by_xpath('/html/body/div[10]/div[2]/div[3]/table/tbody/tr[2]/td[2]').click() 
#     logging.info('Selecciono tipo de datos')
# except:
#     logging.info('No selecciono tipo de datos')   

# #================================= Carga la opcion para selecionar las variables ==================================================
# try:
#     browser.get('https://adminfoflex.bancolombia.com.co/vsmart/index.php?rtr=informes&ctr=InformesControlador&acc=&nom_programa=inf_direc')
#     logging.info('Cargo pantalla para cargar las variables')
# except:
#     logging.info('No cargo pantalla para cargar las variables')        

# #===================================Fracción del código que parametriza las variables==============================
# try:
#     #================================= Selecion el pimer filtro ==================================================
#     sleep(2)
#     webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_agrupador"]/a/span[2]'))).click() 
#     sleep(2)
#     webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/div/input'))).send_keys('Detalle En Pantalla')
#     sleep(2)
#     webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/ul/li/div'))).click() 
#     sleep(2)
#     #================================= Selecion el segundo filtro ==================================================
#     webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_col"]'))).click() 
#     sleep(2)
#     webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/div/input'))).send_keys('Fecha Gestion Telefono')
#     sleep(2)
#     webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/ul/li/div'))).click() 
#     sleep(2)
#     #================================= Selecion el tercer filtro ==================================================
#     webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_ope"]'))).click() 
#     # sleep(2)
#     webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/div/input'))).send_keys('Igual Que')
#     # sleep(2)
#     webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/ul/li[1]/div'))).click() 
#     sleep(2)
#     #================================= Selecion el cuarto filtro ==================================================
#     #webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="valor"]'))).send_keys(50617)
#     sleep(2)
#     #webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="btnAgregarCriterio"]'))).click() 
#     # logging.info('OK, variable detalle en pantalla')

# except:    
#     logging.info('Error, no se seleccionaron las variables del reporte')    

        


# día = ('return document.querySelector("#ui-datepicker-div > table > tbody > tr:nth-child(5) > td:nth-child(4)").innerText')
# print(día)

# //*[@id="btnAgregarCriterio"]

# //*[@id="add_tab"]
# /html/body/div[2]/div[1]/div/div[3]/div/div[2]/div/div/a[3]

# //*[@id="detallePantallaVisor_5398"]/div[2]/a[3]
# /html/body/div[2]/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/a[3]

# //*[@id="toolbar"]/a[3]
# /html/body/div[2]/div[1]/div/div[3]/div/div[2]/div[2]/div/div/span[1]/a[3]

# //*[@id="printerCSV_710"]/form/div[3]/input[1]
# /html/body/div[2]/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/form/div[3]/input[1]
# from datetime import date, time, datetime, timedelta
# DiaAyer = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
# DiaAyer = DiaAyer.split('-')
# year, month, day=DiaAyer[0],DiaAyer[1],DiaAyer[2]
# print(year,month,day)
downloadpath='C:\\Users\\MARTIN~1.55\\AppData\\Local\\Temp\\'
try:
    items = os.listdir(downloadpath)
#=====================Mueve el archivo descomprimido===================================    
    if 'Informe' in items:
        print(items)
        head,tail = os.path.split(a)        
        shutil.move('C:\\Users\\martineztorres.55\\Desktop\\mios\\nininin\\')
        logging.info('Pasa a drop y finaliza OK')
except:
    logging.info('Error, descomprimiendo y pasando a ruta de Dropbox')