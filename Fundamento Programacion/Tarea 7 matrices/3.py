#importamos las librerias
import os
import sys
import time


print('Programa Lee una matriz 4x3 entera calcula la suma de los elementos de cada fila y determina cuál es la fila que tiene la mayor suma.\n')
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
    sm,sm1,sm2,sm3=0,0,0,0
    matriz=[]
    for i in range(4):
        matriz.append([0]*3)
    
    print('Digite un numero y pulse enter hasta que la matriz este completa.\n')
    for i in range (4):
        for d in range(3):
            try:
                matriz[i][d]=int(input("Digite el elemento "+str(i+1)+":"+str(d+1)+"  >>> "))
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
                
    for i in range(1):
        for d in range(3):
            sm+=matriz[i][d]
    for i in range(1,2):
        for d in range(3):
            sm1+=matriz[i][d]
    for i in range(2,3):
        for d in range(3):
            sm2+=matriz[i][d] 
    for i in range(3,4):
        for d in range(3):
            sm3+=matriz[i][d]  

    if sm > sm1 and sm > sm2 and sm > sm3:
        print(matriz,'\n')
        print ("La mayor suma esta en la fila 1\n")
        cont()
    if sm1 > sm and sm1 > sm2 and sm1 > sm3:
        print(matriz,'\n')
        print ("La mayor suma esta en la fila 2\n")
        cont()
    if sm2 > sm and sm2 > sm1 and sm2 > sm3:
        print(matriz,'\n')
        print ("La mayor suma esta en la fila 3\n")
        cont()
    if sm3 > sm and sm3 > sm1 and sm3 > sm2:
        print(matriz,'\n')
        print ("La mayor suma esta en la fila 4\n")
        cont()
		
proceso()
