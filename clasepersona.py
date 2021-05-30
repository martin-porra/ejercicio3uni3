
class persona:
    __nombre = ''
    __direccion = ''
    __dni = ''

    def __init__(self,nom,dire,dni):
        self.__nombre = nom
        self.__direccion = dire
        self.__dni = dni


    def nom(self):
     return self.__nombre
    def dni(self):
        return self.__dni
    def dire(self):
      return self.__direccion