from claseinscripciones import ins
from  clasemanejadortaller import  manejadortaller
from datetime import  date
import csv
class manejadorins:
    __ins = []
    def __init__(self):
        self.__ins = []

    def añadi(self,persona):
     print('en que taller desea inscribirse?')
     print('1-lol / 2-dota / 3-rocket / 4-csgo / 5-tf2')
     op = input()
     today = date.today()
     taller = manejadortaller.inscri(op)
     inscrip = ins(today)
     inscrip.añad(persona,taller)
     self.__ins.append(inscrip)
     manejadortaller.actualizar(op)

    def mostrar(self):
        for x in range(0,len(self.__ins)):
         print(self.__ins[x].devolver())

    def buscar(self):
     print('ingresar dni de persona a buscar')
     dni = input()
     for x in range(0,len(self.__ins)):
         if dni == self.__ins[x].dni():
           self.__ins[x].info()

    def mostrartaller(self):
        print('ingresar identificador del taller')
        i = input()
        for x in range(0,len(self.__ins)):
            if i == self.__ins[x].idtall():
                self.__ins[x].infoper()

    def alta(self):
     dni = input('ingrese dni de persona ')
     for x in range(0,len(self.__ins)):
          if self.__ins[x].dni() == dni:
           self.__ins[x].alta()
          else:
           print('no se encontro una persona con el dni '+ dni + ' asociado')
    def escribir(self):
        p = []
        he = ['dni','idtaller','fehca','pago']
        with open('inscripciones.csv', 'w') as csvfile:
         writer = csv.writer(csvfile, delimiter=',')
         writer.writerow(he)
         for x in range(0,len(self.__ins)):
          p.append(self.__ins[x].dni())
          p.append(self.__ins[x].idtall())
          p.append(self.__ins[x].fecha())
          p.append(self.__ins[x].pago())
          writer.writerow(p)
          p.clear()