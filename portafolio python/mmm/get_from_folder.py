from datetime import datetime
import pandas as pd
import tarsConstruct
import logging 
from sqlalchemy.types import String
import sys
import zipfile
from os import remove
import os
import numpy as np

items = os.listdir('C:\\Users\\martineztorres.55\\Desktop\\mios')
print(items)
m=0
frames=['df1','df2','df3','df4','df5','df6']
while m<=5:
	for i in items:
		if 'Cabify Vouchers' in i:
			print(i)
			k=str(os.path.splitext(i)[:-1])

			j='C:\\Users\\martineztorres.55\\Desktop\\mios\\lll\\'+str(os.path.splitext(i)[:-1])+'.zip'
			zf = zipfile.ZipFile(j, mode="w")
			zf.write(i, compress_type=zipfile.ZIP_DEFLATED)
			zf.close()
			#remove(i)

		
		elif 'summary' in i:
			df = pd.read_excel(i)
			if 'Teledatos' in i or 'Nearshore Medellin Taxi' in i:
				print(i)
				
				df=df.rename(columns={'Código ticket':'sale code',
					'Nombre del cliente':"Client's name",
					'Código tributario del cliente':"Client's tax code",
					'Cargo del cliente':"Client's role",
					'Solicitado por':"Requested by",
					'Código empleado solicitante':"Employee user code",
					'Divisa':"Currency",
					'Importe':"Price",
					'Descuento':"Discount",
					'Precio total tras descuento':"Total after discount",
					'Precio base':"Base price",
					'Precio por tiempo de espera':"Price for Waiting Time",
					'Suplementos':"Billed supplement",
					'Hora de inicio del viaje':"Start time",
					'Pasajero':"Rider's name",
					'Código de empleado del pasajero':"rider employee code",
					'Email del pasajero':"Rider's email",
					'Punto de salida':"Pick up point",
					'Paradas':"Stops",
					'Punto de destino':"Destination",
					'Región':"Region name",
					'Tipo de petición':"Type of request",
					'Estado final':"Final state",
					'Departamento del pasajero':"User department",
					'Centro de coste del pasajero':"Charge code used by passenger",
					'Centro de coste':"Charge Code",
					'Mensaje para el conductor':"Message for driver",
					'Conductor':"Driver",
					'Tipo de vehículo':"Type of vehicle",
					'Modelo de vehículo':"Vehicle model",
					'Tiempo de espera conductor (min)':"Driver waiting time (mins)",
					'Distancia (km)':"Distance (km)",
					'Hora de recepción de la petición':"Hired at",
					'Hora de llegada al punto de salida':"Arrived at the pick up point",
					'Hora de salida':"Pick up time",
					'Hora de llegada al punto de destino':"Drop off time",
					'Duración total del viaje (minutos)':"Travel time (minutes)",
					'Punto de salida: latitud':"Pick up point: latitude",
					'Punto de salida: longitud':"Pick up point: longitude",
					'Punto de destino: latitud':"end latitude",
					'Punto de destino: longitud':"Destination: longitude",
					'Tiempo de espera pasajero (min)':"Passenger waiting time (mins)",
					'Motivo del viaje':"Journey purpose",
					'Centro de coste variable':"Variable charge code"

					})

			

			print(i)
			columnas_total = ["sale code"
                            ,"Client's name"
                            ,"Client's tax code"
                            ,"Client's role"
                            ,"Requested by"
                            ,"Employee user code"
                            ,"Currency"
                            ,"Price"
                            ,"Discount"
                            ,"Total after discount"
                            ,"Base price"
                            ,"Price for Waiting Time"
                            ,"Billed supplement"
                            ,"Start time"
                            ,"Rider's name"
                            ,"rider employee code"
                            ,"Rider's email"
                            ,"Pick up point"
                            ,"Stops"
                            ,"Destination"
                            ,"Region name"
                            ,"Type of request"
                            ,"Final state"
                            ,"User department"
                            ,"Charge code used by passenger"
                            ,"Charge Code"
                            ,"Message for driver"
                            ,"Driver"
                            ,"Type of vehicle"
                            ,"Vehicle model"
                            ,"Driver waiting time (mins)"
                            ,"Distance (km)"
                            ,"Hired at"
                            ,"Arrived at the pick up point"
                            ,"Pick up time"
                            ,"Drop off time"
                            ,"Travel time (minutes)"
                            ,"Pick up point: latitude"
                            ,"Pick up point: longitude"
                            ,"end latitude"
                            ,"Destination: longitude"
                            ,"Passenger waiting time (mins)"
                            ,"Journey purpose"
                            ,"Variable charge code"

                            ]

                #dataExcel.to_csv('C:\\Users\\martineztorres.55\\Desktop\\HashtagsService\\summary-COLE21Y02147 Nearshore Bogota Taxi Jul-21.csv')
            #pd.read_excel(excel)
            #df = pd.read_excel(i)
			df.insert(1,'Upload Date',datetime.now().strftime('%Y-%m-%d'))
			print(df.columns.values)
			for item in columnas_total:
				if item in df.columns:
					print("dataframe already contains: "+item)
				else:
					print("adding empty col: "+item)
					df[item] = '-'
			# try:
			# 	df['rider employee code']=str(df['rider employee code'].astype(int))		

			# except:
			# 	continue
            #-------------------------Vaucher-------------
			df = df.astype('str')
			for columna in range(len(df['rider employee code'])):
				print("ok")
				df['rider employee code'][columna]=df['rider employee code'][columna].strip(".0")
			
			frames[m]=df
			m=m+1
			df.to_excel('fsdfsdf.xlsx')

			#print(type(df['rider employee code'][0]),df['rider employee code'][0])

			

            
            #df.to_excel('fsdfsdf.xlsx')
            #df.to_csv("summary-COLE21Y02147 Nearshore Bogota Taxi Jul-21.csv")
            

			#j='C:\\Users\\martineztorres.55\\Desktop\\mios\\lll\\'+str(os.path.splitext(i)[:-1])+'.zip'
			#zf = zipfile.ZipFile(j, mode="w")
			#zf.write(i, compress_type=zipfile.ZIP_DEFLATED)
			#zf.close()
			#remove(i)

			
	
    ## reemplazar nan por -- 
	result=pd.concat(frames)
	result = result.astype('str')
	#for columna in range(len(df['rider employee code'])):
		#result['rider employee code'][columna]=result['rider employee code'][columna].strip(".0")
		#result['Variable charge code'][columna]=result['Variable charge code'][columna].strip(".0")
		#result["Charge code used by passenger"][columna]=result["Charge code used by passenger"][columna].strip(".0")
	#for i in result.columns:
		#result[i]=result[i].replace('nan','--',regex=True)
	# for i in range(len(result)):
	# 	while j <=6:
	# 		if result['rider employee code'][i][j][-1:-2]=
	# 		j=j+1
	#print(result['rider employee code'][2000])#[-2:])	
	
	result.to_excel('fsdfsdf.xlsx')
			
			
			# frames[m] = pd.read_excel(i)
			

#result=pd.concat(frames)
#print(len(result))

#file.endswith('.pdf'):
#concat