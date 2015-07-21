#importamos las librerias
import os
import sys
import time


print(' Programa Lee una matriz 5x3 entera y determina en qué fila y columna está el mayor número que comienza con el dígito 4.\n')
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
    mnp,t,f,c=-99**99,0,0,0
    matriz=[]
    for i in range(5):
        matriz.append([0]*3)
    print('Digite un numero y pulse enter hasta que la matriz este completa.\n')
    for i in range (5):
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
                
    for i in range(5):
        for d in range(3):
            pot,dig,cont,aux = 0,0,0,0
            aux = matriz[i][d]
            while aux > 0:
                cont+=1
                aux //= 10
                
            aux = matriz[i][d]
            tope = 1
            while tope == 1:
                pot = 10 ** (cont - tope)
                dig = aux // pot
                dig4=dig
                tope+= 1

            if dig4 == 4 and matriz[i][d] > mnp:
                mnp = matriz[i][d]
                t +=1
                f,c=i,d
    if t == 0:
        print(matriz,'\n')
        print("no hay numeros que comienzan en cuatro en la matriz\n")
        r()
    else:
        print(matriz,"\n")
        print("El mayor numero que comienza en 4 esta en la fila:",f+1,"columna:",c+1,'\n,')
        r()
        
def r():
    cont()
    
proceso()
