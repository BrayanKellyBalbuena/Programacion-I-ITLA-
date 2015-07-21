#importamos las librerias
import os
import sys
import time
print("Programa lee 10 números enteros, almacenarlos en un vector y determina cuántos números terminan en dígito primo..\n")


def clear(): 
    if os.name == "posix":
        return os.system ('clear')
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ('cls')


def cont():
    resp =input("Digite S para continuar o N Para salir'\n")
    if resp == 'S':
        proceso()
    elif resp == 'N':
        c= int(5)
        while c != 0:
            time.sleep(1)
            clear()
            print("El programa se cirra en",c,"segundos !Good Bye!\n")
            c-=1
            if c == 0:
                sys.exit(1)
    else:   
        print("!Error! debe ser S o N\n")
        cont()

#Creacion de la  funcion que hara todo el proceso
def proceso():
    vector =[]
    c=0
    print("Digite un numero entero de mas de 1 digito y pulse enter hasta que sean 10 numeros enteros")
    for ind in range(10):
            try:
                vector.insert((ind),int(input('>>> ')))
            except ValueError:
                print("!Error! debe ser numeros enteros vuelva a intentar\n")
                proceso()
            if  error(vector[ind]) == 0:
                print("!Error! debe ser  numeros de mas de 1 digito  entero vuelva a intentar\n")
                proceso()    
    for ind in range(10):
        rpz = vector[ind] % 10
        c+=Proce(rpz)
    print("hay ",c," primos")
    
         

def Proce(n): 

   if n < 0:
      n *= int(-1)
   x =int(0)
   p =int(1)
   while p <= n:
      if n % p == 0:
         x += int(1)
      p += 1
   if x > 2:
      pri = 0
      return pri
   else:
      pri = 1
      return pri
    
def error(x):
    if x < 10 :
        return 0

proceso()    
