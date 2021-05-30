import csv
from clasemanejadorpersona import  manejadorpersona
from clasemanejadortaller import  manejadortaller
from  clasemanejadorinscrip import  manejadorins
def menu():
 print('1 - añadir persona')
 print('2 - buscar dni y mostrar taller y lo que adeuda')
 print('3 - buscar id taller listar persona')
 print('4 - ingresar dni y dar de alta')
 print('5 - crear archivo de inscripciones')
if __name__ == '__main__':
 manejatalleres =  manejadortaller()
 manejapersona = manejadorpersona()
 manejain = manejadorins()
 band = True
 while band == True:
  print('ingresar opcion')
  menu()
  op = input()
  if op == '1':
   manejapersona.añadir(manejain)
  elif op == '2':
   manejain.buscar()
  elif op == '3':
   manejain.mostrartaller()
  elif op == '4':
   manejain.alta()
  elif op == '5':
   manejain.escribir()
  else:
   band = False
 print('termino programa')
