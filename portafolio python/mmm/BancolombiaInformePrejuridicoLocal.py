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


options = Options()
options.binary_location = r'C:\Users\ortizc.28\AppData\Local\Mozilla Firefox\firefox.exe' 
downloadpath = r'C:\Users\ortizc.28\Documents\RPA\modulos'
options.set_preference("browser.download.dir", downloadpath)
ruta = r'C:\Users\ortizc.28\Documents\RPA\modulos\Descarga'

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

browser = webdriver.Firefox(executable_path=r"C:\Users\ortizc.28\Documents\RPA\modulos\geckodriver.exe", firefox_options=options) 
token = 'f23bda4a9ecb63d93d08d06e49bc46a0420c50ab60aacf85ca'

#================================= Iniciar Sesiòn ==================================================
try:
    browser.get('https://adminfoflex.bancolombia.com.co/vsmart/index.php')        
    browser.maximize_window()
    tarsConstruct_debugs.app_login(app=browser,request_token=token,credentials_services=['AdminfoflexCBZ'],usernamefield_id='usuario',passwordfield_id='clave')
    sleep(2)
    browser.find_element_by_xpath('/html/body/div[4]/div/form/div[3]/div[5]/button').click() 
    logging.info('Ingreso a la app web sin problema')
except:
        logging.info('No Ingreso a la app web, problema') 

#=================================Selecion para el informe==================================================
try:
    webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div[3]/div/a[2]'))).click()
    logging.info('Selecciono informe principal')
except:
    logging.info('No selecciono informe principal')     

#=================================Selecion para el tipo de datos==================================================
try:
    webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div[2]/div[3]/table/tbody/tr[2]/td[2]')))
    browser.find_element_by_xpath('/html/body/div[10]/div[2]/div[3]/table/tbody/tr[2]/td[2]').click() 
    logging.info('Selecciono tipo de datos')
except:
    logging.info('No selecciono tipo de datos')   

#================================= Carga la opcion para selecionar las variables ==================================================
try:
    browser.get('https://adminfoflex.bancolombia.com.co/vsmart/index.php?rtr=informes&ctr=InformesControlador&acc=&nom_programa=informesprejuridicos_agentesexternos')
    logging.info('Cargo pantalla para cargar las variables')
except:
    logging.info('No cargo pantalla para cargar las variables')        

#===================================Fracción del código que parametriza las variables==============================
try:
    #================================= Selecion el pimer filtro ==================================================
    sleep(2)
    webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_agrupador"]'))).click() 
    sleep(2)
    webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/div/input'))).send_keys('Detalle En Pantalla')
    sleep(2)
    webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[10]/ul/li/div/span'))).click() 
    sleep(2)
    #================================= Selecion el segundo filtro ==================================================
    webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_col"]'))).click() 
    sleep(2)
    webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/div/input'))).send_keys('Código Abogado')
    sleep(2)
    webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/ul/li[1]/div/span'))).click() 
    sleep(2)
    #================================= Selecion el tercer filtro ==================================================
    webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_ope"]'))).click() 
    sleep(2)
    webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/div/input'))).send_keys('Igual Que')
    sleep(2)
    webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-drop"]/ul/li[1]/div'))).click() 
    sleep(2)
    #================================= Selecion el cuarto filtro ==================================================
    webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="valor"]'))).send_keys(50617)
    sleep(2)
    webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="btnAgregarCriterio"]'))).click() 
    logging.info('OK, variable detalle en pantalla')
except:    
    logging.info('Error, no se seleccionaron las variables del reporte')    

    
#=======================================Parte final del código para la descargar del archivo final==========================================
try:    
#=================================Cargar el informe==================================================
    sleep(3)
    webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="add_tab"]'))).click() 
    sleep(3)
    webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/a[3]'))).click() 
    
#=================================Espera que los datos esten disponible para el exporte y click a csv==================================================
    webdriver = WebDriverWait(browser, 70).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[1]/div/div[3]/div/div[2]/div[2]/div/div/span[1]/a[3]')))
    
    sleep(2)
    webdriver = WebDriverWait(browser, 70).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[1]/div/div[3]/div/div[2]/div[2]/div/div/span[1]/a[3]'))).click()
    
#================================= Le da click al exporte final==================================================
    sleep(2)
    webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/form/div[3]/input[1]'))).click() 
    
#=================================Deslogueo de la app==================================================
    sleep(20)
    browser.quit()
    logging.info('Termino de descargar .ZIP, cierra seccion y baja el driver')
except:
    logging.info('Error, no se pudo cargar datos para descargar el informe')    

#================================Mueve la descarga a Dropbox==================================================
try:
    sleep(2)
    items = os.listdir(downloadpath)

    #=====================Descomprime el archivo===================================
    for x in items:
        if '.zip' in x:
            DesZip = zipfile.ZipFile(downloadpath+'\\'+x)
            DesZip.extractall(downloadpath)
            DesZip.close()
            os.remove(downloadpath+'\\'+x)            
            logging.info('Descomprime .ZIP OK')
    #=====================Mueve el archivo descomprimido===================================    
    items = os.listdir(downloadpath)
    hoy = datetime.now().strftime('%Y%m%d')
    if datetime.now().time() < time(12):
        c = 'AM'
    else:
        c = 'PM'

    for a in items:
        if '.csv' in a:
            #head,tail = os.path.split(a)
            b = f'Informe Prejuridico {c} {hoy}.csv'
            os.rename(downloadpath+'\\'+a,downloadpath+'\\'+b)
            shutil.move(downloadpath+'\\'+b,ruta+'\\'+b)
            logging.info('Pasa a drop y finaliza OK')
except:
    logging.info('Error, descomprimiendo y pasando a ruta de Dropbox')
