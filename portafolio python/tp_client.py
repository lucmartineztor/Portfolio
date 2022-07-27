import requests 
import pyodbc
import tarsConstruct
import pandas as pd
import openpyxl 


token='649ab0e2c2467d1d38235bdfc6ac02b42a87cbe99ab12ba3e5'


def Get_data_dimlogs():
	
	table= tarsConstruct.read_SQL_table(server='TPCCP-DB128\\SQL2016STD',database='MessengerService',tablename='dimLogos', 
	request_token=token, credentials_services=['SQL-TPCCP-DB128'])
	columns=['picurl','client','b64logo']
	a=[]
	i=0
	while i<(len(table)):
		try:
			element= (table['picurl'][i],table['client'][i],table['b64logo'][i])
			a.append(element)
			
		except:
			print('error en Get_data_dimlogs ')
		i=i+1
	df=pd.DataFrame(a,columns=columns)
	df=df.astype(str)
	return df
 


def Get_data_NETapp():
	
	table= tarsConstruct.read_SQL_table(server='TPCCP-DB128\\SQL2016STD',database='LoginMaster',tablename='tbClient', 
	request_token=token, credentials_services=['SQL-TPCCP-DB128'])
	columns=['client','idccms']
	a_Net=[]
	i=0
	while i<(len(table)):
		try:
			element= (table['fullname'][i],table['id'][i])
			a_Net.append(element)
			
		except:
			print('error en Get_data_NETapp')
		i=i+1
	df_Net=pd.DataFrame(a_Net,columns=columns)
	df_Net=df_Net.astype(str)
	return df_Net


def Get_data_Login_Master():
	
	table= tarsConstruct.read_SQL_table_HC(server='TPCCP-DB128\\SQL2016STD',database='NETapp',tablename='tbClientApp', 
	request_token=token, credentials_services=['SQL-TPCCP-DB128'])
	columns=['client','idccms']
	a_Log=[]
	i=0
	while i<(len(table)):
		try:
			element= (table['fullname'][i],table['idclient_ccms'][i])
			a_Log.append(element)
			
		except:
			print('error en Get_data_Login_Master')
		i=i+1
	df_Log=pd.DataFrame(a_Log,columns=columns)
	df_Log=df_Log.astype(str)
	return df_Log



def Join_dim_Net_Log_Total():
	
	Merge_,columns=Join_dim_Net_Log()
	k=[]
	
	for i in range(0,len(Merge_['idccms_x']),1):
	
		if Merge_['idccms_x'][i]==Merge_['idccms_y'][i]:
			element=(Merge_['idccms_x'][i],Merge_['picurl'][i],Merge_['client'][i],Merge_['b64logo'][i])
			k.append(element)
		elif Merge_['idccms_x'][i]!=Merge_['idccms_y'][i] and str(Merge_['idccms_x'][i])=='nan':
			element=(Merge_['idccms_y'][i],Merge_['picurl'][i],Merge_['client'][i],Merge_['b64logo'][i])
			k.append(element)
		elif Merge_['idccms_x'][i]!=Merge_['idccms_y'][i] and str(Merge_['idccms_y'][i])=='nan':
			element=(Merge_['idccms_x'][i],Merge_['picurl'][i],Merge_['client'][i],Merge_['b64logo'][i])
			k.append(element)


	df_Join=pd.DataFrame(k,columns=columns)
	df_Join=df_Join.astype(str)
	
	tarsConstruct.send_df_to_sql(table,tlname='Table_1',database='Sandbox',schema='dbo',credentials_services=['SQL-TPCCP-DB128'], request_token=token)


def Join_dim_Net_Log():
	columns=['idccms','picurl','client','b64logo']
	df_Log=Get_data_Login_Master()
	df_Net=Get_data_NETapp()
	df=Get_data_dimlogs()
	merge=pd.merge(df,df_Net,on='client',how='left')
	Merge_=pd.merge(merge,df_Log,on='client',how='left')
	print()
	
	#tarsConstruct.send_df_to_sql(Merge_,tlname='Table_1',database='Sandbox',schema='dbo',credentials_services=['SQL-TPCCP-DB128'], request_token=token)
	return Merge_,columns


def Update_nan():
	try:
		conn = pyodbc.connect('Driver={SQL Server};''Server=TPCCP-DB128\\SQL2016STD;''Database=MessengerService;''Trusted_Connection=yes;')
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM dbo.dimLogos WHERE client ='BancolombiaCobranzas'")
		data=cursor.fetchall()
		
		cursor.execute("UPDATE MessengerService.dbo.dimLogos SET idccms='3685' WHERE client='BancolombiaCobranzas'")
		
		cursor.execute("UPDATE MessengerService.dbo.dimLogos SET idccms='532' WHERE client='General Motors On Star'")
		
		cursor.execute("UPDATE MessengerService.dbo.dimLogos SET idccms='3250' WHERE client='MarketingPersonal'")
		
		cursor.execute("UPDATE MessengerService.dbo.dimLogos SET idccms='3632' WHERE client='Rebel'")
		
		cursor.execute("UPDATE MessengerService.dbo.dimLogos SET idccms='3632' WHERE client='Rebel EMEA'")
		
		cursor.execute("UPDATE MessengerService.dbo.dimLogos SET idccms='3632' WHERE client='Rebel USC'")
		conn.commit()

		
	except Exception as e:
		print(e)

def Savedata():
	df=Get_data_dimlogs()
	df.to_excel('dimLogos_2.xlsx') 



def Excel_to_sql():
	table=pd.read_excel('dimLogos.xlsx')
	tarsConstruct.send_df_to_sql(table,tlname='Table_1',database='Sandbox',schema='dbo',credentials_services=['SQL-TPCCP-DB128'], request_token=token)
	
#Join_dim_Net_Log()
Join_dim_Net_Log_Total()
Update_nan()













# def New_Database():
# 	a_Net=Get_data_NETapp()
# 	a=Get_data_dimlogs()
# 	b=[]
# 	#print("a",a)
# 	for i in a:
# 		for j in a_Net:
# 			if i==j:
# 				b.append(i)
# 	for i in b:
# 		if i in a: 
# 			a.remove(i)

# 	for i in b:
# 		if i in a_Net: 
# 			a_Net.remove(i)
		
# 	print("a",a)
# 	print("a_Net",a_Net)