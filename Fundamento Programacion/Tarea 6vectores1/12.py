#importamos las librerias
import os
import sys
import time
print(""" Leer 10 números enteros, almacenarlos en un vector y determinar cuáles son los números múltiplos de 5 y en qué posiciones están.\n""")

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
    print("Digite un numero y pulse enter hasta que sean 10 numeros enteros\n")
    for ind in range(10):
            try:
                vector.insert((ind),int(input('>>> ')))
            except ValueError:
                print("!Error! debe ser numeros enteros vuelva a intentar\n")
                proceso()
    pos_m5 =0
    p=1
    print("Esta en la posicion:\n")
    for ind in range(10):
        if vector[ind] % 5 == 0:
            pos_m5+=1
            print(ind+1)
   
    if pos_m5 ==0:
            print("No hay multiplos de 5\n")
    cont()

       
proceso()
