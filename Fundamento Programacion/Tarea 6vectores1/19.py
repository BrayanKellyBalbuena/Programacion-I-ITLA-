import os
import sys
import time
print("""programa que leer 10 números enteros, almacena en un vector y determina si el promedio entero de dichos números es un número primo.\n""")
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
    promedio=0
    vector =[]
    print("Digite un numero y pulse enter hasta que sean 10 numeros enteros")
    for ind in range(10):
            try:
                vector.insert((ind),int(input('>>> ')))
            except ValueError:
                print("!Error! debe ser numeros enteros vuelva a intentar\n")
                proceso()
    for  ind in range(10):
        promedio += vector[ind]
    promedio //=10
    print("El promedio",Prom(promedio))
        
    cont()


def Prom(t):
    t
    if t < 0:
        t *= int(-1)
    x =int(0)
    p =int(1)
    while p <= t:
        if t % p == 0:
            x += int(1)
        p += 1
    if x > 2:
        pri = "no es primo\n"
        return pri
    else:
        pri = " es primo\n"
        return pri    
proceso()
