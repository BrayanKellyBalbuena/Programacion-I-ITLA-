import os
import sys
import time
print(""" Programa lee 10 números enteros, almacena en un vector y determina cuántos datos almacenados son múltiplos de 3.\n""")

def clear():
    if os.name == "Posix":
        return os.system('clear')
    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        return os.system('cls')

def cont():
    resp = input("Digite S para continuar o N para salir\n")
    if resp == 'S':
        proceso()
    elif resp == 'N':
        c = int (5)
        while c != 0:
            time.sleep(1)
            clear()
            print("El programa se cirra en",c,"segundos !Good Bye!\n")
            c -= 1
            if c == 0:
                sys.exit(1)
    else:
        print("!Error debe ser S o N!\n")
        cont()

def proceso():
    c=0
    vector =[]
    print("Digite un numero y pulse enter hasta que sean 10 numeros enteros")
    for ind in range(10):
            try:
                vector.insert((ind),int(input('>>> ')))
            except ValueError:
                print("!Error! debe ser numeros enteros vuelva a intentar\n")
                proceso()
    for  ind in range(10) :
        if vector[ind] % 3 == 0:
            c+=1
    
    if c==0 :
        print("No hay multiplos de 3 en el vector\n")
    else:
        print("Hay",c,"multiplos de 3 en el vector\n")
    cont()
    
proceso()
