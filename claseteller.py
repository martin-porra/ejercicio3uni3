
class taller:
    __idtaller = 0
    __nombre = ''
    __vacante = 0
    __montoins = 0

    def __init__(self,id = 0,nom = '',vac=0,mon=0):
        self.__idtaller  = id
        self.__nombre = nom
        self.__vacante = vac
        self.__montoins = mon

    def nombre(self):
        return self.__nombre
    def actua(self):
        self.__vacante = int(self.__vacante) - 1

    def monto(self):
      return  self.__montoins
    def id(self):
        return self.__idtaller