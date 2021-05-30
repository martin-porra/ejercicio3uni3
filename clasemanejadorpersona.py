from  clasemanejadorinscrip import  manejadorins
from clasepersona import  persona
class manejadorpersona:

    def __init__(self):
        self.__personas = []
    def añadir(self,manejador):
     print('inscribir persona')
     nom = input('ingresa nombre ')
     dire = input('ingresar direccion ')
     dni = input('ingrese dni ')
     perso = persona(nom,dire,dni)
     self.__personas.append(perso)
     print('desea inscribirse en un taller?')
     res = input('si/no ')
     if res == 'si':
         manejador.añadi(perso)



