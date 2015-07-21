#importamos las librerias
import os
import sys
import time
print("Programa lee 10 números enteros, almacenarlos en un vector y determinar cuántos de los números leídos son números primos terminados en 3.\n")


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
    for ind in range(10):
        x,p,c = 0,1,0
        while p <= vector[ind]:
            if vector[ind] % p == 0:
                x +=1
            p+=1
        if x == 2 and vector[ind] % 10 == 3 :
            c+=1
    if c == 0:
        print("No hay numeros primos multilplos de 3")
    else:
        print("Hay",c,"numeros primos multiplos de 3")
    cont()

proceso()    
