from datetime import date
from clasepersona import  persona
from claseteller import  taller

class ins:
    __fechainscrip = date
    __pago = bool
    __taller = None
    __persona = None

    def __init__(self,fecha,pago = False):
        self.__fechainscrip = fecha
        self.__pago = pago
    def añad(self, persona, taller):
        self.__persona = persona
        self.__taller = taller
    def devolver(self):
        print(self.__fechainscrip)
        print(self.__taller.nombre())
        print(self.__persona.nom())

    def dni(self):
      return self.__persona.dni()

    def info(self):
     print('nombre taller '+ self.__taller.nombre())
     print('monto: ' + self.__taller.monto())

    def idtall(self):
     return self.__taller.id()
    def fecha(self):
     return self.__fechainscrip
    def pago(self):
        return self.__pago

    def infoper(self):
        print('nombre: ' + self.__persona.nom())
        print('direccion: ' + self.__persona.dire())
        print('dni: ' + self.__persona.dni())

    def alta(self):
     self.__pago = True
     print('pago de alta')