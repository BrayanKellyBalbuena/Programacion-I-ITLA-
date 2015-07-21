#importamos las librerias
import os
import sys
import time


print(' Programa Lee una matriz 4x6 entera y determina cuál es el mayor dato almacenado en ella que pertenezca a la Serie de Fibonacci.\n')
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

def  proceso():
    fi,co=0,0
    matriz=[]
    for i in range(4):
        matriz.append([0]*6)
    
    print('Digite un numero y pulse enter hasta que la matriz este completa.\n')
    for i in range (4):
        for d in range(6):
            try:
                matriz[i][d]=int(input("Digite el elemento "+str(i+1)+":"+str(d+1)+" >>> "))
            except ValueError:
                print("!Error! debe ser numeros enteros vuelva a intentar\n")
                proceso()

    print("")            
    for i in matriz:
        str_fila = ""
        for v in i:
            str_fila +="\t"+str(v)
        print(str_fila)    
        print("")
        
       
    for i in range(4):
        for d in range(6):
            if fib(matriz[i][d]) == True:
                if matriz[fi][co] < matriz[i][d]:
                    fi,co=i,d

    print("El mayor numero se encuentra en fila:",fi+1,"columna:",co+1)
    cont()


def fib(matriz):
    c=False
    a, b = 0, 1
    while a < 99*99:
        a, b = b, a+b
        if matriz == a:
            c = True
            return c
        
        
        
        
proceso()
