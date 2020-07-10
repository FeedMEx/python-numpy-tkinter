
"""
Este modulo contiene el codigo para la construccion de la GUI
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import sympy as sy

class GUI():

	def __init__(self):
		pass

	def Interfaz(self):
		#Crear la interfaz grafica de usuario
		self.Window.title("App Matrices")
		self.Window.geometry("400x325+100+100")
		self.Window.resizable(0,0)
		self.Window.config(bg='#d4dce3')

		BarraMenu=Menu(self.Window) #Menu para que el usuario establesca ejecucion de matrices o sistema de ecuaciones
		self.Window.config(menu=BarraMenu)

		self.Archivo=Menu(BarraMenu,tearoff=0)
		self.Archivo.add_radiobutton(label="Matriz                ",variable=self.VarMatriz,value=1,command=self.InterfazMatriz)
		self.Archivo.add_radiobutton(label="Sistema de ecuaciones ",variable=self.VarMatriz,value=2,command=self.InterfazMatriz)		

		Ayuda=Menu(BarraMenu,tearoff=0)
		Ayuda.add_command(label="Ver la ayuda     ",command=self.TopAyuda)
		BarraMenu.add_cascade(label='Archivo', menu=self.Archivo)
		BarraMenu.add_cascade(label='Ayuda', menu=Ayuda)
		
		self.Texto1=Label(self.Window,bg='#d4dce3',font=(10))
		self.Texto2=Label(self.Window,bg='#d4dce3',font=(10))
		ttk.Combobox(self.Window,values=['2','3','4','5'],textvariable=self.NFilas,width=1,state='readonly',font=(10)).place(x=115,y=15)
		ttk.Combobox(self.Window,values=['2','3','4','5'],textvariable=self.NColumnas,width=1,state='readonly',font=(10)).place(x=270,y=15)
		self.NFilas.set("2")
		self.NColumnas.set("2")

		Button(self.Window,text="Generar Cuadro",font=(10),bg='#5c8cc5',fg='white',bd=0,width=39,command=self.MoS).place(x=20,y=50)
		self.FrameMatriz=Frame(self.Window,bg='#d4dce3')
		self.FrameVariables=Frame(self.Window,bg='#d4dce3')
		ttk.Entry(self.FrameMatriz,textvariable=self.A11,width=5,justify='right',font=(10)).grid(row=1,column=1)
		ttk.Entry(self.FrameMatriz,textvariable=self.A12,width=5,justify='right',font=(10)).grid(row=1,column=2)
		ttk.Entry(self.FrameMatriz,textvariable=self.A21,width=5,justify='right',font=(10)).grid(row=2,column=1)
		ttk.Entry(self.FrameMatriz,textvariable=self.A22,width=5,justify='right',font=(10)).grid(row=2,column=2)
		self.MTS=ttk.Button(self.Window,text="Matriz Escalonada",width=58,command=lambda: self.Reducir('T'))
		self.MER=ttk.Button(self.Window,text="Matriz Escalonada Reducida",width=58,command=lambda: self.Reducir('R'))
		self.SGJ=ttk.Button(self.Window,text="Solucion por el Metodo de Gauss-Jordan",width=58,command=lambda: self.Reducir('G'))

		self.Archivo.invoke(index=0) #Iniciar con la interfaz grafica de matrices

		Label(self.Window,text='By: Freddy',bg='#d4dce3').place(x=317,y=300)
	
	def TopAyuda(self):
		Top=Toplevel()
		texto="\n\tCualquier consulta sobre el proyecto:\t\t\n\ngmail: 160892@unsaac.edu.pe\n"
		Label(Top,text=texto).pack()

	def InterfazMatriz(self):

		self.NFilas.set('2') #Iniciar la interfaz grafica con dos filas y columnas
		self.NColumnas.set('2')

		if self.VarMatriz.get()==1:
			self.FrameMatriz.place(x=20,y=90)
			self.Texto1.config(text='Filas:')
			self.Texto1.place(x=70,y=15)
			self.Texto2.config(text='Columnas:')
			self.Texto2.place(x=190,y=15)
			self.FrameVariables.place(x=1000,y=90)
			self.MTS.place(x=20,y=230)
			self.MER.place(x=20,y=254)
			self.SGJ.place(x=1000,y=254)

			self.MxN()
			self.L16(),self.L26(),self.L36(),self.L46(),self.L56()
			self.L17(),self.L27(),self.L37(),self.L47(),self.L57()

		else:
			self.MTS.place(x=1000,y=230)
			self.MER.place(x=1000,y=254)
			self.SGJ.place(x=20,y=254)
			
			#Frame(self.Window,bg='#d4dce3',width=360,height=49).place(x=20,y=230)
			self.FrameVariables.place(x=20,y=90)
			self.FrameMatriz.place(x=20,y=115)
			self.NFilas.set('2')
			self.NColumnas.set('2')
			self.Texto1.config(text='Ecuaciones:')
			self.Texto1.place(x=20,y=15)
			self.Texto2.config(text='Variables:')
			self.Texto2.place(x=190,y=15)
			self.Sistema()		
		self.IniciarCeros()

	def TopMostrar(self):
		#Dimensiones y propiedades de la Ventana emergente para la vizualizacion de la resolucion de matrices    
		self.Top=Toplevel()
		self.Top.title("Resultados")
		self.Top.geometry('500x400+520+100')
		self.Top.resizable(0,0)
		self.Top.focus_set()

		self.canvas=Canvas(self.Top)#Canvas para desplazarse en las 4 direcciones a travez de la ventana emergente
		self.canvas.pack()

		self.BloqueMostrar=Frame(self.canvas)
		self.BloqueMostrar.bind("<Configure>",self.Scroll)#evento para el uso del scroll a travez de la ventana emergente
		self.BloqueMostrar.pack()

		myscrollbar=Scrollbar(self.Top,orient="vertical",command=self.canvas.yview)#scroll vertical
		self.canvas.configure(yscrollcommand=myscrollbar.set)
		myscrollbar.place(x=480,y=0,heigh=380)

		myscrollbar=Scrollbar(self.Top,orient="horizontal",command=self.canvas.xview)#scroll horizontal
		self.canvas.configure(xscrollcommand=myscrollbar.set)
		myscrollbar.place(x=0,y=380,width=480)

		self.canvas.create_window((0,0),window=self.BloqueMostrar,anchor='nw')

		Label(self.BloqueMostrar,text=' ',width=20).pack()
		Label(self.BloqueMostrar,text='Matriz inicial',font=(10)).pack()
	
	def Sistema(self):
		self.MxN()

		for n in range(0,int(self.NColumnas.get())):
			Label(self.FrameVariables,text='X{}'.format(n+1),font=(10),bg='#d4dce3',width=5).grid(row=0,column=n+1)

		if self.NFilas.get()=='2' and self.NColumnas.get()=='2':
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=3)
			self.C14(),self.C24(),self.L03(),self.L04(),self.L05()
			self.L16(),self.L26(),self.L36(),self.L46(),self.L56()
			self.L17(),self.L27(),self.L37(),self.L47(),self.L57()	

		elif self.NFilas.get()=='2' and self.NColumnas.get()=='3':
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=4)
			self.C15(),self.C25(),self.L04(),self.L05()
			self.L16(),self.L26(),self.L36(),self.L46(),self.L56()
			self.L17(),self.L27(),self.L37(),self.L47(),self.L57()

		elif self.NFilas.get()=='2' and self.NColumnas.get()=='4':
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=5)
			self.C16(),self.C26(),self.L36(),self.L46(),self.L05()
			self.L17(),self.L27(),self.L37(),self.L47(),self.L57()
		
		elif self.NFilas.get()=='2' and self.NColumnas.get()=='5':
			self.L16(),self.L26(),self.L36(),self.L46(),self.L56()
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=6)
			self.C17(),self.C27(),self.L37(),self.L47(),self.L57()

		elif self.NFilas.get()=='3' and self.NColumnas.get()=='2':
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=3)
			self.C14(),self.C24(),self.C34(),self.L03(),self.L04(),self.L05()
			self.L16(),self.L26(),self.L36(),self.L46(),self.L56()
			self.L17(),self.L27(),self.L37(),self.L47(),self.L57()

		elif self.NFilas.get()=='3' and self.NColumnas.get()=='3':
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=4)
			self.C15(),self.C25(),self.C35(),self.L04(),self.L05()
			self.L16(),self.L26(),self.L36(),self.L46(),self.L56()
			self.L17(),self.L27(),self.L37(),self.L47(),self.L57()
		
		elif self.NFilas.get()=='3' and self.NColumnas.get()=='4':
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=5)
			self.C16(),self.C26(),self.C36(),self.L46(),self.L05()
			self.L17(),self.L27(),self.L37(),self.L47(),self.L57()

		elif self.NFilas.get()=='3' and self.NColumnas.get()=='5':
			self.L16(),self.L26(),self.L36(),self.L46(),self.L56()
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=6)
			self.C17(),self.C27(),self.C37(),self.L47(),self.L57()

		elif self.NFilas.get()=='4' and self.NColumnas.get()=='2':
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=3)
			self.C14(),self.C24(),self.C34(),self.C44(),self.L03(),self.L04(),self.L05()
			self.L16(),self.L26(),self.L36(),self.L46(),self.L56()
			self.L17(),self.L27(),self.L37(),self.L47(),self.L57()
			
		elif self.NFilas.get()=='4' and self.NColumnas.get()=='3':
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=4)
			self.C15(),self.C25(),self.C35(),self.C45(),self.L04(),self.L05()
			self.L16(),self.L26(),self.L36(),self.L46(),self.L56()
			self.L17(),self.L27(),self.L37(),self.L47(),self.L57()

		elif self.NFilas.get()=='4' and self.NColumnas.get()=='4':
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=5)
			self.C16(),self.C26(),self.C36(),self.C46(),self.L56(),self.L05()
			self.L17(),self.L27(),self.L37(),self.L47(),self.L57()

		elif self.NFilas.get()=='4' and self.NColumnas.get()=='5':
			self.L16(),self.L26(),self.L36(),self.L46(),self.L56()
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=6)
			self.C17(),self.C27(),self.C37(),self.C47(),self.L57()

		elif self.NFilas.get()=='5' and self.NColumnas.get()=='2':
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=3)
			self.C14(),self.C24(),self.C34(),self.C44(),self.C54(),self.L03(),self.L04(),self.L05()
			self.L16(),self.L26(),self.L36(),self.L46(),self.L56()
			self.L17(),self.L27(),self.L37(),self.L47(),self.L57()

		elif self.NFilas.get()=='5' and self.NColumnas.get()=='3':
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=4)
			self.C15(),self.C25(),self.C35(),self.C45(),self.C55(),self.L04(),self.L05()
			self.L16(),self.L26(),self.L36(),self.L46(),self.L56()
			self.L17(),self.L27(),self.L37(),self.L47(),self.L57()

		elif self.NFilas.get()=='5' and self.NColumnas.get()=='4':
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=5)
			self.C16(),self.C26(),self.C36(),self.C46(),self.C56(),self.L05()
			self.L17(),self.L27(),self.L37(),self.L47(),self.L57()

		elif self.NFilas.get()=='5' and self.NColumnas.get()=='5':
			self.L16(),self.L26(),self.L36(),self.L46(),self.L56()
			for i in range(0,int(self.NFilas.get())):
				Label(self.FrameMatriz,text="=",bg='#d4dce3',font=(10)).grid(row=i+1,column=6)
			self.C17(),self.C27(),self.C37(),self.C47(),self.C57()



	def MoS(self): #Metodo ejecutar el metodo de reduccion matrices o sistema de ecuaciones
		self.IniciarCeros()
		if self.VarMatriz.get()==1:
			self.MxN()
		else:
			self.Sistema()

	def MostrarMatriz(self,matriz,m,n,tipo): #Muestra todos los pasos de la resolucion de matrices en la ventana emergente
		Bloque=Frame(self.BloqueMostrar)
		Bloque.pack()
		Frame(Bloque,bg='black',height=2).grid(row=0,column=1,sticky='we')
		Frame(Bloque,bg='black',height=2,width=10).grid(row=n+1,column=1,sticky='we')
		Frame(Bloque,bg='black',height=2).grid(row=0,column=0,sticky='we')
		Frame(Bloque,bg='black',height=2).grid(row=n+1,column=0,sticky='we')

		for i in range(0,n):
			Frame(Bloque,bg='black',width=2).grid(row=i+1,column=0,sticky='ns')			
			for j in range(0,m):
				if tipo!='G':
					for e in str(matriz[i,j]):
						if e=='e' or e=='.':
							matriz[i,j]=0
				if tipo=='G' and int(j)<m-1:
					for e in str(matriz[i,j]):
						if e=='e' or e=='.':
							matriz[i,j]=0
					Label(Bloque,text=str(matriz[i,j]),font=(18)).grid(row=i+1,column=j+2,padx=10)
				else:
					Label(Bloque,text=str(matriz[i,j]),font=(18)).grid(row=i+1,column=j+3,padx=10)

			if tipo=='G':
				Frame(Bloque,bg='black',width=2).grid(row=i+1,column=m+1,sticky='ns')
			Frame(Bloque,bg='black',width=2).grid(row=i+1,column=m+5,sticky='ns')

		Frame(Bloque,bg='black',height=2,width=10).grid(row=0,column=m+4,sticky='we')
		Frame(Bloque,bg='black',height=2).grid(row=n+1,column=m+4,sticky='we')
		Frame(Bloque,bg='black',height=2).grid(row=0,column=m+5,sticky='we')
		Frame(Bloque,bg='black',height=2).grid(row=n+1,column=m+5,sticky='we')
		Label(self.BloqueMostrar,text=' ',width=20).pack()

	def Scroll(self,event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=450,height=350)
	
	#Creacion de cuadros para la matriz inicial
	def C11(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A11,width=5,justify='right',font=(16)).grid(row=1,column=1)

	def C12(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A12,width=5,justify='right',font=(16)).grid(row=1,column=2)
	
	def C13(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A13,width=5,justify='right',font=(16)).grid(row=1,column=3)

	def C14(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A14,width=5,justify='right',font=(16)).grid(row=1,column=4)

	def C15(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A15,width=5,justify='right',font=(16)).grid(row=1,column=5)

	def C16(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A16,width=5,justify='right',font=(16)).grid(row=1,column=6)

	def C17(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A17,width=5,justify='right',font=(16)).grid(row=1,column=7)

	def C21(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A21,width=5,justify='right',font=(16)).grid(row=2,column=1)
		
	def C22(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A22,width=5,justify='right',font=(16)).grid(row=2,column=2)

	def C23(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A23,width=5,justify='right',font=(16)).grid(row=2,column=3)

	def C24(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A24,width=5,justify='right',font=(16)).grid(row=2,column=4)
	
	def C25(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A25,width=5,justify='right',font=(16)).grid(row=2,column=5)

	def C26(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A26,width=5,justify='right',font=(16)).grid(row=2,column=6)

	def C27(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A27,width=5,justify='right',font=(16)).grid(row=2,column=7)

	def C31(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A31,width=5,justify='right',font=(16)).grid(row=3,column=1)
		
	def C32(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A32,width=5,justify='right',font=(16)).grid(row=3,column=2)

	def C33(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A33,width=5,justify='right',font=(16)).grid(row=3,column=3)

	def C34(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A34,width=5,justify='right',font=(16)).grid(row=3,column=4)
	
	def C35(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A35,width=5,justify='right',font=(16)).grid(row=3,column=5)

	def C36(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A36,width=5,justify='right',font=(16)).grid(row=3,column=6)

	def C37(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A37,width=5,justify='right',font=(16)).grid(row=3,column=7)

	def C41(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A41,width=5,justify='right',font=(16)).grid(row=4,column=1)
		
	def C42(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A42,width=5,justify='right',font=(16)).grid(row=4,column=2)

	def C43(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A43,width=5,justify='right',font=(16)).grid(row=4,column=3)

	def C44(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A44,width=5,justify='right',font=(16)).grid(row=4,column=4)
	
	def C45(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A45,width=5,justify='right',font=(16)).grid(row=4,column=5)

	def C46(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A46,width=5,justify='right',font=(16)).grid(row=4,column=6)

	def C47(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A47,width=5,justify='right',font=(16)).grid(row=4,column=7)

	def C51(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A51,width=5,justify='right',font=(16)).grid(row=5,column=1)
		
	def C52(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A52,width=5,justify='right',font=(16)).grid(row=5,column=2)

	def C53(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A53,width=5,justify='right',font=(16)).grid(row=5,column=3)

	def C54(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A54,width=5,justify='right',font=(16)).grid(row=5,column=4)
	
	def C55(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A55,width=5,justify='right',font=(16)).grid(row=5,column=5)

	def C56(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A56,width=5,justify='right',font=(16)).grid(row=5,column=6)

	def C57(self):
		ttk.Entry(self.FrameMatriz,textvariable=self.A57,width=5,justify='right',font=(16)).grid(row=5,column=7)

	#Esconder cuadros de la matriz inicial
	def L13(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=1,column=3,sticky='wesn')

	def L14(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=1,column=4,sticky='wesn')

	def L15(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=1,column=5,sticky='wesn')

	def L16(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=1,column=6,sticky='wesn')

	def L17(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=1,column=7,sticky='wesn')

	def L23(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=2,column=3,sticky='wesn')

	def L24(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=2,column=4,sticky='wesn')

	def L25(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=2,column=5,sticky='wesn')

	def L26(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=2,column=6,sticky='wesn')

	def L27(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=2,column=7,sticky='wesn')

	def L31(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=3,column=1,sticky='wesn')

	def L32(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=3,column=2,sticky='wesn')

	def L33(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=3,column=3,sticky='wesn')

	def L34(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=3,column=4,sticky='wesn')

	def L35(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=3,column=5,sticky='wesn')

	def L36(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=3,column=6,sticky='wesn')

	def L37(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=3,column=7,sticky='wesn')

	def L41(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=4,column=1,sticky='wesn')

	def L42(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=4,column=2,sticky='wesn')

	def L43(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=4,column=3,sticky='wesn')

	def L44(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=4,column=4,sticky='wesn')

	def L45(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=4,column=5,sticky='wesn')

	def L46(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=4,column=6,sticky='wesn')

	def L47(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=4,column=7,sticky='wesn')

	def L51(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=5,column=1,sticky='wesn')

	def L52(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=5,column=2,sticky='wesn')

	def L53(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=5,column=3,sticky='wesn')

	def L54(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=5,column=4,sticky='wesn')

	def L55(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=5,column=5,sticky='wesn')

	def L56(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=5,column=6,sticky='wesn')

	def L57(self):
		Frame(self.FrameMatriz,bg='#d4dce3').grid(row=5,column=7,sticky='wesn')

	def L03(self):
		Frame(self.FrameVariables,bg='#d4dce3').grid(row=0,column=3,sticky='wesn')

	def L04(self):
		Frame(self.FrameVariables,bg='#d4dce3').grid(row=0,column=4,sticky='wesn')

	def L05(self):
		Frame(self.FrameVariables,bg='#d4dce3').grid(row=0,column=5,sticky='wesn')
		
	def MxN(self): #Llamar a los metodos creadores o desaparecedores de cuadros segun establezca el usuario
		if self.NFilas.get()=='2' and self.NColumnas.get()=='2':
			self.C11(),self.C12(),self.L13(),self.L14(),self.L15()
			self.C21(),self.C22(),self.L23(),self.L24(),self.L25()			
			self.L31(),self.L32(),self.L33(),self.L34(),self.L35()
			self.L41(),self.L42(),self.L43(),self.L44(),self.L45()
			self.L51(),self.L52(),self.L53(),self.L54(),self.L55()

		elif self.NFilas.get()=='2' and self.NColumnas.get()=='3':
			self.C11(),self.C12(),self.C13(),self.L14(),self.L15()
			self.C21(),self.C22(),self.C23(),self.L24(),self.L25()
			self.L31(),self.L32(),self.L33(),self.L34(),self.L35()
			self.L41(),self.L42(),self.L43(),self.L44(),self.L45()
			self.L51(),self.L52(),self.L53(),self.L54(),self.L55()

		elif self.NFilas.get()=='2' and self.NColumnas.get()=='4':
			self.C11(),self.C12(),self.C13(),self.C14(),self.L15()
			self.C21(),self.C22(),self.C23(),self.C24(),self.L25()
			self.L31(),self.L32(),self.L33(),self.L34(),self.L35()
			self.L41(),self.L42(),self.L43(),self.L44(),self.L45()
			self.L51(),self.L52(),self.L53(),self.L54(),self.L55()
		
		elif self.NFilas.get()=='2' and self.NColumnas.get()=='5':
			self.C11(),self.C12(),self.C13(),self.C14(),self.C15()
			self.C21(),self.C22(),self.C23(),self.C24(),self.C25()
			self.L31(),self.L32(),self.L33(),self.L34(),self.L35()
			self.L41(),self.L42(),self.L43(),self.L44(),self.L45()
			self.L51(),self.L52(),self.L53(),self.L54(),self.L55()

		elif self.NFilas.get()=='3' and self.NColumnas.get()=='2':
			self.C11(),self.C12(),self.L13(),self.L14(),self.L15()
			self.C21(),self.C22(),self.L23(),self.L24(),self.L25()
			self.C31(),self.C32(),self.L33(),self.L34(),self.L35()
			self.L41(),self.L42(),self.L43(),self.L44(),self.L45()
			self.L51(),self.L52(),self.L53(),self.L54(),self.L55()

		elif self.NFilas.get()=='3' and self.NColumnas.get()=='3':
			self.C11(),self.C12(),self.C13(),self.L14(),self.L15()
			self.C21(),self.C22(),self.C23(),self.L24(),self.L25()
			self.C31(),self.C32(),self.C33(),self.L34(),self.L35()
			self.L41(),self.L42(),self.L43(),self.L44(),self.L45()
			self.L51(),self.L52(),self.L53(),self.L54(),self.L55()
		
		elif self.NFilas.get()=='3' and self.NColumnas.get()=='4':
			self.C11(),self.C12(),self.C13(),self.C14(),self.L15()
			self.C21(),self.C22(),self.C23(),self.C24(),self.L25()
			self.C31(),self.C32(),self.C33(),self.C34(),self.L35()
			self.L41(),self.L42(),self.L43(),self.L44(),self.L45()
			self.L51(),self.L52(),self.L53(),self.L54(),self.L55()

		elif self.NFilas.get()=='3' and self.NColumnas.get()=='5':
			self.C11(),self.C12(),self.C13(),self.C14(),self.C15()
			self.C21(),self.C22(),self.C23(),self.C24(),self.C25()
			self.C31(),self.C32(),self.C33(),self.C34(),self.C35()
			self.L41(),self.L42(),self.L43(),self.L44(),self.L45()
			self.L51(),self.L52(),self.L53(),self.L54(),self.L55() 

		elif self.NFilas.get()=='4' and self.NColumnas.get()=='2':
			self.C11(),self.C12(),self.L13(),self.L14(),self.L15()
			self.C21(),self.C22(),self.L23(),self.L24(),self.L25()
			self.C31(),self.C32(),self.L33(),self.L34(),self.L35()
			self.C41(),self.C42(),self.L43(),self.L44(),self.L45()
			self.L51(),self.L52(),self.L53(),self.L54(),self.L55() 
			
		elif self.NFilas.get()=='4' and self.NColumnas.get()=='3':
			self.C11(),self.C12(),self.C13(),self.L14(),self.L15()
			self.C21(),self.C22(),self.C23(),self.L24(),self.L25()
			self.C31(),self.C32(),self.C33(),self.L34(),self.L35()
			self.C41(),self.C42(),self.C43(),self.L44(),self.L45()
			self.L51(),self.L52(),self.L53(),self.L54(),self.L55()

		elif self.NFilas.get()=='4' and self.NColumnas.get()=='4':
			self.C11(),self.C12(),self.C13(),self.C14(),self.L15()
			self.C21(),self.C22(),self.C23(),self.C24(),self.L25()
			self.C31(),self.C32(),self.C33(),self.C34(),self.L35()
			self.C41(),self.C42(),self.C43(),self.C44(),self.L45()
			self.L51(),self.L52(),self.L53(),self.L54(),self.L55()

		elif self.NFilas.get()=='4' and self.NColumnas.get()=='5':
			self.C11(),self.C12(),self.C13(),self.C14(),self.C15()
			self.C21(),self.C22(),self.C23(),self.C24(),self.C25()
			self.C31(),self.C32(),self.C33(),self.C34(),self.C35()
			self.C41(),self.C42(),self.C43(),self.C44(),self.C45()
			self.L51(),self.L52(),self.L53(),self.L54(),self.L55()

		elif self.NFilas.get()=='5' and self.NColumnas.get()=='2':
			self.C11(),self.C12(),self.L13(),self.L14(),self.L15()
			self.C21(),self.C22(),self.L23(),self.L24(),self.L25()
			self.C31(),self.C32(),self.L33(),self.L34(),self.L35()
			self.C41(),self.C42(),self.L43(),self.L44(),self.L45()
			self.C51(),self.C52(),self.L53(),self.L54(),self.L55()

		elif self.NFilas.get()=='5' and self.NColumnas.get()=='3':
			self.C11(),self.C12(),self.C13(),self.L14(),self.L15()
			self.C21(),self.C22(),self.C23(),self.L24(),self.L25()
			self.C31(),self.C32(),self.C33(),self.L34(),self.L35()
			self.C41(),self.C42(),self.C43(),self.L44(),self.L45()
			self.C51(),self.C52(),self.C53(),self.L54(),self.L55()

		elif self.NFilas.get()=='5' and self.NColumnas.get()=='4':
			self.C11(),self.C12(),self.C13(),self.C14(),self.L15()
			self.C21(),self.C22(),self.C23(),self.C24(),self.L25()
			self.C31(),self.C32(),self.C33(),self.C34(),self.L35()
			self.C41(),self.C42(),self.C43(),self.C44(),self.L45()
			self.C51(),self.C52(),self.C53(),self.C54(),self.L55()

		elif self.NFilas.get()=='5' and self.NColumnas.get()=='5':
			self.C11(),self.C12(),self.C13(),self.C14(),self.C15()
			self.C21(),self.C22(),self.C23(),self.C24(),self.C25()
			self.C31(),self.C32(),self.C33(),self.C34(),self.C35()
			self.C41(),self.C42(),self.C43(),self.C44(),self.C45()
			self.C51(),self.C52(),self.C53(),self.C54(),self.C55()

	def IniciarCeros(self): #LLenar de ceros todos los cuadroz de la matriz
		self.A11.set('0'),self.A12.set('0'),self.A13.set('0'),self.A14.set('0'),self.A15.set('0'),self.A16.set('0'),self.A17.set('0')
		self.A21.set('0'),self.A22.set('0'),self.A23.set('0'),self.A24.set('0'),self.A25.set('0'),self.A26.set('0'),self.A27.set('0')
		self.A31.set('0'),self.A32.set('0'),self.A33.set('0'),self.A34.set('0'),self.A35.set('0'),self.A36.set('0'),self.A37.set('0')
		self.A41.set('0'),self.A42.set('0'),self.A43.set('0'),self.A44.set('0'),self.A45.set('0'),self.A46.set('0'),self.A47.set('0')
		self.A51.set('0'),self.A52.set('0'),self.A53.set('0'),self.A54.set('0'),self.A55.set('0'),self.A56.set('0'),self.A57.set('0')