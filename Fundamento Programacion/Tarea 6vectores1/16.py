#importamos las librerias
import os
import sys
import time
print("""Programa lee 10 números enteros, almacena en un vector y mostrar en pantalla todos los enteros
comprendidos entre 1 y cada uno de los dígitos de cada uno de los números almacenados en el vector.\n""")


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
    com =[]
    vector =[]
    mp = 1
    print("Digite un numero entero de mas de 1 digito y pulse enter hasta que sean 10 numeros enteros")
    for ind in range(10):
            try:
                vector.insert((ind),int(input('>>> ')))
            except ValueError:
                print("!Error! debe ser  numeros de mas de 1 digito  entero vuelva a intentar\n")
                proceso()
            if  error(vector[ind]) == 0:
                print("!Error! debe ser  numeros de mas de 1 digito  entero vuelva a intentar\n")
                proceso()           
    for ind in range(10):
        pot,dig,aux,n1 = 0,0,0,1
        cont = 0
        aux = vector[ind]
        while aux > 0:
            cont +=1
            aux //= 10
                
        aux = vector[ind]
        i = 1
        while i <= cont:
            pot = 10 ** (cont - i)
            dig = aux // pot
            aux =aux - dig * pot
            i += 1
            while n1 < dig:
                com.append(n1)
                n1+=1
            n1=1

    print("\n",com)

def error(x):
    if x < 10 :
        return 0

proceso()
