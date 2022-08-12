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
import pickle
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

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
#options.set_preference("dom.push.enabled", False)

cap["marionette"] = True

profile = webdriver.FirefoxProfile(r'C:\Users\martineztorres.55\AppData\Roaming\Mozilla\Firefox\Profiles\f3ktijsg.default')
profile.set_preference("dom.push.enabled", False)
profile.update_preferences()
browser = webdriver.Firefox(firefox_profile=profile,capabilities=cap, executable_path='C:\\Users\\martineztorres.55\\Desktop\\mios\\geckodriver.exe', options=options)





#driver = webdriver.Firefox(firefox_profile=profile,executable_path='C:\\Users\\martineztorres.55\\Desktop\\mios\\geckodriver.exe')

#pickle.dump(browser.get_cookies() , open("cookies.pkl","wb"))

# for cookie in cookies:
#     browser.add_cookie(cookie)
# browser.get("https://example.com/p/api/v5/profile/blabla")
# response = json.loads(browser.find_element_by_tag_name('body').text)
# print(response)


#profile = webdriver.FirefoxProfile('/home/admin/.cache/mozilla/firefox/o0eaxyux.user')




token='b238b0352c2e6627277d09ac56246a34fef8522206b6c4d933'



browser.get('https://datastudio.google.com/u/0/reporting/56d89c70-26e8-49e7-b33c-dabd3c60da9c/page/xnWBB/')
print('Logging into the web site')

def load_cookie(driver, path):
    with open(path, 'r') as cookiesfile:
        cookies = json.load(cookiesfile)
    for cookie in cookies:
        driver.add_cookie(cookie)


load_cookie(browser,r'C:\Users\martineztorres.55\AppData\Roaming\Mozilla\Firefox\Profiles\bky1dx65.usuario')


tarsConstruct_debugs_.app_login(app=browser,usernamefield_id='identifierId',credentials_services=['SunrunDS'], request_token=token)

user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')))
user_logging.click()
sleep(5)


tarsConstruct_debugs_.app_login(app=browser,usernamefield_id='okta-signin-username',passwordfield_id='okta-signin-password',credentials_services=['SunrunDS'], request_token=token)


user_logging = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="okta-signin-submit"]')))
user_logging.click()
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
        print(cookie)
        browser.add_cookie(cookie)

pickle.dump(browser.get_cookies() , open("cookies.pkl","wb"))

import json

def save_cookie(driver, path):
    with open(path, 'w') as filehandler:
        json.dump(driver.get_cookies(), filehandler)
save_cookie(browser,r'C:\Users\martineztorres.55\AppData\Roaming\Mozilla\Firefox\Profiles\bky1dx65.usuario')

#browser.get('https://datastudio.google.com/u/0/reporting/56d89c70-26e8-49e7-b33c-dabd3c60da9c/page/xnWBB/')
#response = json.loads(browser.find_element_by_tag_name('body').text)

# sleep(100)

# open_window_elem = browser.find_element_by_id('cdk-describedby-message-ecp-1-89')
# action = webdriver.common.action_chains.ActionChains(browser)
# action.move_to_element_with_offset(open_window_elem, 1, 1)
# action.click()
# action.perform()