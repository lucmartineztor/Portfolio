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

from os import remove


__file__ = os.path.abspath(__file__)
path = os.path.dirname(__file__)
mainpath = os.path.split(path)
sys.path.append(mainpath[0])


def selenium(browser, downloadpath):
	print(path)
	globaltime =  datetime.now()  #get the date of today
	dayvalue = globaltime.strftime('%Y-%m-%d')  #format of date
	dateM3 = globaltime - timedelta(days=3) #get date -3

	#downloadpath = path + "\\DownloadFile"
	#if not os.path.exists(downloadpath):
		#os.makedirs(downloadpath)

#	logRPA = path + "\\LogRPACSAT"
#	if not os.path.exists(logRPA):
#	    os.makedirs(logRPA)

#	logging.basicConfig(filename=logRPA+ r'\DiscordRPA.log', level=logging.INFO)
#	logging.info('Se ejecuto el codigo')
#	logging.info(dayvalue)

	try:
		browser.get('https://discord.com/login?brand_id=96508&locale_id=2&return_to=https%3A%2F%2Fsupport.discord.com%2Fexplore%2F&service=zendesk&timestamp=1633356324')
		logging.info('Inicia Sesion')
		print('Inicia Sesion')
		webdriver = WebDriverWait(browser, 40).until(EC.visibility_of_element_located((By.XPATH,'//input[@name="email"]')))
		sleep(1)
		tarsConstruct.app_login(app=browser,credentials_services=['Discord - Zendesk'],usernamefield_xpath='//input[@name="email"]',passwordfield_xpath='//input[@name="password"]')
		sleep(1)
		browser.find_element_by_xpath('//button[@class="marginBottom8-AtZOdT button-3k0cO7 button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeLarge-1vSeWK fullWidth-1orjjo grow-q77ONN"]').click() 
		sleep(4)
		webdriver = WebDriverWait(browser, 800).until(EC.visibility_of_element_located((By.XPATH,'//button[@title="Queries"]')))
		logging.info('Fin Inicio sesion')
		print('Fin Inicio sesion')
	except:
		pass
	#================================= Fin Inicio Sesion ==================================================

	def Total_Reporting():
		logging.info('Total Reporting')
		browser.get('https://hammerandchisel.zendesk.com/explore#/pivot-table/connection/12026271/query/68463341')
		webdriver = WebDriverWait(browser, 120).until(EC.visibility_of_element_located((By.XPATH,'//div[@bime-tooltip="Update - Date"]')))
		try:
			sleep(10)
			browser.find_element_by_xpath('//div[@bime-tooltip="Update - Date"]').click()    
		except ElementClickInterceptedException:
			sleep(10)
			logging.warning('No hay data')
			browser.find_element_by_xpath('/html/body/div[@class="bime-popup"]/div[2]/div[2]/button[@id="bimePopup-1"]').click()
		#Waiting web driver
		sleep(4)
		webdriver = WebDriverWait(browser, 120).until(EC.visibility_of_element_located((By.ID,'bimeHierarchyMembers-2')))
		try:
			browser.find_element_by_id('bimeHierarchyMembers-2').click()
		except ElementClickInterceptedException:
			sleep(40)
			logging.warning('No hay data')
			browser.find_element_by_xpath('/html/body/div[@class="bime-popup"]/div[2]/div[2]/button[@id="bimePopup-1"]').click()
			sleep(5)
		if globaltime.strftime('%w') != '1' :
			logging.info('No es lunes')
			browser.find_element_by_xpath('//bime-radio[@value="today"]/div/div[2]').click()
		else:
			print('Es lunes')
			logging.info('Es lunes')
			sleep(3)
			browser.find_element_by_xpath('//div[@class="animated bime-range-date-container"]/div/div/div[@class="bime-switch ng-pristine ng-untouched ng-valid ng-not-empty"]/div[2]').click()
			browser.find_element_by_xpath('//div[@class="advanced-range-date"]/bime-radio[3]/div/div').click()
			browser.find_element_by_xpath('//div[@class="advanced-range-date"]/bime-radio[3]/div/div[2]/span/input').clear()
			browser.find_element_by_xpath('//div[@class="advanced-range-date"]/bime-radio[3]/div/div[2]/span/input').send_keys("3")
			logging.info('Fecha inicio a -3 dias')
			browser.find_element_by_xpath('//div[@class="advanced-range-date"]/bime-radio[3]/div/div[2]/div').click()
			browser.find_element_by_id('select2-result-label-22').click()
			logging.info('Fecha fin dia de hoy')
			browser.find_element_by_xpath('//div[@class="advanced-range-date"]/bime-radio[5]/div/div').click()
			# browser.execute_script("$('#bimeRangeDate-3').text('" + globaltime.strftime('%Y/%m/%d') +"')")
		browser.find_element_by_id('bimeRangeDate-8').click()
		for i in range(0,60):
			sleep(2)
			try:
				browser.find_element_by_xpath('//div[@class="loader-container"]')
			except:
				logging.info('Termina Carga de tabla')
				print('Termino Carga de datos con fechas')
				break
		webdriver = WebDriverWait(browser, 40).until(EC.visibility_of_element_located((By.XPATH,'//button[@class="sc-dlnjPT sc-jSFkmK liGXLv fllDip"]')))
		browser.find_element_by_xpath('//button[@class="sc-dlnjPT sc-jSFkmK liGXLv fllDip"]').click()
		sleep(2)

		print('Despues de click save')
		logging.info('Click en el save para export')
		webdriver = WebDriverWait(browser, 40).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="sc-dPaNSN kwJeao is-animated"]/ul/li[4]')))
		browser.find_element_by_xpath('//div[@class="sc-dPaNSN kwJeao is-animated"]/ul/li[4]').click()
		print('Selecciona 4 opcion')
		sleep(5)
		try:
			sleep(10)
			print('csv')
			#webdriver =WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[20]/div[1]/div[2]/div[1]/div[1]/div[1]/label[1]'))).click()
			webdriver =WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="10val-field_1.3.7--label"]'))).click()
			sleep(5)
			print('quitar Image')
			webdriver =WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="12val-field_1.3.7--label"]'))).click()
			sleep(2)
			webdriver =WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="12val-field_1.3.7--label"]'))).click()
			sleep(5)
			
		except Exception as e:
			print(e)
			sleep(10)
			pass
		try:
			sleep(10)
			print('csv')
			#webdriver =WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[20]/div[1]/div[2]/div[1]/div[1]/div[1]/label[1]'))).click()
			webdriver =WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="8val-field_1.3.7--label"]'))).click()
			sleep(5)
			print('quitar Image')
			webdriver =WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="10val-field_1.3.7--label"]'))).click()
			sleep(2)
			webdriver =WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="10val-field_1.3.7--label"]'))).click()
			sleep(5)
			
		except Exception as e:
			print(e)
			sleep(10)
			pass

		print('Export')
		webdriver =WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="sc-dlnjPT bNVMrz"]'))).click()
		sleep(30)

	try:
		Total_Reporting()
		directorio = os.listdir(downloadpath)
		strmatch = [i for i in directorio if "Total_Reporting" in i]
		shutil.move( downloadpath + '\\' + strmatch[0] , '\\\\10.151.230.78\\Dropbox\\New Economy\\Discord\\DailyInfo\\Discord_Tickets_Touches_ZD\\' + strmatch[0])
		print('Termino')
		logging.info('Termino proceso')
	except Exception as e:
		print(e)
		logging.error(e)
	finally:
		browser.quit()


if __name__ == '__main__':
	profilepath = path + '\\' + 'ds_Discord_DiscordTotalReporting'
	shutil.rmtree(profilepath, ignore_errors=True, onerror=None)
	service = tarsConstruct.TARS_Service(filepath=__file__)
	service.fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip; charset=utf-8")
	service.fp.set_preference("browser.helperApps.neverAsk.openFile","application/zip; charset=utf-8")
	service.run_service(func=selenium)