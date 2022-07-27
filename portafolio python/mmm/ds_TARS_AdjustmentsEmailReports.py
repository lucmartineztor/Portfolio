""" TARS Library """
import os
import sys
__file__ = os.path.abspath(__file__)
path = os.path.dirname(__file__)
mainpath = os.path.split(path)
sys.path.append(mainpath[0])
import tarsConstruct

""" Libs here -- please include all libs what you need below"""
import win32com.client as win32
import time
import shutil
from zipfile import ZipFile
import logging

def main(downloadpath):
    
    """RPA para el envío por correo electrónico del reporte de ajustes
        Este Rpa está dividido en 7 RPAs diferentes puesto que presenta errores en ejecuciones muy largas
        Cada Rpa envía un máximo de 20 clientes diferentes
    [Proceso]
    1. Lectura del Excel
        Consiste en abrir el archivo de excel que contiene las pivots tables de donde se van a sacar las imágenes que se enviarán en los correos electrónicos.
        Limpiar la carpeta donde se guardan las imagenes que son enviadas en los correos
        Actualizar el excel con los datos del cliente
        Crear una copia .zip del archivo de excel (de este zip se sacan las imágenes)
        Crear otra copia .xlsx del archivo que será adjuntada en el correo electrónico
    2. Creación del Body del correo
        Consiste en crear el body del correo de acuerdo al cliente y a los hallazgos encontrados
        Se extraen las imagenes del archivo .zip creado en el paso anterior
    3. Envío del correo electrónico
        Se envía el correo electrónico con el body creado en el paso anterior y se adjunta la copia de excel creada en el paso 1
        Se elimina la copia del excel creado y del archivo .zip

    [Raise]:
        1. En caso que el archivo de excel sea movido o cambiado de nombre
        2. Este RPA presenta una particularidad y es que muestra algún error si la ejecución tarda mucho tiempo
    """
    
    #------------------------------------
    #MAIN
    #------------------------------------
    
    #------------------------------------
    # VARIABLES DE CONFIGURACION
    #------------------------------------
    
    excel_file_name = r'\Adjustments_Report_RPA_v2.xlsx'
    excel_file_name_copy = r'\Email_Adjustments_Report_RPA_v2.xlsx'
    excel_user='tpco\tarsuser'
    excel_worksheet_name = 'Main'
    
    #########################################################
    #1. Lectura del Excel
    #########################################################
    
    try:
        if not os.path.exists(downloadpath + '\\Sources'):
            os.makedirs(downloadpath + '\\Sources')
        excelfile = downloadpath + '\\Sources'+excel_file_name#Variable con la ruta completa del archivo de excel que se va a leer
        Copy_excelfile = downloadpath + '\\Sources'+excel_file_name_copy#Variable con la ruta completa del archivo de excel que será enviado por correo
        visible = False
        excel = win32.DispatchEx('Excel.Application',userName=excel_user)#Objeto de Excel
        excel.Visible = visible
        excel.ScreenUpdating = visible
        excel.DisplayAlerts = False
        workbook = excel.Workbooks.Open(excelfile)#Objeto con el archivo de excel abierto
        workbook.RefreshAll()#Se refresca el excel para actualizar la lista de clientes
        excel.CalculateUntilAsyncQueriesDone()
        mainsheet = workbook.workSheets(excel_worksheet_name)#Objeto con la hoja principal del excel
        lista  = mainsheet.ListObjects(1).Range.Columns(1).Rows()#Lista de Clientes
        imgfilespath = downloadpath + '\\Images'#Ruta donde se guardarán las imágenes que serán enviadas en los correos
        zipfilename = excelfile[:-5]+'.zip'#Nombre del archivo comprimido
        #Comienza la iteración por cada uno de los clientes
        for lis in lista[1:]:
            logging.info("cleaning temp images folder...")
            files_items = os.listdir(downloadpath+ '\\Images')#Lista de imágenes que hay en la carpeta
            #Se eliminan las imágenes que existan en la ruta para poder guardar las nuevas imágenes
            for item in files_items:
                try:
                    os.remove(os.path.join(downloadpath+ '\\Images',item))
                except:
                    shutil.rmtree(os.path.join(downloadpath+ '\\Images',item), ignore_errors=True, onerror=None)
            lis[0]
            mainsheet.Range('C2').Value = lis[0]#Asignamos a la celda C2 el nombre del Cliente
            time.sleep(1)
            #Se refresca el excel para que se actualice la información con los datos del cliente seleccionado, se hace 2 veces por que hay ocasiones que no actualiza bien
            workbook.RefreshAll()
            excel.CalculateUntilAsyncQueriesDone()
            excel.CalculateUntilAsyncQueriesDone()
            workbook.RefreshAll()
            excel.CalculateUntilAsyncQueriesDone()
            excel.CalculateUntilAsyncQueriesDone()
            lenguaje = mainsheet.Range('C1').Value#Se toma el valor del lenguaje del excel para luego hacer el body en español o inglés
            validatorsheet = workbook.workSheets('Validador')#Hoja del excel donde se encuentran los validadores
            #Los validadores sirven para determinar si hay imágenes que adjuntar en el cuerpo del correo
            additions_val = validatorsheet.Range('A2').Value#Numero de Adiciones
            reductions_val = validatorsheet.Range('C2').Value#Numero de Reducciones
            absent_justified_val = validatorsheet.Range('E2').Value#Numero de Ausencias Justificadas
            logging.info("verifiying zip file creation")
            excel.ActiveWorkbook.SaveCopyAs(zipfilename)#Se guarda copia en formato Zip
            excel.CalculateUntilAsyncQueriesDone()
            excel.ActiveWorkbook.SaveCopyAs(Copy_excelfile)#Se guarda copia en formato xlsx
            excel.CalculateUntilAsyncQueriesDone()
            logging.info(".zip file created")
            
            #########################################################
            #2. Creación del Body del correo
            #########################################################
            
            dest  = mainsheet.Range('C3').Value#Lista de destinatarios
            x=0#Variable que irá incrementando por cada imagen que se adjuntará en el correo
            """ If there are no reductions, the images from the
                pivot table are not update. Therefore, they must be skipped.
                The first 2 images are reductions, the next 2 are additions, and the last 2 are abs paid.
                The zip duplicate the images, so there are actually 12 following the same order. """
            
            if lenguaje.lower() == 'español':
                subject = lis[0] + ' | Report | Reporte de ajustes | FS'
                body="""
                        <br>
                        Buen día
                        <br>
                        Comparto el reporte de time adjustment para la fecha $$$DATE--HERE$$$
                        <br>"""
                if reductions_val != None:
                    body += """
                    <br>
                    <b>Ajustes de Reducción:</b> en la siguiente imagen podrán ver la cantidad de horas de ajustes por reducción que llevamos para este mes y el respectivo ranking de tipos de ajuste, ACCM, Supervisor y Agente por CCMS_ID 
                    <br>
                    """
                    x+=1
                    body += """
                    $$$IMAGE"""+str(x)+"""--HERE$$$
                    """
                    x+=1
                    body +="""
                    <br>
                    $$$IMAGE"""+str(x)+"""--HERE$$$
                    """
                else:
                    body += """
                            <br>
                            <br>
                            <b>Ajustes de Reducción:</b> en la siguiente imagen podrán ver la cantidad de horas de ajustes por reducción que llevamos para este mes y el respectivo ranking de tipos de ajuste, ACCM, Supervisor y Agente por CCMS_ID 
                            <br>
                            <br>
                            <br>
                            <br>
                            NO Data
                            <br>
                            <br>
                            """
                if additions_val != None:
                    body +="""
                    <br>
                    <b>Ajustes de Adición:</b> en la siguiente imagen podrán ver la cantidad de horas de ajustes por adición que llevamos para este mes y el respectivo ranking de tipos de ajuste, ACCM, Supervisor y Agente por CCMS_ID .
                    <br>
                    """
                    x+=1
                    body += """
                    $$$IMAGE"""+str(x)+"""--HERE$$$
                    """
                    x+=1
                    body +="""
                    <br>
                    $$$IMAGE"""+str(x)+"""--HERE$$$
                    """
                else:
                    body += """
                            <br>
                            <b>Ajustes de Adición:</b> en la siguiente imagen podrán ver la cantidad de horas de ajustes por adición que llevamos para este mes y el respectivo ranking de tipos de ajuste, ACCM, Supervisor y Agente por CCMS_ID .
                            <br>
                            <br>
                            <br>
                            <br>
                            NO Data
                            <br>
                            <br>
                            """
                if absent_justified_val != None:
                    body +="""
                    <br>
                    <b>Horas de Ausentismo Pagadas:</b> en la siguiente imagen podrán ver la cantidad de horas de ajustes por adicción que están pegando en ausentismo, debido a fallas en la actualización de TP_adherence o por que se realizó el ajuste fuera de los tiempos establecidos.
                    <br>
                    """
                    x+=1
                    body += """
                    $$$IMAGE"""+str(x)+"""--HERE$$$
                    """
                    x+=1
                    body +="""
                    <br>
                    $$$IMAGE"""+str(x)+"""--HERE$$$
                    """
                else:
                    body += """
                            <br>
                            <b>Horas de Ausentismo Pagadas:</b> en la siguiente imagen podrán ver la cantidad de horas de ajustes por adicción que están pegando en ausentismo, debido a fallas en la actualización de TP_adherence o por que se realizó el ajuste fuera de los tiempos establecidos.
                            <br>
                            <br>
                            <br>
                            <br>
                            NO Data
                            <br>
                            <br>
                            """
            else:
                subject = lis[0] + ' | Report | Adjustments report | FS'
                body="""
                    <br>
                    Good day Team
                    <br>
                    I share the time adjustment report for the date $$$DATE--HERE$$$
                    <br>
                    """
                if reductions_val != None:
                    body += """
                    <br>
                    <b>Reduction Adjustments:</b> in the following image you can see the number of hours of reduction adjustments that we have for this month and the respective ranking of types of adjustment, ACCM, Supervisor and Agent by CCMS_ID.
                    <br>
                    """
                    x+=1
                    body += """
                    $$$IMAGE"""+str(x)+"""--HERE$$$
                    """
                    x+=1
                    body +="""
                    <br>
                    $$$IMAGE"""+str(x)+"""--HERE$$$
                    """
                else:
                    body += """
                            <br>
                            <b>Reduction Adjustments:</b> in the following image you can see the number of hours of reduction adjustments that we have for this month and the respective ranking of types of adjustment, ACCM, Supervisor and Agent by CCMS_ID.
                            <br>
                            <br>
                            <br>
                            <br>
                            NO Data
                            <br>
                            <br>
                            """
                if additions_val != None:
                    body +="""
                    <br>
                    <b>Addition Adjustments:</b> in the following image you can see the number of hours of adjustments by addition that we have for this month and the respective ranking of types of adjustment, ACCM, Supervisor and Agent by CCMS_ID.
                    <br>
                    """
                    x+=1
                    body += """
                    $$$IMAGE"""+str(x)+"""--HERE$$$
                    """
                    x+=1
                    body +="""
                    <br>
                    $$$IMAGE"""+str(x)+"""--HERE$$$
                    """
                else:
                    body += """
                            <br>
                            <b>Addition Adjustments:</b> in the following image you can see the number of hours of adjustments by addition that we have for this month and the respective ranking of types of adjustment, ACCM, Supervisor and Agent by CCMS_ID.
                            <br>
                            <br>
                            <br>
                            <br>
                            NO Data
                            <br>
                            <br>
                            """
                if absent_justified_val != None:
                    body +="""
                    <br>
                    <b>Paid Absenteeism Hours:</b> in the following image you can see the number of hours of addiction adjustments that are hitting absenteeism, due to failures in the TP_adherence update or because the adjustment was made outside the established times.
                    <br>
                    """
                    x+=1
                    body += """
                    $$$IMAGE"""+str(x)+"""--HERE$$$
                    """
                    x+=1
                    body +="""
                    <br>
                    $$$IMAGE"""+str(x)+"""--HERE$$$
                    """
                else:
                    body += """
                            <br>
                            <b>Paid Absenteeism Hours:</b> in the following image you can see the number of hours of addiction adjustments that are hitting absenteeism, due to failures in the TP_adherence update or because the adjustment was made outside the established times.
                            <br>
                            <br>
                            <br>
                            <br>
                            NO Data
                            <br>
                            <br>
                            """
            receipts = []
            receipts = dest.split(',')
            receipts.append('Jonathan.AcevedoZapata@teleperformance.com')
            sendto= receipts
            ccto=[]
            bodyimgcant = x#Numero total de imágenes
            #Se extraen la anchura y altura de las imágenes que serán enviadas
            imageswidth_t,imagesheight_t = tarsConstruct.extract_images_from_zip(zipfilename,imagespath=imgfilespath,imgchunk=6)
            files_items = os.listdir(downloadpath+ '\\Images')#Lista de imágenes
            imageswidth = []#Lista para ir guardando las anchuras de las imágenes
            imagesheight = []#Lista para ir guardando las alturas de las imágenes
            if reductions_val == None:#Si no hay reducciones se eliminan las dos primeras imágenes, de lo contrario se añaden las alturas y anchuras a la lista respectiva
                os.remove(os.path.join(downloadpath+ '\\Images',files_items[0]))
                os.remove(os.path.join(downloadpath+ '\\Images',files_items[1]))
            else:
                imageswidth.append(imageswidth_t[0])
                imagesheight.append(imagesheight_t[0])
                imageswidth.append(imageswidth_t[1])
                imagesheight.append(imagesheight_t[1])
            if additions_val == None:#Si no hay adiciones se eliminan las dos siguientes imágenes, de lo contrario se añaden las alturas y anchuras a la lista respectiva
                os.remove(os.path.join(downloadpath+ '\\Images',files_items[2]))
                os.remove(os.path.join(downloadpath+ '\\Images',files_items[3]))
            else:
                imageswidth.append(imageswidth_t[2])
                imagesheight.append(imagesheight_t[2])
                imageswidth.append(imageswidth_t[3])
                imagesheight.append(imagesheight_t[3])
            if absent_justified_val == None:#Si no hay ausencias no justificadas se eliminan las dos siguientes imágenes, de lo contrario se añaden las alturas y anchuras a la lista respectiva
                os.remove(os.path.join(downloadpath+ '\\Images',files_items[4]))
                os.remove(os.path.join(downloadpath+ '\\Images',files_items[5]))
            else:
                imageswidth.append(imageswidth_t[4])
                imagesheight.append(imagesheight_t[4])
                imageswidth.append(imageswidth_t[5])
                imagesheight.append(imagesheight_t[5])
            files_items = os.listdir(downloadpath+ '\\Images')#Lista con las imagenes definitivas que se enviarán en el correo
            y = 0#Iniciacio de variable que servirá para renombrar y enumerar las imágenes
            for item in files_items:
                y+=1
                os.rename(os.path.join(downloadpath+ '\\Images',item),os.path.join(downloadpath+ '\\Images','image0'+str(y)+'.png'))
            #Creacion del body definitivo con las imágenes
            body, bodyimgfiles = tarsConstruct.body_config(body,bodyimgcant,imgfilespath=imgfilespath,
                                                                            imageswidth=imageswidth,
                                                                            imagesheight=imagesheight,
                                                                            time_delay=0,
                                                                            date_delay=0,
                                                                            banner_id=1)
            
            #########################################################
            #3. Envío del correo electrónico
            #########################################################
            
            files = [Copy_excelfile]
            subject = 'TPMAR | ' + subject 
            tarsConstruct.send_mail(sendto, ccto, subject,body, market=1, files=files, use_tls=True, imgfiles=bodyimgfiles)
            #Eliminacion del archivo Zip y del excel enviado por correo
            if os.path.exists(zipfilename):
                os.remove(zipfilename)
            if os.path.exists(Copy_excelfile):
                os.remove(Copy_excelfile)
    except Exception as e:
        logging.exception(e)
        print(str(e))
        excel.ScreenUpdating = True
        excel.DisplayAlerts = True
        if visible == False:
            excel.Visible = not visible
        workbook.Close(False)
        excel.Quit()
    finally:
        excel.ScreenUpdating = True
        excel.DisplayAlerts = True
        if visible == False:
            excel.Visible = not visible
        workbook.Close(False)
        excel.Quit()
        
if __name__ == '__main__':
    service = tarsConstruct.TARS_Service(filepath=__file__)
    service.run_service(func = main)