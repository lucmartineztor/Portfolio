import re
print("PRIMER PUNTO")
cadena=input("introduzca cadena deseada: ")
busqueda=re.search(r"\*",cadena)
#Busca el simbolo * en la cadena
cadena=cadena.replace("*"," ")
#Genera nueva cadena reemplazando * por espacio
cadena1=cadena.split(" ")
#Permite interpretar el espacio como separador 
l=1
#Variable bandera
if busqueda:
	busqueda=re.search(r"\&",cadena)
	cadena=cadena.replace("&","B")
	busqueda=re.search(r"\-",cadena)
	cadena=cadena.replace("-","k")
	busqueda=re.search(r"\_",cadena)
	cadena=cadena.replace("_","m")
	#Cambio de variables para facilitar el reconocimiento de 
	#caracteres en la siguiente parte del codigo
	u=re.findall('([A-Za-z]+)',cadena)
	#genera y almacena grupos
	#Sentencias if anidadas para revisar si la cadena cumple las condiciones especificadas 
	if cadena:
		if  len(u)>1:
			for i in u: 
				if i[0]=="B" or i[0]==i[0].upper():
					if len(u)>=2:
							for i in u:
								if len(i)>2:
								
									for j in range(1,len(i),1):
										if (i[j]==i[j].lower() or i[j]=="k" or i[j]=="m"):
											pass

										else: 
											print("Solo minusculas, _ o - despues del primer caracter")
											l=0
											exit()
				
								else: 
									print ("grupos muy cortos")
									l=0
									exit()
				else: 
					print("Colocar en mayuscula o & despues de cada asterisco")
					l=0
					exit()

		else: 
			print("cadena muy corta")
			l=0
			exit()
				
else:
	print("Por favor separar con *")
	l=0
	exit()
	
if l==1:
	print("Todo perfecto")
					
				
	

	



	