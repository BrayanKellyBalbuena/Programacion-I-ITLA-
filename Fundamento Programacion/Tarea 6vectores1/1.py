#importamos las librerias
import os
import sys
import time
os.system('cls')


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
    print("""Programa que lee 10 enteros y los almacena en un vector y determina en qué posición del vector está elmayor número leído.\n""")
    vector =[]
    print("Digite un numero y pulse enter hasta que sean 10 numeros enteros")
    for ind in range(10):
            try:
                vector.insert((ind),int(input('>>> ')))
            except ValueError:
                print("!Error! debe ser numeros enteros vuelva a intentar\n")
                proceso()
    pos_may =int(0)
    p=1
    for ind in range(1,10):
        if vector[ind] > vector[pos_may]:
            pos_may = ind
            p=pos_may+1
    print("El numero mayor esta en la posicion",p,'\n')
    cont()
    

       
proceso()