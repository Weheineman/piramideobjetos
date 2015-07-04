class Celda:
  def __init__(self,h1,h2):
    self.valor=0
    self.hijo1=h1
    self.hijo2=h2
  
  def Resolv(self):
    flag=False
    #Parte fea de fijarse
    flag=flag or hijo1.Resolv() or hijo2.Resolv()
    return flag
    
  def setval(self, a)
    


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


#PROCESO
sinresolver=true
while(sinresolver)
  sinresolver=Cima.Resolv()

#OUTPUT
