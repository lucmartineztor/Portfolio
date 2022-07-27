
import logging
import os
import sys
__file__ = os.path.abspath(__file__)
path = os.path.dirname(__file__)
mainpath = os.path.split(path)
sys.path.append(mainpath[0])
import tarsConstruct
import win32com.client as win32
import time
import win32api
request_token='baeaea86616393fb58359b355c0f98f5058cfde250968001a8'
import win32api




def main(downloadpath):
    try:
        if not os.path.exists(downloadpath + '\\Sources'):
            os.makedirs(downloadpath + '\\Sources')
        excelfile = downloadpath + '\\Sources'+r'\_TpAdherence.xlsx'
        visible = True
        excel = win32.DispatchEx('Excel.Application')
        excel.Interactive = False
        excel.Visible = visible
        excel.ScreenUpdating = visible
        excel.DisplayAlerts = False
        workbook = excel.Workbooks.Open(excelfile)
        mainsheet= workbook.Worksheets('Set Up')
        
        #print(win32api.FormatMessage(-2147352565))

        imgfilespath = downloadpath + '\\Sources'+'\\Images'
        zipfile = excelfile[:-5]+'.zip'
        print(zipfile)
        lista  = mainsheet.ListObjects(1).Range.Columns(2).Rows()
        for lis in lista[1:]:

            #get image from excel to IMAGES

            validatorsheet = workbook.Sheets('Adherence')
            reductions_val = validatorsheet.Range('B1:R66')
            validatorsheet = workbook.Worksheets('Set Up')
            


            logging.info("cleaning temp images folder...")
            print("cleaning temp images folder...")
            files_items = os.listdir(downloadpath+ '\\Sources'+'\\Images')
            # for item in files_items:
            #     try:
            #         os.remove(os.path.join(downloadpath+ '\\Sources'+'\\Images',item))
            #     except:
            #         shutil.rmtree(os.path.join(downloadpath+ '\\Sources'+'\\Images',item), ignore_errors=True, onerror=None)
            # if os.path.exists(zipfile):
            #     os.remove(zipfile)
            lis[0]
            print(lis)
            mainsheet.Range('B3').Value = lis[0]
            print(lis[0])
            time.sleep(1)

            #workbook.RefreshAll()
            #excel.CalculateUntilAsyncQueriesDone()
            #excel.ActiveWorkbook.Save()
            #excel.CalculateUntilAsyncQueriesDone()
            #workbook.RefreshAll()
            excel.CalculateUntilAsyncQueriesDone()
            #excel.ActiveWorkbook.Save()
            #excel.CalculateUntilAsyncQueriesDone()
            print("workbook refreshed")
            #lenguaje = mainsheet.Range('C1').Value
            validatorsheet = workbook.Worksheets('Adherence')
            reductions_val = validatorsheet.Range('B14','R14').Value
            reductions_val=reductions_val[0]
            print(reductions_val)
            Client = validatorsheet.Range('B15').Value
            validatorsheet = workbook.Worksheets('Set Up')

            print("verifiying zip file creation")
            logging.info("verifiying zip file creation")
            excel.ActiveWorkbook.SaveAs(zipfile)
            excel.CalculateUntilAsyncQueriesDone()
            excel.ActiveWorkbook.SaveAs(excelfile,FileFormat=51)
            print(".zip file created")
            logging.info(".zip file created")
            excel.CalculateUntilAsyncQueriesDone()
            
            x=0
            subject = lis[0] + ' | Reporte de ajustes'
            body="""
                    <br>
                    Teams,
                    <br>
                    Les comparto la información de adherencia para la campaña de """+Client+""" a corte $$$DATE--HERE$$$, en la cual podrán validar los resultados por LOB.
                    <br>
                    <b>Tener en cuenta:</b>
                    <br>
                    •   Con el nuevo proceso es muy importante que las novedades de incapacidades largas, licencias, permisos y vacaciones sean reportadas con antelación (MyTP). Esto con el fin de evitar afectaciones, pues se debe cargar un Overlay que debe ser ejecutado a -1 día y siempre a futuro
                    <br>
                    •   Sí se presenta un <b>retiro, incapacidad</b> o novedad que afecte la programación o lo planificado, ésta impactará de manera negativa la semana en curso, de ser necesario se debe enviar la solicitud para desprogramar el turno durante el tiempo que sea requerido.
                    """

            if reductions_val != None:
                
                x+=1
                body += """
                $$$IMAGE"""+str(x)+"""--HERE$$$
                """
        
                body += """
                <html>
                <body>

                <br>
                Recuerden que pueden encontrar información más detallada por servicio, agente o día en el enlace:
                <br>
                https://tpcompass.teleperformance.co/
                <br>
                <br>
                <b>Terminos:</b>
                <br>
                •   <b>Scheduled:</b> cantidad de horas programadas en CCMS. No incluye la hora del almuerzo como parte del turno.
                <br>
                •   <b>Worked: </b>cantidad de horas registradas en CMS Avaya
                <br>
                •   <b>% de conformidad:</b> proporción de tiempo registrado en relación con las horas programadas.
                <br>
                •  <b> % de adherencia:</b> proporción de tiempo registrado dentro del programa en relación con las horas programadas.
                <br>
                •   <b>Horas adheridas:</b> cantidad de horas registradas en el turno.
                <br>
                •   <b>Absent:</b> cantidad de horas ausentes.
                <br>
                •   <b>% Absent:</b> Porcentaje de horas ausentes.
                <br>
                •   <b>Tardy:</b> cantidad de horas con retraso.
                <br>
                •   <b>% Tardy:</b> Porcentaje de horas con retraso.
                <br>
                •   <b>Missed inshift:</b> Desconexiones intraturno.
                <br>
                •   <b>% Missed inshift:</b> Porcentaje de desconexiones intraturno.
                <br>
                •   <b>Early:</b> Cantidad de horas con salida anticipada.
                <br>
                •   <b>% Early:</b> Porcentaje de horas con salida anticipada.
                <br>
                •   <b>Missed total:</b> Suma de ausencia, tardanza, desconexiones intraturno y horas de salida anticipada que representa el total de horas que afecta el porcentaje de cumplimiento.
                <br>
                •   <b>% Missed total:</b> Porcentaje de la suma de ausencia, tardanza, desconexiones intraturno y horas de salida anticipada que representa el total de horas que afecta el porcentaje de cumplimiento

                </body>
                </html>"""
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
                
            #receipts = dest.split(',')
            #receipts.append('Juan.GomezInfante@teleperformance.com')
            #sendto= receipts
            #ccto=[]
            bodyimgcant = x
            imageswidth,imagesheight = tarsConstruct.extract_images_from_zip(zipfile,imagespath=imgfilespath,imgchunk=bodyimgcant)
            body, bodyimgfiles = tarsConstruct.body_config(body,bodyimgcant,imgfilespath=imgfilespath,
                                                                            imageswidth=imageswidth,
                                                                            imagesheight=imagesheight,
                                                                            timedelta=0,
                                                                            datedelta=0,
                                                                            banner_id=1,
                                                                            #request_token=request_token,
                                                                            #credentials_services=['SQL-TPCCP-DB128']
                                                                            )


            #====================================================================================================================================
            # Sending Email
            # files = [excelfile]
            #tarsConstruct.send_mail(sendto, ccto, subject,body, market=1, files=files, use_tls=True, imgfiles=bodyimgfiles)
    # except Exception as e:
    #     print(str(e))
    #     excel.ScreenUpdating = True
    #     excel.DisplayAlerts = True
    #     # excel.EnableEvents = True
    #     if visible == False:
    #         excel.Visible = not visible
    #     workbook.Close(False)
    #     excel.Quit()
    #     del excel
    finally:
        # excel.EnableEvents = True
        excel.ScreenUpdating = True
        excel.DisplayAlerts = True
        if visible == False:
            excel.Visible = not visible
        workbook.Close(False)
        excel.Quit()
        #del excel
 
main('C:\\Users\\martineztorres.55\\Desktop\\DownloadService')

