import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot as plt
import sqlite3
import random
import seaborn as nsn



class AVION:
	global hola,agregar,marca_avion,destino,vuelo,c,conn,Bandera
	marca_avion=""
	destino=""
	vuelo=""
	print("Por favor ingrese los datos requeridos")
	agregar="si"

	conn=sqlite3.connect('tutorial.db')
	c=conn.cursor()
	Bandera=False

	def __init__(self,marca_avion,destino,vuelo):
		self.marca_avion=marca_avion
		self.destino=destino
		self.vuelo=vuelo
		

	def crea_tabla(self,c):
		c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(Destino TEXT, Avion TEXT, Pasaje REAL)')
		Bandera=True
	
	def entrada(self):
		if bandera==false:
			self.crea_tabla
		else:
			c.execute("INSERT INTO stuffToPlot VALUES (Destino,Avion,Pasaje)")
			conn.commit()
			c.close()
			conn.close()

	def datos_dinamicos(self,c,conn):
		print("Agregar datos")
		self.Destino=input("Destino: ")
		self.marca_avion=input("avion: ")
		self.vuelo=input("pasaje: ")
		c.execute("INSERT INTO stuffToPlot (Destino,Avion,Pasaje) VALUES(?,?,?)",(self.Destino,self.marca_avion,self.vuelo))
		conn.commit()


	def Introducir(self,agregar,c,conn):
 		while agregar=="si":
 			self.datos_dinamicos(c,conn)
 			agregar=input("desea agregar a la lista?")
 		c.close()
 		conn.close()


	def leer_Avion(self):
		conn=sqlite3.connect('tutorial.db')
		c=conn.cursor()
		c.execute('SELECT * FROM stuffToPlot  WHERE Avion="Boeing"')
		data=c.fetchall()
		print(data)
		for row in data:
			print(row)
		c.close()
		conn.close()


	def leer_destino(self):
		conn=sqlite3.connect('tutorial.db')
		c=conn.cursor()
		seleccione=input("seleccione pais destino: ")
		c.execute("SELECT * FROM stuffToPlot  WHERE Destino ='{}'".format(seleccione))
		data=c.fetchall()
		print(data)
		for row in data:
			print(row)
		c.close()
		conn.close()
	
	def update(self):
		conn=sqlite3.connect('tutorial.db')
		c=conn.cursor()
		c.execute('SELECT * FROM stuffToPlot')
		data=c.fetchall()
		print(data)
		item=input("item a cambiar: ")
		antes=input("valor inicial: ")
		despues=input("valor final: ")
		x=False
		while x==False:
			try:
				c.execute("UPDATE stuffToPlot SET {}='{}' WHERE {}='{}'".format(item,despues,item,antes))
				conn.commit()
				c.execute('SELECT * FROM stuffToPlot')
				data=c.fetchall()
				print(data)
				x=True
			except:
				print("Vuelva a intentarlo con los valores correctos")

	def Actualizar(self,agregar,c,conn):
		agregar=input("desea actualizar otro elemento de la lista?")
		while agregar=="si":
			self.update()
			agregar=input("desea actualizar otro elemento de la lista?")
		c.close()
		conn.close()


	def Delete(self):
		conn=sqlite3.connect('tutorial.db')
		c=conn.cursor()
		c.execute('SELECT * FROM stuffToPlot')
		data=c.fetchall()
		print(data)
		x=False
		while x==False:
			item=input("item a eliminar: ")
			antes=input("valor del elemento a eliminar")
			item2=input("item a eliminar: ")
			antes2=input("valor del elemento a eliminar")
			try:
				c.execute("DELETE FROM stuffToPlot WHERE {}='{}' AND {}='{}'".format(item,antes,item2,antes2))
				conn.commit()
				c.execute('SELECT * FROM stuffToPlot')
				data=c.fetchall()
				print(data)
				x=True
			except:
				print("Vuelva a intentarlo con los valores correctos")



	def ExtraerData(self):
		conn=sqlite3.connect('tutorial.db')
		c.execute('SELECT * FROM stuffToPlot WHERE Destino == "Colombia"')
		for row in c.fetchall():
			print (row)
		conn.close()

 	
		
	def Eliminar(self,agregar,c,conn):
		agregar=input("desea eliminar a item de la lista?")
		while agregar=="si":
 			self.Delete()
 			agregar=input("desea eliminar algun item de la lista?")
 			c.close()
 			conn.close()
	
	def Graficar(self):
		c.execute('SELECT * FROM stuffToPlot')
		df=c.fetchall()
		print(len(df))
		d={}
		valor=[]
		valor2=[]
		for row in range(len(df)):
 			valor.append(df[row][0])
 			if df[row][0] not in valor2:
 				valor2.append(df[row][0])
 		for fila in valor2:
 			x=valor.count(fila)
 			print(x)
 			d[fila]=x
 		print(d)
 		plt.bar(d.keys(), d.values(), color='g')
 		plt.show()
 		


 		





 		

	
Avionn=AVION(marca_avion,destino,vuelo)
#Avionn.crea_tabla(c)
#Avionn.Introducir(agregar,c,conn)
#Avionn.leer_Avion()
#Avionn.leer_destino()
#Avionn.Eliminar(agregar,c,conn)
#Avionn.Actualizar(agregar,c,conn)
Avionn.ExtraerData()
Avionn.Graficar()
