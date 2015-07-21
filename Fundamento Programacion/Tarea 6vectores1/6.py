#importamos las librerias
import os
import sys
import time


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
    print("""Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces está repetidoel mayor\n.""")
    vector =[]
    print("Digite un numero y pulse enter hasta que sean 10 numeros enteros")
    for ind in range(10):
            try:
                vector.insert((ind),int(input('>>> ')))
            except ValueError:
                print("!Error! debe ser numeros enteros vuelva a intentar\n")
                proceso()
    pos_may =int(0)
    p=0
    for ind in range(1,10):
        if vector[ind] > vector[pos_may]:
            pos_may = ind
    for ind in range(10):
        if vector[pos_may]==vector[ind]:
            p+=1
    if p == 1:
        print("El numero mayor no esta repetido\n")
    else:
        print("El numero mayor esta repetido:",p,"\n")    
    
    cont()
    

       
proceso()
