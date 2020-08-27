class AVION:
	global hola,arreglo,agregar,marca_avion,destino,vuelo
	marca_avion=""
	destino=""
	vuelo=""
	arreglo=[]
	print("Por favor ingrese los datos requeridos")
	agregar="si"
	
	def __init__(self,marca_avion,destino,vuelo,arreglo):
		self.marca_avion=marca_avion
		self.destino=destino
		self.vuelo=vuelo
		self.arreglo=arreglo
		 

	def	avion(self):
		self.inicio()
		#En diccionario se almacena la informacion de cada vuelo
		diccionario={"avion":self.marca_avion, "destino":self.destino,"vuelo":self.vuelo}
		#En arreglo se almacena en forma de array los diccionarios
		self.arreglo.append(diccionario)
		return self.arreglo
		


	
	def eliminar(self):
		print(self.arreglo)
		itemm=input("escoger item: ")
		dato=input("dato a eliminar: ")
		item=input("escoger segundo item: ")
		datom=input("dato 2 a elimiar: ")
		x=False
		while x==False:	
			try:
				for i in range(len(self.arreglo)):
					if self.arreglo[i][item]==dato:
						if self.arreglo[i][itemm]==datom:
							self.arreglo.pop(i)
							x=True
			except:
				print("vuelva a introducir los datos correctamente")

	def final2(self,agregar):
		while agregar=="si":
			self.eliminar()
			agregar=input("desea agregar a la lista?")
		print (self.arreglo)

	def modificar(self):
		print(self.arreglo)
		item=input("escoger item: ")
		antes=input("dato a modifica: ")
		despues=input("dato actual: ")
		x=False
		while x==False:	
			try:
				for i in range(len(self.arreglo)):
					if self.arreglo[i][item]==antes:
						self.arreglo[i][item]=despues
			except:
				print("vuelva a introducir los datos correctamente")
	
	def final1(self,agregar):
		while agregar=="si":
			self.modificar()
			agregar=input("desea agregar a la lista?")
		return self.arreglo				
						
			

#metodo que especifica si es tipo Boeing o no
	def Boeing(self):
		#se recorre el array que contiene los diccionarios con la informacion de cada vuelo
		for i in range(len(self.arreglo)):
			if self.arreglo[i]["avion"]=="Boeing":
				#devuelve los aviones tipo Boeing
				print( "el tipo del avion es: "+self.arreglo[i]["avion"]) 
				
			elif self.arreglo[i]["avion"]!="Boeing":
				print("el vuelo "+self.arreglo[i]["vuelo"] + " NO es tipo Boeing")

		
#metodo que especifica si el dstino de dos vuelos es el  mismo. 
	def Destino(self):
		self.final(agregar)
		#variable bandera
		u=0
		#Para hacer la comparacion entre todos los elementos se hace doble recorrido i j
		for i in range(len(self.arreglo)):
			for j in range(len(self.arreglo)):
				if j>i:
					if self.arreglo[i]["destino"]==self.arreglo[j]["destino"]:
						u=1
						#devuelve vuelos con mismos destinos
						print("los vuelos"+self.arreglo[i]["vuelo"]+" y " +self.arreglo[j]["vuelo"]+"tienen el mismo destino")
			if u==0:
 				print("ningun vuelo tiene el mismo destino")


	def inicio(self):
		hola="por favor ingrese los datos solicitados"
		self.marca_avion=input("elija entre Boeing, Airbus o Antonov:  ")
		self.destino=input("destino: ")
		self.vuelo=input("codigo de vuelo: ")
		return self.marca_avion,self.destino,self.vuelo

	def final(self,agregar):
		while agregar=="si":
			self.avion()
			agregar=input("desea agregar a la lista?")
		return self.arreglo

avioncito=AVION(marca_avion,destino,vuelo,arreglo)
avioncito.Destino()
avioncito.Boeing()
avioncito.final2(agregar)
print(avioncito.final1(agregar))

