#importamos las librerias
import os
import sys
import time
print("Programa lee 10 números enteros, almacenarlos en un vector Luego leer un entero y determinar cuantos divisores exactos tiene este último número entre los valores almacenados en el vector..\n")


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
    dvex=0
    print("Digite un numero y pulse enter hasta que sean 10 numeros enteros")
    for ind in range(10):
            try:
                vector.insert((ind),int(input('>>> ')))
            except ValueError:
                print("!Error! debe ser numeros enteros vuelva a intentar\n")
                proceso()
    n=lee_num()            
    for ind in range(10):
        if n % vector[ind]== 0:
            dvex+=1
    if dvex ==0:
        print("No hay divisores exactos de",n,"en el vector\n")
        cont()
    else:
        print("Hay",dvex,"divisores exactos de",n,"en el vector\n")
        cont()
            
def lee_num():
    try:
        num = int(input("Digite un numero que desea comprobar\n>>>>"))
    except :
        print("Debe ser un numero entero")
        lee_num()
    return num

    

proceso()
