#!/usr/bin/env python

"""
Modulo principal para definir atributos y ejecutar los diferentes metodos
"""

from AlgoritmoReducir import *

class App(GUI):

	def __init__(self,window):
		self.Window=window
		self.NFilas=StringVar() #Variable para en N° de filas
		self.NColumnas=StringVar() #Variable para en N° de columnas
		self.VarMatriz=IntVar() #Variable para elegir la resolucion de matriz o sistema de ecuaciones

		#Definir variables para cada cuadro (elemento) de la matriz
		self.A11,self.A12,self.A13,self.A14,self.A15,self.A16,self.A17=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
		self.A21,self.A22,self.A23,self.A24,self.A25,self.A26,self.A27=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
		self.A31,self.A32,self.A33,self.A34,self.A35,self.A36,self.A37=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
		self.A41,self.A42,self.A43,self.A44,self.A45,self.A46,self.A47=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
		self.A51,self.A52,self.A53,self.A54,self.A55,self.A56,self.A57=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
		self.Interfaz() #Crear la interfaz

	def Reducir(self,Valor):

		try: 
			#Convertir cada elemento de tipo string a tipo racional (fraccion)
			a11,a12,a13,a14,a15,a16,a17=sy.Rational(self.A11.get()),sy.Rational(self.A12.get()),sy.Rational(self.A13.get()),sy.Rational(self.A14.get()),sy.Rational(self.A15.get()),sy.Rational(self.A16.get()),sy.Rational(self.A17.get())
			a21,a22,a23,a24,a25,a26,a27=sy.Rational(self.A21.get()),sy.Rational(self.A22.get()),sy.Rational(self.A23.get()),sy.Rational(self.A24.get()),sy.Rational(self.A25.get()),sy.Rational(self.A26.get()),sy.Rational(self.A27.get())
			a31,a32,a33,a34,a35,a36,a37=sy.Rational(self.A31.get()),sy.Rational(self.A32.get()),sy.Rational(self.A33.get()),sy.Rational(self.A34.get()),sy.Rational(self.A35.get()),sy.Rational(self.A36.get()),sy.Rational(self.A37.get())
			a41,a42,a43,a44,a45,a46,a47=sy.Rational(self.A41.get()),sy.Rational(self.A42.get()),sy.Rational(self.A43.get()),sy.Rational(self.A44.get()),sy.Rational(self.A45.get()),sy.Rational(self.A46.get()),sy.Rational(self.A47.get())
			a51,a52,a53,a54,a55,a56,a57=sy.Rational(self.A51.get()),sy.Rational(self.A52.get()),sy.Rational(self.A53.get()),sy.Rational(self.A54.get()),sy.Rational(self.A55.get()),sy.Rational(self.A56.get()),sy.Rational(self.A57.get())

			#Armar el orden de la matris de nxm segun establezca el usuario
			if self.NFilas.get()=='2' and self.NColumnas.get()=='2':
				matriz = np.array([[a11,a12],[a21,a22]])
				if Valor=='G': #Sistema de ecuaciones
					matriz=np.insert(matriz, matriz.shape[1], np.array((a14,a24)), 1) #Insertar columna de terminos Independientes

			elif self.NFilas.get()=='2' and self.NColumnas.get()=='3':
				matriz = np.array([[a11,a12,a13],[a21,a22,a23]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a15,a25)), 1)

			elif self.NFilas.get()=='2' and self.NColumnas.get()=='4':
				matriz = np.array([[a11,a12,a13,a14],[a21,a22,a23,a24]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a16,a26)), 1)

			elif self.NFilas.get()=='2' and self.NColumnas.get()=='5':
				matriz = np.array([[a11,a12,a13,a14,a15],[a21,a22,a23,a24,a25]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a17,a27)), 1)

			elif self.NFilas.get()=='3' and self.NColumnas.get()=='2':
				matriz = np.array([[a11,a12],[a21,a22],[a31,a32]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a14,a24,a34)), 1)

			elif self.NFilas.get()=='3' and self.NColumnas.get()=='3':
				matriz = np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a15,a25,a35)), 1)

			elif self.NFilas.get()=='3' and self.NColumnas.get()=='4':
				matriz = np.array([[a11,a12,a13,a14],[a21,a22,a23,a24],[a31,a32,a33,a34]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a16,a26,a36)), 1)

			elif self.NFilas.get()=='3' and self.NColumnas.get()=='5':
				matriz = np.array([[a11,a12,a13,a14,a15],[a21,a22,a23,a24,a25],[a31,a32,a33,a34,a35]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a17,a27,a37)), 1)

			elif self.NFilas.get()=='4' and self.NColumnas.get()=='2':
				matriz = np.array([[a11,a12],[a21,a22],[a31,a32],[a41,a42]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a14,a24,a34,a44)), 1)

			elif self.NFilas.get()=='4' and self.NColumnas.get()=='3':
				matriz = np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33],[a41,a42,a43]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a15,a25,a35,a45)), 1)

			elif self.NFilas.get()=='4' and self.NColumnas.get()=='4':
				matriz = np.array([[a11,a12,a13,a14],[a21,a22,a23,a24],[a31,a32,a33,a34],[a41,a42,a43,a44]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a16,a26,a36,a46)), 1)

			elif self.NFilas.get()=='4' and self.NColumnas.get()=='5':
				matriz = np.array([[a11,a12,a13,a14,a15],[a21,a22,a23,a24,a25],[a31,a32,a33,a34,a35],[a41,a42,a43,a44,a45]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a17,a27,a37,a47)), 1)

			elif self.NFilas.get()=='5' and self.NColumnas.get()=='2':
				matriz = np.array([[a11,a12],[a21,a22],[a31,a32],[a41,a42],[a51,a52]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a14,a24,a34,a44,a54)), 1)

			elif self.NFilas.get()=='5' and self.NColumnas.get()=='3':
				matriz = np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33],[a41,a42,a43],[a51,a52,a53]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a15,a25,a35,a45,a55)), 1)

			elif self.NFilas.get()=='5' and self.NColumnas.get()=='4':
				matriz = np.array([[a11,a12,a13,a14],[a21,a22,a23,a24],[a31,a32,a33,a34],[a41,a42,a43,a44],[a51,a52,a53,a54]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a16,a26,a36,a46,a56)), 1)

			elif self.NFilas.get()=='5' and self.NColumnas.get()=='5':
				matriz = np.array([[a11,a12,a13,a14,a15],[a21,a22,a23,a24,a25],[a31,a32,a33,a34,a35],[a41,a42,a43,a44,a45],[a51,a52,a53,a54,a55]])
				if Valor=='G':
					matriz=np.insert(matriz, matriz.shape[1], np.array((a17,a27,a37,a47,a57)), 1)

			#Ejecutar la reduccion dandole por parametro la matriz y el tipo de ejecucion que se desea realizar el usuario
			Reduccion(matriz,Valor)

		except TypeError: #El usuario no digito valores numericos o dejo los cuadros en blanco
			messagebox.showwarning('Mensaje','Asegurese de digitar solo datos numericos')

		except ZeroDivisionError: #El usuario escribio una fraccion con denominador 0
			messagebox.showwarning('Mensaje','Error, division entre 0')
			
if __name__=='__main__':
	window=Tk() #Crear la ventana
	App(window)
	window.mainloop() 
	
