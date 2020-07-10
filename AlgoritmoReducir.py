
"""
Este modulo contiene el algoritmo para la reduccion de matrices
"""

from InterfazGrafica import *

class Reduccion(GUI):

    def __init__(self,Matriz,Valor):
        #Ejecutar la creacion de la ventana emergente para mostrar la reduccion de matrices
        self.TopMostrar(),self.reducir(Matriz,Valor)

    def reducir(self,Matriz,Valor):        
        np.asarray(Matriz) #Encapsular el arreglo
        Matriz = Matriz.astype('object') #Los datos conservaran su tipo (fracciones)

        n,m = Matriz.shape #Obtener en N° de filas y columnas respectivamente
        self.MostrarMatriz(Matriz,m,n,Valor)   #Ejecutar la creacion de la matriz inicial
        
        Break=True #variable true, por si se encuantra un pivote cero y romper el bucle
        self.Arreglo=[] #declarar un arreglo por si existe un pivote cero e intercambiar indices
        for v in range(0,m):
            self.Arreglo.append(v) 

        #Reducir a una matris triangular Superior
        for i in range(0,n): #recorrer las columnas
            for j in range(i+1,n): #recorrer las filas desde los pivotes para abajo
                try:
                    if Matriz[i,i]==0: #pivote 0
                        V,Matriz=self.Intercambiar(Matriz,i,Valor) #Ejecutar el metodo que intercambia columnas de la matriz
                        if V=='True': #Existe columnas de intercambio para dar un valor diferente de cero al pivote
                            Label(self.BloqueMostrar,text='Intercambiando fila',font=(10)).pack()
                            self.MostrarMatriz(Matriz,m,n,Valor) #Mostrar el paso realizado
                        else:
                            Break=False 
                            break #romper bucle por que se encontro un pivote cero

                    if Matriz[j,i] != 0.0: #el elemento en ejecucion es diferente a cero
                        Factor = Matriz[j,i]/Matriz[i,i] #Guardar la division entre el elemento en ejecucion y el pivote
                        Label(self.BloqueMostrar,text="Operando: Fila{} + ({})Fila{}".format(j+1,-Factor,i+1),font=(10)).pack()
                        
                        #restar a toda la fila la division guardada multiplicada por la fila del pivote respectivo
                        Matriz[j,i:m]=Matriz[j,i:m] - Factor*Matriz[i,i:m] 
                        self.MostrarMatriz(Matriz,m,n,Valor) #Mostrar el paso realizado
                except IndexError:
                    pass
        
        #Reducir a una matris triangular inferior
        if (Valor=='G' or Valor=='R') and Break: #Se indico el boton de escalonar o sistema de ecuaciones y no hay una fila de puro ceros
            CoF=n-1 #Existe mas filas
            if m>n:
                CoF=m-1 #Existe mas columnas
            for i in range(CoF,-1,-1): #recorrer las columnas
                for j in range(i-1,-1,-1): #recorrer las filas desde los pivotes para arriba
                    try:
                        if Matriz[i,i]==0:#pivote 0
                            V,Matriz=self.Intercambiar(Matriz,i,Valor) #Ejecutar el metodo que intercambia columnas de la matriz
                            if V=='True':#Existe columnas de intercambio para dar un valor diferente de cero al pivote
                                Label(self.BloqueMostrar,text='Intercambiando fila',font=(10)).pack()
                                self.MostrarMatriz(Matriz,m,n,Valor) #Mostrar el paso realizado
                            else:
                                Break=False
                                break #romper bucle por que se encontro un pivote cero

                            Label(self.BloqueMostrar,text='Intercambiando fila',font=(10)).pack()
                            self.MostrarMatriz(Matriz,m,n,Valor)

                        if Matriz[j,i] != 0.0:  #el elemento en ejecucion es diferente de 0                        
                            Factor = Matriz[j,i]/Matriz[i,i] #Guardar la division en ejecucion entre el elemento y el pivote
                            Label(self.BloqueMostrar,text="Operando: Fila{} + ({})Fila{}".format(j+1,-Factor,i+1),font=(10)).pack()

                            #restar a toda la fila la division guardada multiplicada por la fila del pivote respectivo
                            Matriz[j,i:m]=Matriz[j,i:m] - Factor*Matriz[i,i:m]
                            self.MostrarMatriz(Matriz,m,n,Valor) #Mostrar el paso realizado
                    except IndexError:
                        pass
        
        #Dividir los pivotes entre si para obtener el valor de 1
        if (Valor=='G' or Valor=='R') and Break: #Se indico el boton de escalonar o sistema de ecuaciones y no hay una fila de puro ceros
            for i in range(0,n): #recorre fila
                for j in range(0,m): #recorre columna
                    if Matriz[i,j]!=0: 
                        if Matriz[i,j]!=1: 
                            Label(self.BloqueMostrar,text="Multiplicando la fila {} por {}".format(i+1,1/Matriz[i,j]),font=(10)).pack()
                            Matriz[i]=Matriz[i]/Matriz[i,j] #Dividir toda la fila entre el pivote
                            self.MostrarMatriz(Matriz,m,n,Valor) #Mostrar el paso realizado
                        break #optimizar
                    
        if Valor=='G': #se indico el boton sistema de ecuaciones
            #Almacenar valores para x1,x2,x3,etc
            for i,l in zip(range(0,n),self.Arreglo): #recorrer indices ordenados e indices del arreglo por si hubo intercambio de filas
                Valores = []
                FrameResul=Frame(self.BloqueMostrar)
                FrameResul.pack()
                for j in range(0,m): #recorrer indices de columnas
                    if j<m-1: #almacenar coeficientes por fila
                        Valores.append(Matriz[i,j])                
                    else: #almacenar termino independiente por fila
                        Resultado=Matriz[i,j]

                #Mostrar valor de x1,x2,x3,etc
                Label(FrameResul,text='X{} = {}'.format(l+1,Resultado),font=(10)).grid(row=1,column=0)

                
    def Intercambiar(self,matriz,n,tipo): #Metodo para el intercambio de columnas 
        Arreglo=[]
        f,c=matriz.shape #obtener N° de filas y columnas de la matriz
        for i in range(0,c):    
            Arreglo.append(i) #Formar un arreglo de los indices de una matriz

        UC=c-1 #Matriz
        if tipo=='G':
           UC=c-2 #Sistema de ecuaciones

        k=n
        while k<UC and matriz[n,n]==0: #Mientras el pivote sea 0
            Temp=Arreglo[n] #Guardamos el numero de columna del pivote 0 
            Arreglo[n]=Arreglo[k+1] #Intercambiamos la columna del pivote 0 con el resto de la matriz        

            Temp2=self.Arreglo[n]

            if (matriz[:,Arreglo])[n,n]!=0: #El intercambio generó un pivote diferente a 0
                Arreglo[k+1]=Temp
                matriz=matriz[:,Arreglo] #Guardar la matriz con las columnas intercambiadas
                self.Arreglo[n]=self.Arreglo[k+1]
                self.Arreglo[k+1]=Temp2
                
            else:
                Arreglo[n]=Temp #Matriz original
            k+=1
      
        if matriz[n,n]!=0:
            return 'True',matriz #Devolver matriz con columna intercambiada
        else:
            return 'False',matriz #Devolver matriz original     
       