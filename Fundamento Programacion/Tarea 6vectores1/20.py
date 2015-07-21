#importamos las librerias
import os
import sys
import time
os.system('cls')
print( "Programa que Lee 10 números enteros, almacena en un vector y determinar si la semisuma entre el valor mayor y el valor menor es un número par\n")

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
    print("Digite un numero y pulse enter hasta que sean 10 numeros enteros")
    for ind in range(10):
            try:
                vector.insert((ind),int(input('>>> ')))
            except ValueError:
                print("!Error! debe ser numeros enteros vuelva a intentar\n")
                proceso()
    pos_may =int(0)
    pos_men = 0
    for ind in range(1,10):
        if vector[ind] > vector[pos_may]:
            pos_may = ind
            
        if vector[ind] < vector[pos_men]:
           pos_men = ind
       
    print("La semi suma del numero mayor  y el  menor es:",par(vector[pos_may],vector[pos_men]))
    cont()

def par(x,y) :
    if int((x+y)/2) % 2 == 0:
        return " es par\n"
    else:
        return " es par\n"

       
proceso()
