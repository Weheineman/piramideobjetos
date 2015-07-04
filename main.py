class Celda:
  def __init__(self,h1,h2):
    self.val=0
    self.hijo1=h1
    self.hijo2=h2
  
  def Resolv(self):
    flag=False
    #Parte fea de fijarse
    
    flag=flag or hijo1.Resolv() or hijo2.Resolv()
    return flag
    
  def Solved(self):
    flag=true
    if(self.val==0)
      flag=false
    flag=flag and hijo1.Solved() or hijo2.Solved()
    
  def setval(self, a)
    self.val=a


class CeldaAbajo(Celda):
  def __init__(self)
    self.valor=0
    
  def Resolv(self):
    return false


#HACER PIRAMIDE A MANO
piso0=CeldaAbajo()
piso1=CeldaAbajo()
piso2=CeldaAbajo()
piso3=CeldaAbajo()
piso4=CeldaAbajo()
piso5=CeldaAbajo()
celda40=(piso0,piso1)
celda41=(piso1,piso2)
celda42=(piso2,piso3)
celda43=(piso3,piso4)
celda44=(piso4,piso5)
celda30=(celda40,celda41)
celda31=(celda41,celda42)
celda32=(celda42,celda43)
celda33=(celda43,celda44)
celda20=(celda30,celda31)
celda21=(celda31,celda32)
celda22=(celda32,celda33)
celda10=(celda20,celda21)
celda11=(celda21,celda22)
celda00=(celda10,celda11)


#INPUT
print ("Ingrese los valores de las celdas por fila desde arriba y desde la izquierda, ingrese 0 en caso de que la celda no tenga contenido:\n")
celda00.setval(input())
celda10.setval(input())
celda11.setval(input())
celda20.setval(input())
celda21.setval(input())
celda22.setval(input())
celda30.setval(input())
celda31.setval(input())
celda32.setval(input())
celda33.setval(input())
celda40.setval(input())
celda41.setval(input())
celda42.setval(input())
celda43.setval(input())
celda44.setval(input())
piso0.setval(input())
piso1.setval(input())
piso2.setval(input())
piso3.setval(input())
piso4.setval(input())
piso5.setval(input())


#PROCESO
sinresolver=true
while(sinresolver)
  sinresolver=celda00
  .Resolv()

#OUTPUT
print (celda00.val)
print (str(celda10.val)+str(celda11.val))
print (str(celda20.val)+str(celda21.val)+str(celda22.val))
print (str(celda30.val)+str(celda31.val)+str(celda32.val)+str(celda33.val))
print (str(celda40.val)+str(celda41.val)+str(celda42.val)+str(celda43.val)+str(celda44.val))
print (str(piso1.val)+str(piso2.val)+str(piso3.val)+str(piso4.val)+str(piso5.val)+str(piso6.val))
