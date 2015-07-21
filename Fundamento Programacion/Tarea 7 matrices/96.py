#importamos las librerias
import os
import sys
import time


print('Programa Lee una matriz 4x4 entera y determina cuántas veces se repita en ella el número mayor.\n')
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
    cont=0
    fi,co=0,0
    matriz=[]
    for i in range(4):
        matriz.append([0]*4)
    
    print('Digite un numero y pulse enter hasta que la matriz este completa.\n')
    for i in range (4):
        for d in range(4):
            try:
                matriz[i][d]=int(input('>>> '))
            except ValueError:
                print("!Error! debe ser numeros enteros vuelva a intentar\n")
                proceso()
                
    for i in range(4):
        for d in range(4):
            if matriz[fi][co] < matriz[i][d]:
                fi,co=i,d
                
    for i in range(1,4):
        for d in range(1,4):
            if matriz[fi][co] == matriz[i][d]:
                cont+=1
       
    print(matriz,"\n")
    print("El numero mayor es:",matriz[fi][co],"Se encuentra repetido:",cont,'veces\n')
    r()
    
def r():
    cont()
    
proceso()

