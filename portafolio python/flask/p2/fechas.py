import json
from datetime import datetime, timedelta



with open('fecha.json') as file:

  	data = json.load(file)
    #Rescatar los keys del diccionario generado
  	dates=data['date']
    #cambia el formato
  	fechaIni =datetime.strptime(dates,"%Y/%m/%d")
  	#Suma 21 dias
  	fechaFin = fechaIni + timedelta(days=21)
  	#Guarda el valore del año y mes de la nueva fecha respectivamente 
  	anio=int(datetime.strftime(fechaFin, "%Y"))
  	mes=int(datetime.strftime(fechaFin, "%m"))
    #Calcula el ultimo dia del mes  teniendo en cuenta si es bisiesto (febrero)
  	if  int(mes)==1 or 3 or 5 or 7 or 8  or 10 or 12:
  		Ultimo_Dia=datetime(int(anio),int(mes),30)
  		print(type(Ultimo_Dia),Ultimo_Dia)
  	elif int(mes)==4 or 6 or 9 or 11:
  		Ultimo_Dia=datetime(int(anio),int(mes),30)
  		print(type(Ultimo_Dia),Ultimo_Dia)
  	else:
  		if int(anio)%4==0:
  			Ultimo_Dia=datetime(int(anio),int(mes),29)
  			print(type(Ultimo_Dia),Ultimo_Dia)
  		else: 
  			Ultimo_Dia=datetime(int(anio),int(mes),28)
  			print(type(Ultimo_Dia),Ultimo_Dia)


	#specific_date = datetime(dates[1],dates[2],dates[0])
	#new_date1 = specific_date + timedelta(21)


#date_entry = input('Enter a date (i.e. 2017-7-1)')
	#year, month, day = map(int, date_entry.split('-'))
	#dates = datetime(year, month, day)

  	
 # 	specific_date = datetime(date)
	# new_date = specific_date + timedelta(21)
 # 	print(new_date)
# #class Dias:
   # def __init__(self,day,month,year):
    	#self.day=day
    	#self.month=month
    	#self.year=year
    #def add90Days(self):
		#given_date=datetime.date(self.year,self.month,self.day)
		#new_date = given_date + datetime.timedelta(days=21)
		#return new_date

#dd=dias(year,month,day)

#class Dias:
 #   def __init__(self,day,month,year):
    	
    	#self.day=day+21
    	#self.month=month
    	#self.year=year
    	
    #def dos():
    #if self.year%4!=0:
   		#if (self.month==2 and self.day+21>=28):
   		#	self.month=self.month+1
   		#	self.day=abs(self.day-29)
   		#else
   		#		pass
   		#else:
   		#	if (self.month==2 and self.day+21>=29): 
   		#		self.month=self.month+1
   		#		self.day=abs(self.day-30)
   		#	return(self.day,self.month,self.year)
   	


#pares1=Dias(3,2,2018)
#print(pares1.dos())
 
#def cambio():
    # if month==1,3,5,7,8,10,12 :
    # 	print(end_date,"u[0],31,")
    # if this.month==4,6,9,11 and this.day>=31:
    # 	this.month=month+1
    # 	print("this.month tiene 31 dias")
    # 	print("wwww")
    # if this.month==2:
    # 	print("sss")
    	



    	



  # #	specific_date = datetime(str(dates[1]),str(dates[2]),str(dates[0])
  # 	#new_date1 = specific_date + timedelta(21)

  # 	#print(new_date)
  # 	date_1 = datetime.datetime.strptime(dates,"%m/%d/%y")
  # 	end_date = date_1 + datetime.timedelta(days=10)
  # 	print(end_date)
