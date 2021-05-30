import csv
from claseteller import taller

class manejadortaller:
    __talleres = []
    def __init__(self):
     with open('Talleres.csv', newline='') as File:
      reader = csv.reader(File, delimiter=(','))
      firstline = True
      for row in reader:
        if firstline:
         firstline = False
        else:
         objeto =  taller(row[0],row[1],row[2],row[3])
         self.__talleres.append(objeto)

    def mostrar(self):
        for x in range(0,len(self.__talleres)):
            print(self.__talleres[x].nombre())

    @classmethod
    def inscri(cls,x):
        return cls.__talleres[int(x)-1]
    @classmethod
    def actualizar(cls,x):
        cls.__talleres[int(x)-1].actua()
