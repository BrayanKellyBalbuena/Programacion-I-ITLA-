#importamos las librerias
import os
import sys
import time


print('Programa Lee una matriz 5x3 entera y determina en qué columna está el menor número par..\n')
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
    nmpc=0
    mnp = 99**123
    matriz=[]
    for i in range(5):
        matriz.append([0]*3)
    
    print('Digite un numero y pulse enter hasta que la matriz este completa.\n')
    for i in range (5):
        for d in range(3):
            try:
                matriz[i][d]=int(input("Digite el elemento "+str(i+1)+":"+str(d+1)+" >>> " ))
            except ValueError:
                print("!Error! debe ser numeros enteros vuelva a intentar\n")
                proceso()
    print('\n')            
    for i in range(5):
        for d in range(3):
           if matriz[i][d] % 2 == 0 and matriz[i][d] < mnp:
               mnp = matriz[i][d]
               nmpc = d
    if mnp == 99**123:
        print("No hay numeros pares en la matriz\n")
        cont()
    else:
        print ("El menor par esta en la columna",nmpc+1,"\n")
        cont()
    
proceso()
