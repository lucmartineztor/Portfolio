import base64
import requests 
import pyodbc
import tarsConstruct
import pandas as pd
import openpyxl 

def Decode():
	g=open('output.txt','rb')
	byte=g.read()
	g.close()

	fh=open('Imagen.jpg','wb')
	fh.write(base64.b64decode(byte))
	fh.close()

def Encode( url_imagen):
	
	nombre_local_imagen = "Imagen.png"
	imagen = requests.get(url_imagen).content
	with open(nombre_local_imagen, 'wb') as handler:
		handler.write(imagen)
	with open('Imagen.png','rb') as imagefile:
		byteform=base64.b64encode(imagefile.read())

	f=open('output.txt','wb')
	f.write(byteform) 
	f.close()
	g=open('output.txt','rb')
	byte=g.read()
	g.close()
	return byte


columns=['picurl', 'client', 'b64logo']
token='6df23324feaf60c2faafef173510512ceb8f87a1e3c4ddda9b'
table= tarsConstruct.read_SQL_table(server='TPCCP-DB128\\SQL2016STD',database='Sandbox',tablename='Table_1', 
	request_token=token, credentials_services=['SQL-TPCCP-DB128'])



def Sing():
	b=[
	('https://revistas.javeriana.edu.co/public/journals/24/cover_issue_1127_es_ES.png','Hospital Universitario San Ignacio','Null'),
	('https://codisenio.com.co/WFMNS/aetna_logo_min.png','Aetna','Null'),
	('https://zenprospect-production.s3.amazonaws.com/uploads/pictures/5ed51e3c82c097000130b909/picture','dzf','Null'),
	('https://revistas.javeriana.edu.co/public/journals/24/cover_issue_1127_es_ES.png','dzf','Null'),
	('https://es.logodownload.org/wp-content/uploads/2020/02/Iberdrola-logo-11.png','dzf','Null'),
	('https://chronos.teleperformance.co/assets/centrales/Orange.svg','Whatsapp CDD','Null')
	]

	df=pd.DataFrame(b, columns=columns)
	tarsConstruct.send_df_to_sql(df,tlname='Table_1',database='Sandbox',schema='dbo',if_exists='replace',
		index=None,dtype=None,credentials_services=['SQL-TPCCP-DB128'], request_token=token)




a=[]

def Convert_to_64(table):
	i=0
	while i<(len(table)):
		try:
			element= (table['picurl'][i], table['client'][i], Encode(table['picurl'][i]))
			a.append(element)
			
		except:
			element= (table['picurl'][i], table['client'][i],table['b64logo'][i])
			a.append(element)
		i=i+1
	df=pd.DataFrame(a,columns=columns)
	df=df.astype(str)	
	tarsConstruct.send_df_to_sql(df,tlname='Table_1',database='Sandbox',schema='dbo',credentials_services=['SQL-TPCCP-DB128'], request_token=token)



def Savedata(table):
	i=0
	while i<(len(table)):
		try:
			element= (table['picurl'][i], table['client'][i], table['b64logo'][i])
			a.append(element)
			
		except:
			print('error')
		i=i+1
	df=pd.DataFrame(a,columns=columns)
	df=df.astype(str)
	df.to_excel('dimLogos.xlsx') 



def Excel_to_sql():
	table=pd.read_excel('dimLogos.xlsx')
	tarsConstruct.send_df_to_sql(table,tlname='Table_1',database='Sandbox',schema='dbo',credentials_services=['SQL-TPCCP-DB128'], request_token=token)



#sing=Sing()
convert_to_64=Convert_to_64(table)
savedata=Savedata(table)
#decode=Decode() 
excel_to_sql=Excel_to_sql()

