import tarsConstruct
import os
import sys
import logging
from time import sleep
import shutil
from datetime import datetime, timedelta
import zipfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import numpy as np
import calendar
import holidays_co
from os import remove


__file__ = os.path.abspath(__file__)
path = os.path.dirname(__file__)
mainpath = os.path.split(path)
sys.path.append(mainpath[0])
profilepath = path + '\\' + 'ds_Bancolombia_Informe_Compromisos'


def selenium(browser, downloadpath):
    
    DiaAyer = (datetime.now()- timedelta(days=1)).strftime('%Y-%m-%d')
    DiaAyer = DiaAyer.split('-')
    year = int(DiaAyer[0])
    holidays = holidays_co.get_colombia_holidays_by_year(year)
    x = []
    for i in holidays:
        x.append(i[0].strftime('%Y-%m-%d'))



    if (datetime.now()- timedelta(days=1)).strftime('%Y-%m-%d') not in x:
        ruta = r"\\10.151.230.78\Dropbox\Panamericano\Bancolombia\Cobranza\RPAs\Informe Compromisos Adminfo\\"
        flag = 0
        # ================================= Iniciar Sesiòn ==================================================
        # while flag<= 5:
        try:
            browser.get(
                r'https://adminfoflex.bancolombia.com.co/vsmart/index.php')
            browser.maximize_window()
            tarsConstruct.app_login(app=browser, credentials_services=[
                                    'AdminfoflexCBZ'], usernamefield_id='usuario', passwordfield_id='clave')
            sleep(2)
            browser.find_element_by_xpath(
                '/html/body/div[4]/div/form/div[3]/div[5]/button').click()
            logging.info('Ingreso a la app web sin problema')
            try:
                webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/a[2]'))).click()
                logging.info('Selecciono informe principal')
            except:
                logging.info('No selecciono informe principal')
            try:
                webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[10]/div[2]/div[3]/table/tbody/tr[2]/td[2]')))
                browser.find_element_by_xpath(
                    '/html/body/div[10]/div[2]/div[3]/table/tbody/tr[2]/td[2]').click()
                logging.info('Selecciono tipo de datos')
            except:
                logging.info('No selecciono tipo de datos')
            try:
                browser.get(
                    'https://adminfoflex.bancolombia.com.co/vsmart/index.php?rtr=informes&ctr=InformesControlador&acc=&nom_programa=informescompromisos_pagos&filtroaux=sgme')
                logging.info('Cargo pantalla para cargar las variables')
            except:
                logging.info('No cargo pantalla para cargar las variables')
            sleep(2)
            # primera parte
            # sleep(2)
            webdriver = WebDriverWait(browser, 50).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="s2id_agrupador"]/a/span[2]'))).click()
            # #sleep(2)
            webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="select2-drop"]/div/input'))).send_keys('Detalle En Pantalla')
            # #sleep(2)
            webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="select2-drop"]/ul/li/div'))).click()
            # #sleep(2)
            webdriver = WebDriverWait(browser, 50).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="s2id_col"]'))).click()
            # #sleep(2)
            webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="select2-drop"]/div/input'))).send_keys('Código De Abogado')
            # #sleep(2)
            webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="select2-drop"]/ul/li/div'))).click()
            # sleep(2)
            webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="valor"]'))).send_keys(50617)
            webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="btnAgregarCriterio"]'))).click()
            # ================================= Selecion el tercer filtro ==================================================
            webdriver = WebDriverWait(browser, 50).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="s2id_col"]'))).click()
            # # #sleep(2)
            webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="select2-drop"]/div/input'))).send_keys('Fecha Generacion')
            # # #sleep(2)
            webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="select2-drop"]/ul/li/div'))).click()
            webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="btnCalendario"]'))).click()
            DiaAyer = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
            DiaAyer = DiaAyer.split('-')
            year, month, day = int(DiaAyer[0]), int(
                DiaAyer[1]), int(DiaAyer[2])
            calendar.setfirstweekday(6)
            def get_week_of_month(year, month, day):
                x = np.array(calendar.monthcalendar(year, month))
                week_of_month = np.where(x == day)[0][0] + 1
                n = np.where(x[week_of_month-1] == day)
                return week_of_month, x, day, int(n[0])
            week_of_month, x, day, n = get_week_of_month(year, month, day)
            webdriver = WebDriverWait(browser, 40).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[6]/table[1]/tbody[1]/tr['+str(week_of_month)+']/td['+str(n+1)+']/a[1]'))).click()
            webdriver = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="btnAgregarCriterio"]'))).click()
            # tercera parte
            # =================================Generar descargas==================================================
            sleep(3)
            webdriver = WebDriverWait(browser, 50).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="add_tab"]'))).click()
            sleep(5)
            webdriver = WebDriverWait(browser, 150).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/a[3]'))).click()
            sleep(120)
            # #================================= Le da a expoerta A CSV==================================================
            print('exporte csv')
            webdriver = WebDriverWait(browser, 70).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/a[3]'))).click()
            sleep(20)
            try:
                for i in os.listdir(downloadpath):
                    if 'Informe' in i and i.endswith("zip"):
                        remove(downloadpath+i)
            except:
                pass
            print('confirmacion exporte')
            sleep(2)
            webdriver = WebDriverWait(browser, 120).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[3]/input[1]'))).click()
            # =================================Envio a ruta especifica==================================================
            sleep(140)
            try:
                browser.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[3]/div[6]/a/div').click()
                # browser.quit()
            except:
                pass
            print(downloadpath)
            for i in os.listdir(downloadpath):
                if 'Informe' in i and i.endswith('zip'):
                    items = downloadpath+'\\'+i
                    password = None
                    archivo_zip = zipfile.ZipFile(items)
                    print('Saved2')
                    archivo_zip.extractall(downloadpath)
                    archivo_zip.close()
                    os.remove(downloadpath+'\\'+i)
                    DiaAyer = (datetime.now() - timedelta(days=1)
                               ).strftime('%Y-%m-%d')
                items = os.listdir(downloadpath)
                print(items)
                DiaAyer = DiaAyer.split('-')
                DiaAyer = str(DiaAyer[0]+DiaAyer[1]+DiaAyer[2])
                for a in items:
                    if '.csv' in a:
                        b = 'Informe Compromisos_' + DiaAyer+'.csv'
                        os.rename(downloadpath+'\\'+a, downloadpath+'\\'+b)
                        shutil.move(downloadpath+'\\'+b, ruta+'\\'+b)
                        logging.info('Pasa a drop y finaliza OK')
        except:
            pass
        finally:
            browser.quit()
            sleep(10)
            shutil.rmtree(profilepath, ignore_errors=True, onerror=None)
            sleep(30)

        # =================================Deslogueo de la app==================================================
    else:
        import sys
        sys.exit()


if __name__ == '__main__':
    profilepath = path + '\\' + 'ds_Bancolombia_Informe_Compromisos'
    shutil.rmtree(profilepath, ignore_errors=True, onerror=None)
    service = tarsConstruct.TARS_Service(filepath=__file__)
    service.run_service(func=selenium)
