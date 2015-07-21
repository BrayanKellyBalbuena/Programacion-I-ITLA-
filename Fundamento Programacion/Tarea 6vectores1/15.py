#importamos las librerias
import os
import sys
import time
print("Programa lee 10 números enteros, almacena en un vector y determina a cuánto es igual el promedio entero de los factoriales de cada uno de los números leídos.\n")


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
    prom,di,s = 0,1,0
    print("Digite un numero y pulse enter hasta que sean 10 numeros enteros")
    for ind in range(10):
            try:
                vector.insert((ind),int(input('>>> ')))
            except ValueError:
                print("!Error! debe ser numeros enteros vuelva a intentar\n")
                proceso()
    for ind  in range(10):
        prom += fact(vector[ind])
        s+=1
    print("El promedio es",int(prom/s),"\n")
    cont()
    
def fact(x):
    if x == 0 :
        return 0
    fac=1
    c=1
    while c <= x:
        fac *= c
        c += 1
    return fac

proceso()
