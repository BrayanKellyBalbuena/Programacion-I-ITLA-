#importamos las librerias
import os
import sys
import time


print('Programa Lee una matriz 4x6 entera y determina en qué posiciones están los menores por fila.\n')
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
    mnp = 99**123
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
                
    print('\n')            
    for i in range(4):
        for d in range(6):
           if matriz[i][d] < mnp:
               mnp = matriz[i][d]
               nmp = d+1
           if  d == 5:
               print ("El menor en la fila",i+1,"","esta en la columna",nmp,'\n')
               mnp = 99**123

    cont()
proceso()
