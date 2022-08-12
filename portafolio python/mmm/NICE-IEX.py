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


downloadpath = r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice IEX'


options.set_preference("browser.download.dir", downloadpath)
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/force-download, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet ,\
                                                                application/octet-stream doc xls pdf txt,\
                                                                text/csv,application/x-msexcel,\
                                                                application/excel,application/x-excel,\
                                                                applicatno lion/vnd.ms-excel,\
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

ruta1= r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice IEX\TimeOFF'



def selenium(browser,downloadpath):

    fecha = (datetime.now()).strftime('%Y-%m-%d')
    print(fecha)
    fecha = fecha.split('-')
    print(fecha)
    Fecha = str(fecha[0]+fecha[1]+fecha[2])

    def descarga(path,items):
            
            
            
            try:
                shutil.move(items, path)
            except:
                print('Error al renombrar el archivo')
                logging.info('Error al renombrar el archivo')
                pass
            try:
                    os.remove(items)
            except:
                    pass



    def Nice_IEX(ruta1):
        try:
            for i in range(int(len(table_row)/8),int(len(table_row)/8)-5,-1):
                   user_logging=WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'html/body/table[1]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td/div/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/a[2]'))).click()
                   sleep(5)

            for i in  os.listdir(downloadpath):
                    if '.' in i:
                            items = downloadpath+'\\'+i
                            path = ruta1+'\\'+i
                            descarga(path,items)

            for i in range(int(len(table_row)/8)-5,int(len(table_row)/8)-10,-1):
                   user_logging=WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'html/body/table[1]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td/div/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/a[2]'))).click()
                   sleep(5)
            for i in  os.listdir(downloadpath):
                    if '.' in i:
                            downloadpath2= r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice IEX\Scheduled_Hours'
                            items = downloadpath+'\\'+i
                            path = downloadpath2+'\\'+i
                            descarga(path,items)

            for i in range(int(len(table_row)/8)-10,int(len(table_row)/8)-15,-1):
                   user_logging=WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'html/body/table[1]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td/div/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/a[2]'))).click()
                   sleep(5)

            for i in  os.listdir(downloadpath):
                    if '.' in i:
                            downloadpath2= r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice IEX\TrainingHours'
                            items = downloadpath+'\\'+i
                            path = downloadpath2+'\\'+i
                            descarga(path,items)


            for i in range(int(len(table_row)/8)-15,int(len(table_row)/8)-20,-1):
                   user_logging=WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'html/body/table[1]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td/div/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/a[2]'))).click()
                   sleep(5)

            for i in  os.listdir(downloadpath):
                    if '.' in i:
                            downloadpath2= r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice IEX\AuxHours'
                            items = downloadpath+'\\'+i
                            path = downloadpath2+'\\'+i
                            descarga(path,items)


            for i in range(int(len(table_row)/8)-20,int(len(table_row)/8)-25,-1):
                    user_logging=WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'html/body/table[1]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td/div/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/a[2]'))).click()
                    sleep(10)


            for i in  os.listdir(downloadpath):
                    if '.' in i:
                            downloadpath2= r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice IEX\TechIssuesHours'
                            items = downloadpath+'\\'+i
                            path = downloadpath2+'\\'+i
                            descarga(path,items)


            for i in range(int(len(table_row)/8)-25,int(len(table_row)/8)-30,-1):
                    user_logging=WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'html/body/table[1]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td/div/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/a[2]'))).click()
                    sleep(10)


            for i in  os.listdir(downloadpath):
                    if '.' in i:
                            downloadpath2= r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice IEX\TeleperformanceAdherence'
                            items = downloadpath+'\\'+i
                            path = downloadpath2+'\\'+i
                            descarga(path,items)



            for i in range(int(len(table_row)/8)-35,int(len(table_row)/8)-40,-1):
                    user_logging=WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'html/body/table[1]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td/div/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/a[2]'))).click()
                    sleep(10)


            for i in  os.listdir(downloadpath):
                    if '.' in i:
                            downloadpath2= r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice IEX\OverTime'
                            items = downloadpath+'\\'+i
                            path = downloadpath2+'\\'+i
                            descarga(path,items)


            for i in range(int(len(table_row)/8)-40,int(len(table_row)/8)-45,-1):
                    user_logging=WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'html/body/table[1]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td/div/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/a[2]'))).click()
                    sleep(10)


            for i in  os.listdir(downloadpath):
                    if '.' in i:
                            downloadpath2= r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice IEX\Unapproved Time Off'
                            items = downloadpath+'\\'+i
                            path = downloadpath2+'\\'+i
                            descarga(path,items)


            for i in range(4,0,-1):
                user_logging=WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'html/body/table[1]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td/div/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/a[2]'))).click()
                sleep(10)
           
            for i in  os.listdir(downloadpath):
                    downloadpath2= r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice IEX\SunrunADH'
                    if 'report(3)' in i:
                            items = downloadpath+'\\'+i
                            i=i[:-9]
                            path=downloadpath2+'\\'+i+' ADH '+str(Fecha)+' Digital.xlsx'
                            descarga(path,items)

                    if 'report(2)' in i:
                            items = downloadpath+'\\'+i
                            i=i[:-9]
                            path=downloadpath2+'\\'+i+' ADH '+str(Fecha)+' CM.xlsx'
                            descarga(path,items)
                    if 'report(1)' in i:
                            items = downloadpath+'\\'+i
                            i=i[:-9]
                            path=downloadpath2+'\\'+i+' ADH '+str(Fecha)+' ST.xlsx'
                            descarga(path,items)
                    if 'report.' in i:
                            items = downloadpath+'\\'+i
                            i=i[:-5]
                            path=downloadpath2+'\\'+i+' ADH '+str(Fecha)+' CC.xlsx'
                            descarga(path,items)
        except:
            logging.info('No se pudo realizar la descarga de los archivos')
            print('No se pudo realizar la descarga de los archivos')
    
    def logging():    
        try:
            for i in os.listdir( r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice IEX'):
                if i.endswith('.csv') or i.endswith('.xlsx'):
                    os.remove(r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice IEX\\'+i)
                else: 
                    for j in os.listdir( r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice IEX\\'+i):
                        os.remove(r'\\10.151.230.78\Dropbox\Transversal\Proyectos\Sunrun\Nice IEX\\'+i+'\\'+j)
        except:

            pass
        

        try:
            browser.get('https://wfm4595152-nicewfm.niceincontact.com/wfm/supervisor/home')



            tarsConstruct_debugs_.app_login(app=browser,usernamefield_id="username",passwordfield_id='password',credentials_services=['SunrunIEX'], request_token=token)
            user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnLogin"]')))
            user_logging.click()
            sleep(5)
            # user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-side-nav/nav/header/a')))
            # user_logging.click()
            # sleep(2)
            user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-side-nav/nav/div/ul/li[8]/a')))
            user_logging.click()
            sleep(2)
            user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-side-nav/nav/div/ul/li[8]/ul/li[2]/a')))
            user_logging.click()
            sleep(60)

            #element = driver.find_element_by_tag_name('a')
            #browser.find_element_by_xpath('//div[@class="generatedTimeColumn_N" and contains(text(),"8/4/22 4:01 AM")]')
            print('ok')
            #user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root')))
            browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
            #user_logging =browser.find_elements(By.XPATH, 'html/body/table[1]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td/div/div/div[2]/table/tbody/tr/td' and contains(text()='8/4/22 4:01 AM')")
            #user_logging =browser.find_elements(By.xpath("//<tagName>[text()='text value']"))
            #print(user_logging.get_attribute('tr'))
            user_logging =browser.find_elements(By.XPATH, 'html/body/table[1]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td/div/div/div[2]/table/tbody/tr')
            #print(user_logging)
            table_row = []
            for row in user_logging:
                columns = row.find_elements(By.XPATH,"./td") # Use dot in the xpath to find elements with in element.
                for column in columns:
                    #table_row.append(column)
                    table_row.append(column.text)
             
            print(len(table_row))
            Nice_IEX(ruta1=ruta1)

        except:
            logging.info('Error en la pagina. Problemas en la autenticacion o encontrando los archivos deseados')
            print('Error en la pagina. Problemas en la autenticacion o encontrando los archivos deseados')


    logging()









selenium(browser,downloadpath)
browser.quit()