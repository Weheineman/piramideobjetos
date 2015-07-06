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
		flag=flag and self.hijo1.Solved() and self.hijo2.Solved()
		return flag
		
	def setval(self, a):
		self.val=a

	def tostr(self):
		return str(self.val)


class CeldaAbajo(Celda):
	def __init__(self):
		self.val=0
		
	def Resolv(self):
		return False

	def Solved(self): 
		return (self.val!=0)


#HACER PIRAMIDE A MANO
piso0=CeldaAbajo()
piso1=CeldaAbajo()
piso2=CeldaAbajo()
piso3=CeldaAbajo()
piso4=CeldaAbajo()
piso5=CeldaAbajo()
celda40=Celda(piso0,piso1)
celda41=Celda(piso1,piso2)
celda42=Celda(piso2,piso3)
celda43=Celda(piso3,piso4)
celda44=Celda(piso4,piso5)
celda30=Celda(celda40,celda41)
celda31=Celda(celda41,celda42)
celda32=Celda(celda42,celda43)
celda33=Celda(celda43,celda44)
celda20=Celda(celda30,celda31)
celda21=Celda(celda31,celda32)
celda22=Celda(celda32,celda33)
celda10=Celda(celda20,celda21)
celda11=Celda(celda21,celda22)
celda00=Celda(celda10,celda11)


#INPUT
print ("Ingrese los valores de las celdas por fila desde arriba y desde la izquierda, ingrese 0 en caso de que la celda no tenga contenido:")
print("Ingrese la celda número 1 de la fila 1")
celda00.setval(int(input()))
print("Ingrese la celda número 1 de la fila 2")
celda10.setval(int(input()))
print("Ingrese la celda número 2 de la fila 2")
celda11.setval(int(input()))
print("Ingrese la celda número 1 de la fila 3")
celda20.setval(int(input()))
print("Ingrese la celda número 2 de la fila 3")
celda21.setval(int(input()))
print("Ingrese la celda número 3 de la fila 3")
celda22.setval(int(input()))
print("Ingrese la celda número 1 de la fila 4")
celda30.setval(int(input()))
print("Ingrese la celda número 2 de la fila 4")
celda31.setval(int(input()))
print("Ingrese la celda número 3 de la fila 4")
celda32.setval(int(input()))
print("Ingrese la celda número 4 de la fila 4")
celda33.setval(int(input()))
print("Ingrese la celda número 1 de la fila 5")
celda40.setval(int(input()))
print("Ingrese la celda número 2 de la fila 5")
celda41.setval(int(input()))
print("Ingrese la celda número 3 de la fila 5")
celda42.setval(int(input()))
print("Ingrese la celda número 4 de la fila 5")
celda43.setval(int(input()))
print("Ingrese la celda número 5 de la fila 5")
celda44.setval(int(input()))
print("Ingrese la celda número 1 de la fila 6")
piso0.setval(int(input()))
print("Ingrese la celda número 2 de la fila 6")
piso1.setval(int(input()))
print("Ingrese la celda número 3 de la fila 6")
piso2.setval(int(input()))
print("Ingrese la celda número 4 de la fila 6")
piso3.setval(int(input()))
print("Ingrese la celda número 5 de la fila 6")
piso4.setval(int(input()))
print("Ingrese la celda número 6 de la fila 6")
piso5.setval(int(input()))


#PROCESO
sinresolver=True
while(sinresolver):
  sinresolver=celda00.Resolv()

#OUTPUT
if(celda00.Solved()):
	print ("")
	print ("RESULTADO")
	print ("\t"+"\t"+"\t"+"\t"+"\t"+celda00.tostr()+"\t"+"\t"+"\t"+"\t"+"\t")
	print ("")
	print ("\t"+"\t"+"\t"+"\t"+celda10.tostr()+"\t"+"\t"+celda11.tostr()+"\t"+"\t"+"\t"+"\t")
	print ("")
	print ("\t"+"\t"+"\t"+celda20.tostr()+"\t"+"\t"+celda21.tostr()+"\t"+"\t"+celda22.tostr()+"\t"+"\t"+"\t")
	print ("")
	print ("\t"+"\t"+celda30.tostr()+"\t"+"\t"+celda31.tostr()+"\t"+"\t"+celda32.tostr()+"\t"+"\t"+celda33.tostr()+"\t"+"\t")
	print ("")
	print ("\t"+celda40.tostr()+"\t"+"\t"+celda41.tostr()+"\t"+"\t"+celda42.tostr()+"\t"+"\t"+celda43.tostr()+"\t"+"\t"+celda44.tostr()+"\t")
	print ("")
	print (piso0.tostr()+"\t"+"\t"+piso1.tostr()+"\t"+"\t"+piso2.tostr()+"\t"+"\t"+piso3.tostr()+"\t"+"\t"+piso4.tostr()+"\t"+"\t"+piso5.tostr())

else:
	print("")
	print("No se puede resolver. Al menos no por un niño de 10 años.")
