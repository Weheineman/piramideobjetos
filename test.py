class Celda:
	def __init__(self,h1,h2):
		self.val=0
		self.hijo1=h1
		self.hijo2=h2
  
	def Resolv(self):
		flag=False
		#Parte fea de fijarse
		if(self.val==0):
			if( (self.hijo1.val!=0) and (self.hijo2.val!=0) ):
				self.val=self.hijo1.val+self.hijo2.val
				flag=True
		else:
			if( (self.hijo1.val==0) and (self.hijo2.val!=0) ):
				self.hijo1.val=self.val-self.hijo2.val
				flag=True
			if( (self.hijo2.val==0) and (self.hijo1.val!=0) ):
				self.hijo2.val=self.val-self.hijo1.val
				flag=True
		
		flag=flag or self.hijo1.Resolv() or self.hijo2.Resolv()
		return flag
		
	def Solved(self):
		flag=True
		if(self.val==0):
			flag=False
		flag=flag and self.hijo1.Solved() or self.hijo2.Solved()
		
	def setval(self, a):
		self.val=a


class CeldaAbajo(Celda):
	def __init__(self):
		self.val=0
		
	def Resolv(self):
		return False

	def Solved(self):
  		return self.val==0


#HACER PIRAMIDE A MANO
piso4=CeldaAbajo()
piso5=CeldaAbajo()
celda44=Celda(piso4,piso5)

#INPUT
print ("Ingrese los valores de las celdas por fila desde arriba y desde la izquierda, ingrese 0 en caso de que la celda no tenga contenido:")
print("Ingrese la celda número 1 de la fila 1")
celda44.setval(input())
print("Ingrese la celda número 1 de la fila 2")
piso4.setval(input())
print("Ingrese la celda número 6 de la fila 6")
piso5.setval(input())


#PROCESO
sinresolver=True
while(sinresolver):
  sinresolver=celda44.Resolv()

#OUTPUT
print ("")
print ("RESULTADO")
print (celda44.val)
print ("")
print (piso4.val)
print (piso5.val)
