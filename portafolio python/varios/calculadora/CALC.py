from tkinter import*
import math

root=Tk()
root.title("Calculadora")
root.resizable(width=False, height=False)

display=Entry(root,font=("Calibri 25"))
#display.pack()
display.grid(row=1,columnspan=9,sticky=W+E)

#-----------------------
i=0
resultado=0
def numero(n):
	global i
	display.insert(i,n)
	i+=1

def borrar():
	display.delete(0,END)
	i=0
def Operacion():
	#global i
	ecuacion=display.get()
	global resultado
	resultado=eval(ecuacion)
	display.delete(0,END)
	display.insert(0,resultado)
	
def funcion(op):
	global i
	Operacion()
	if op =="^2":
		resultado1=resultado**2
		display.insert(0,resultado1)
		display.delete(0,END)
		i=i**2
	if op =="^1/2":
		resultado1='%.3f'%(math.sqrt(resultado))
		display.insert(0,resultado1)
		display.delete(0,END)
		i=4
	if op =="log":
		resultado1='%.3f'%(math.log(resultado))
		display.insert(0,resultado1)
		display.delete(0,END)
		i=4


	if op=="MoreOrLess":
		resultado1=(resultado*(-1))
		display.insert(0,resultado1)
		display.delete(0,END)
		i=i+1
		numero(resultado1)

def trigonometrico(op):
	global i
	Operacion()
	if op =="sin":
		resultado1='%.3f'%(math.sin(math.radians(resultado)))
		display.insert(0,resultado1)
		display.delete(0,END)
		i=4
		
	
	elif op =="cos":

		resultado1='%.3f'%(math.cos(math.radians(resultado)))
		display.insert(0,resultado1)
		display.delete(0,END)
		i=4
	elif op =="tan":
		resultado1='%.3f'%(math.tan(math.radians(resultado)))
		display.insert(0,resultado1)
		display.delete(0,END)
		i=4

	elif op=="asin":
		resultado1='%.3f'%(math.asin(resultado))
		display.insert(0,resultado1)
		display.delete(0,END)
		i=4
	elif op=="acos":
		resultado1='%.3f'%(math.acos(resultado))
		display.insert(0,resultado1)
		display.delete(0,END)
		i=4
	elif op=="atan":
		resultado1='%.3f'%(math.atan(resultado))
		display.insert(0,resultado1)
		display.delete(0,END)
		i=4
	numero(resultado1)





Button(root,text="1",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero(1)).grid(row=2,column=0,sticky=W+E)
Button(root,text="2",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero(2)).grid(row=2,column=1,sticky=W+E)
Button(root,text="3",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero(3)).grid(row=2,column=2,sticky=W+E)
Button(root,text="4",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero(4)).grid(row=3,column=0,sticky=W+E)
Button(root,text="5",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero(5)).grid(row=3,column=1,sticky=W+E)
Button(root,text="6",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero(6)).grid(row=3,column=2,sticky=W+E)
Button(root,text="7",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero(7)).grid(row=4,column=0,sticky=W+E)
Button(root,text="8",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero(8)).grid(row=4,column=1,sticky=W+E)
Button(root,text="9",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero(9)).grid(row=4,column=2,sticky=W+E)

#---------------------------------------------

Button(root,text="0",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=3, height=2,bg="powder blue",command=lambda:numero(0)).grid(row=5,column=0,sticky=W+E)
Button(root,text="AC",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="blue",command=lambda:borrar()).grid(row=2,column=6,sticky=W+E)
Button(root,text=".",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero(".")).grid(row=5,column=4,sticky=W+E)

Button(root,text="+",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero("+")).grid(row=2,column=3,sticky=W+E)
Button(root,text="-",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero("-")).grid(row=3,column=3,sticky=W+E)
Button(root,text="÷",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero("/")).grid(row=4,column=3,sticky=W+E)
Button(root,text="*",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero("*")).grid(row=5,column=3,sticky=W+E)

Button(root,text="(",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero("(")).grid(row=2,column=4,sticky=W+E)
Button(root,text=")",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero(")")).grid(row=3,column=4,sticky=W+E)
Button(root,text="=",pady=1, bd=4, fg="blue",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:Operacion()).grid(row=5,column=1,sticky=W+E)
Button(root,text="±",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:funcion("MoreOrLess")).grid(row=4,column=4,sticky=W+E)
Button(root,text="π",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=2, height=2,bg="powder blue",command=lambda:numero(math.pi)).grid(row=5,column=2,sticky=W+E)

Button(root,text="√",fg="black", bd=4,font=('arial',20,'bold'),width=3, height=2,bg="blue",command=lambda:funcion("^1/2")).grid(row=6,column=0,sticky=W+E)
Button(root,text="^2",fg="black", bd=4,font=('arial',20,'bold'),width=3, height=2,bg="blue",command=lambda:funcion("^2")).grid(row=6,column=1,sticky=W+E)
Button(root,text="sin",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=3, height=2,bg="blue",command=lambda:trigonometrico("sin")).grid(row=6,column=2,sticky=W+E)
Button(root,text="cos",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=3, height=2,bg="blue",command=lambda:trigonometrico("cos")).grid(row=6,column=3,sticky=W+E)
Button(root,text="tan",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=3, height=2,bg="blue",command=lambda:trigonometrico("tan")).grid(row=6,column=4,sticky=W+E)
Button(root,text="atan",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=3, height=2,bg="blue",command=lambda:trigonometrico("atan")).grid(row=6,column=6,sticky=W+E)
Button(root,text="asin",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=3, height=2,bg="blue",command=lambda:trigonometrico("asin")).grid(row=4,column=6,sticky=W+E)
Button(root,text="acos",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=3, height=2,bg="blue",command=lambda:trigonometrico("acos")).grid(row=5,column=6,sticky=W+E)
Button(root,text="log",pady=1, bd=4, fg="black",font=('arial',20,'bold'),width=3, height=2,bg="blue",command=lambda:funcion("log")).grid(row=3,column=6,sticky=W+E)
root.mainloop()