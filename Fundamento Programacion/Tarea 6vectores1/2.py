import os
import sys
import time
os.system('cls')
print("Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor número par leído.\n")
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
    vector=[]
    print("Digite un numero y pulse enter hasta que sean 10 numeros enteros\n")
    for ind in range(10):
        try:
            vector.insert(ind,int(input('>>> ')))
        except ValueError:
            print("!Error debe ser numeros enteros vuelva a intentar\n!")
            proceso()
    mp = 0        
    pos_may =int(0)
    for ind in range (1,10):
        if vector[pos_may] % 2 == 0:
            mp = pos_may + 1
        if (vector[ind] % 2 == 0) and vector[pos_may] % 2 !=0 or vector[pos_may] < vector[ind]:
            pos_may = ind
    if mp == 0:
        print("No hay numeros pares digitados no se puede aplicar el porgrama")
        cont()
    else:
           print("El mayor numero par se encuentra en la posicion",mp,'\n')
           cont()
    
proceso()    
             
