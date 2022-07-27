
import logging
import os
import sys
__file__ = os.path.abspath(__file__)
path = os.path.dirname(__file__)
mainpath = os.path.split(path)
sys.path.append(mainpath[0])
import tarsConstruct_debugs_
import win32com.client as win32
import time
import win32api
import win32com
import tarsConstruct
global body

def send(body,Body,bodyimgfiles,excelfile):
	bodyimgfile=[]
	#print(bodyimgfiles)
	outlook=win32.Dispatch("Outlook.Application")
	namespace=outlook.GetNameSpace("MAPI")
	message=outlook.createItem(0)
	message.Display()
	for i in os.listdir(bodyimgfiles):
		
		fileName=i
		i=os.path.join(bodyimgfiles,fileName)
		bodyimgfile.append(i)
	account=namespace.Folders("Lucia.MartinezTorres@teleperformance.com")
	#inbox=account.Folders("Inbox")

	#for i in array:
		#print("esto es",i)
	
	message.To="yuli.suarezrodriguez@teleperformance.com"
	message.Subject="prueba"
	message.Attachments.Add(str(bodyimgfile[0]))
	message.save()
	message.Attachments.Add(str(bodyimgfile[1]))
	message.save()
	message.Attachments.Add(str(bodyimgfile[2]))
	message.save()
	message.Attachments.Add(str(bodyimgfile[3]))
	message.save()
	message.Attachments.Add(str(excelfile))
	message.Body = body
	message.save()
	time.sleep(5)
	message.htmlBody = '<html><body><h1>'+str(body)+'</h1><img src="'+str(bodyimgfile[0])+'" width =40%><br><img src="'+str(bodyimgfile[1])+'"width =40%><br><img src="'+str(bodyimgfile[2])+'" width =30%><br><img src="'+str(bodyimgfile[3])+'"width =40%><h1 dir="ltr" style="font-size:12pt;color:#000000;background-color:#FFFFFF;font-family:Calibri,Arial,Helvetica,sans-serif;">'+str(Body)+'</h1></body></html>'
	#message.htmlBody = '<img src="C:\\Users\\martineztorres.55\\Desktop\\mios\\Sources\\Images\\image01.png" height = 50% >'
	message.save()
	#message.Body=bodyimgfiles[1]
	#message.To="dibey.munozrodriguez@teleperformance.com"
	

	message.save()
	
	#message.Send()

	print('message sent')
def main(downloadpath,excelfile,excel):
	try:
		if not os.path.exists(downloadpath + '\\Sources'):
			os.makedirs(downloadpath + '\\Sources')
		#excelfile = downloadpath + '\\Sources'+r'\POC Reports.xlsx'
		visible = True
		#excel = win32.DispatchEx('Excel.Application')
		excel.Interactive = False
		excel.Visible = visible
		excel.ScreenUpdating = visible
		excel.DisplayAlerts = False

		workbook = excel.Workbooks.Open(excelfile)
		zipfile = excelfile[:-5]+'.zip'

		mainsheet= workbook.Worksheets('Reducciones y Adiciones')

		#print(win32api.FormatMessage(-2147352565))
		#mainsheet.Range("A1: O96").CopyPicture()
		#mainsheet.Paste()

		imgfilespath = downloadpath + '\\Sources'+'\\Images'
		zipfile = excelfile[:-5]+'.zip'
		reductions_val = mainsheet.Range('E11:O17').Value
		reductions_val=reductions_val[6]
		excel.ActiveWorkbook.SaveAs(zipfile)
		
		#lista  = mainsheet.ListObjects(1).Range.Columns(2).Rows()
		#print(mainsheet.ListObjects(2))
		x=3
		subject =  ' | Reporte de ajustes'
		body="""
			<br>
			Teams,
			<br>
			Les comparto la información de Reducciones y Adiciones para la campaña de  a corte $$$DATE--HERE$$$.
			
			"""
		
		#body += """
		#$$$IMAGE"""+str(x)+"""--HERE$$$
		#"""	
		
		if reductions_val != None:
			
			x+=1
			#body += """
			#$$$IMAGE"""+str(x)+"""--HERE$$$
			#"""	

			Body = """

			<br>
			Recuerden que pueden encontrar información más detallada por servicio, agente o día en el enlace:
			<br>
			Colocar aca enlace
			<br>
			<b>Terminos:</b>
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

		bodyimgcant = x
		imageswidth,imagesheight = tarsConstruct_debugs_.extract_images_from_zip(zipfile,imagespath=imgfilespath,imgchunk=bodyimgcant)
		request_token='82e99ea2307ff0f22b128ca7f4dffd0db178aee7b69ecc7b70'
		body, bodyimgfiles = tarsConstruct_debugs_.body_config(body,bodyimgcant,imgfilespath=imgfilespath,
																		imageswidth=imageswidth,
																		imagesheight=imagesheight,
																		timedelta=0,
																		datedelta=0,
																		banner_id=1,
																		request_token=request_token,
																		credentials_services=['SQL-TPCCP-DB128']
																		)

		time.sleep(30)
		files = [excelfile]
		receipts =[]
		receipts.append('lucia.martineztorres@teleperformance.com')
		sendto= receipts
		ccto=[]
		subject = 'prueba'
		try:
			ws2 = workbook.Worksheets('IMAGES')
			ws2.Delete()
			workbook.Save()
		except:
			pass
		send(body,Body,imgfilespath,excelfile)
		#tarsConstruct_debugs_.send_mail(sendto, ccto, subject,body, market=1,request_token=request_token,
																		#credentials_services=['SQL-TPCCP-DB128'], files=files, use_tls=True, imgfiles=bodyimgfiles)    
	finally:
		# excel.EnableEvents = True

		excel.ScreenUpdating = True
		excel.DisplayAlerts = True
		if visible == False:
			excel.Visible = not visible
		workbook.Close(False)
		excel.Quit()
#main('C:\\Users\\martineztorres.55\\Desktop\\mios')


def Copy_Sheet(downloadpath):
	#from PIL import ImageGrab
	if not os.path.exists(downloadpath + '\\Sources'):
		os.makedirs(downloadpath + '\\Sources')
	excelfile = downloadpath + '\\Sources'+r'\POC Reports.xlsx'
	visible = True
	excel = win32.DispatchEx('Excel.Application')
	#excel = win32.Dispatch('Excel.Application')
	excel.Interactive = False
	excel.Visible = visible
	excel.ScreenUpdating = visible
	excel.DisplayAlerts = False

	workbook = excel.Workbooks.Open(excelfile)
	
	#si = workbook.SlicerCaches['Slicer_Campaña'].ClearManualFilter()
	si=workbook.SlicerCaches('Slicer_Campaña').SourceName
	print(si)
	si=workbook.SlicerCaches('Slicer_Campaña').SourceType
	si=workbook.SlicerCaches('Slicer_Campaña').PivotTables()
	
	#print(workbook.SlicerCaches['Slicer_Campaña'].Slicers['Campaña'])
	
	#workbook.SlicerCaches('Slicer_Campaña').SlicerItems
	#.SlicerItems[1].Selected = False
	#print(si)
	for i in range (1,9):
		try:
			si = workbook.SlicerCaches(i).Name
			print(si)
			si = workbook.SlicerCaches[i].SlicerItems(Index=1)
			print(si)
			si =workbook.SlicerCaches(i).VisibleSlicerItemsList
			print(si)
		except:
			pass
	zipfile = excelfile[:-5]+'.zip'

	mainsheet= workbook.Worksheets('Reducciones y Adiciones')
	#sl = mainsheet.SlicerCaches
	reductions_val = mainsheet.Range('E17:O211').CopyPicture()
	try:
		ws2 = workbook.Worksheets('IMAGES')
		ws2.Delete()
		workbook.Save()
	except:
		pass
	wb = excel.Worksheets.Add()
	wb.Name='IMAGES'
	ws2 = workbook.Worksheets('IMAGES')
	ws2.Paste()
	workbook.Save()


	mainsheet= workbook.Worksheets('Reducciones y Adiciones')
	lista  = mainsheet.ListObjects(1).Range.Columns(1).Rows()
	print(lista)
	reductions_val = mainsheet.Range('E1:O16').CopyPicture()
	ws2 = workbook.Worksheets('IMAGES')
	ws2.Paste()

	mainsheet= workbook.Worksheets('Reducciones y Adiciones')
	reductions_val = mainsheet.Range('S5:W16').CopyPicture()
	ws2 = workbook.Worksheets('IMAGES')
	ws2.Paste()

	mainsheet= workbook.Worksheets('Reducciones y Adiciones')
	reductions_val = mainsheet.Range('S17:V32').CopyPicture()
	ws2 = workbook.Worksheets('IMAGES')
	ws2.Paste()

	#main(downloadpath, excelfile, excel)


	
	

#send()
Copy_Sheet('C:\\Users\\martineztorres.55\\Desktop\\mios')

def Cambio_Campanna(downloadpath):
	import xlwings as xw
	xl_app = xw.App(visible=True, add_book=False)
	wb = xl_app.books.open(downloadpath)
	sht = wb.sheets[1]
	from pyxll import xl_macro
	@xl_macro
	def SlicerSelection():
		xlcAlert("Hello")

	slicerSelect = wb.macro('SlicerSelection').SlicerItems
	slicerSelect("Stripe")
	#print(a)

	wb.close()
	xl_app.quit()
	
	pass

def change_params_query(downloadpath):
	import xlrd
	downloadpath=downloadpath+ '\\Sources'+r'\POC Reports.xlsx'
	wb = xlrd.open_workbook(downloadpath)
	sheet = wb.sheet_by_index(1)  
	print(sheet.cell_value(0, 0))
	print('of') 
#Cambio_Campanna('C:\\Users\\martineztorres.55\\Desktop\\mios\\Sources\\POCReport.xlsm')
#El archivo tiene que ser .xlsm

#change_params_query('C:\\Users\\martineztorres.55\\Desktop\\mios')