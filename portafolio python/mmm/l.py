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
from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# ===================================================================================================

__file__ =  os.path.abspath(__file__) #get the path of file
print(__file__)
path = os.path.dirname(__file__) #get the folder of file
print(path) #print the path of folder
globaltime =  datetime.now()  #get the date of today
dayvalue = globaltime.strftime('%Y-%m-%d')  #format of date
dateM3 = globaltime - timedelta(days=3) #get date -3




downloadpath = path+'\\'




options=Options()

options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe' 
#options.binary_location = r'C:\Users\martineztorres.55\AppData\Local\Mozilla Firefox\firefox.exe'
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True 
#downloadpath = r"\\10.151.230.78\Dropbox\Panamericano\Bancolombia\Cobranza\RPAs\Informe Compromisos Adminfo\\"
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

browser = webdriver.Firefox(capabilities=cap, executable_path='C:\\Users\\martineztorres.55\\Desktop\\mios\\geckodriver.exe', options=options)






logging.info('Se ejecuto el codigo')


browser = webdriver.Firefox(executable_path='C:\\Users\\martineztorres.55\\Desktop\\mios\\geckodriver.exe')
browser.get('https://www.seadc.ccms.teleperformance.com/ccms-bin/home.pl')
token = '24e9c0614b1deaeed033735d8ef898bf7d034f251a0f4bf42b' #Deben copiar el token
logging.info('Inicia Sesion')
print('Inicia Sesion')
webdriver = WebDriverWait(browser, 40).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="loginname"]')))
sleep(1)
token= 'b853fe7ef4bf125714c72dea8636d31d98f0679e4f46af0b98'
tarsConstruct_debugs_.app_login(app=browser,request_token=token,credentials_services=['CCMS Disney-Star'],usernamefield_xpath='//*[@id="loginname"]',passwordfield_xpath='//*[@id="password"]')

DiaAyer = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')
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




select.select_by_visible_text('Quality Form Disney+ Tier 1 v1')
#select.select_by_visible_text('Quality Form Disney+ Tier 2 v1')
#select.select_by_visible_text('SoMe Disney+ Quality Form v4')




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