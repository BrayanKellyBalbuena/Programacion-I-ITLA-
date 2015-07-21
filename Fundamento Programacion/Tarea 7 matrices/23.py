#importamos las librerias
import os
import sys
import time


print('Programa Lee dos matriz 5x5 entera y determina si el promedio entero de los números mayores de cada fila de una matriz es igual al promedio de los números mayores de cada fila de la otra matriz.\n.')
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
    mnp,mnp1,prome,prome1,div,div1,may,may1 = -99**123,-99**123,0,0,1,1,0,0
    matriz=[]
    for i in range(5):
        matriz.append([0]*5)
    
    print('Digite un numero y pulse enter hasta que la primera matriz este completa.\n')
    for i in range (5):
        for d in range(5):
            try:
                matriz[i][d]=int(input("Digite el elemento "+str(i+1)+":"+str(d+1)+">>> "))
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

    matriz1=[]
    for i in range(5):
        matriz1.append([0]*5)
    
    print('Digite un numero y pulse enter hasta que la segunda matriz este completa.\n')
    for i in range (5):
        for d in range(5):
            try:
                matriz1[i][d]=int(input("Digite el elemento "+str(i+1)+":"+str(d+1)+">>> "))
            except ValueError:
                print("!Error! debe ser numeros enteros vuelva a intentar\n")
                proceso()
                
    print("")            
    for i in matriz1:
        str_fila = ""
        for v in i:
            str_fila +="\t"+str(v)
        print(str_fila)    
        print("")

    for i in range(5):
        for d in range(5):
            if matriz[i][d] > mnp:
                mnp = matriz[i][d]
                may = matriz[i][d]
            if d == 4:
                mnp = -99**123
                prome = (prome + may ) // div
                div += 1
            if matriz1[i][d] > mnp1:
                mnp1 = matriz1[i][d]
                may1 = matriz1[i][d]
            if d == 4:
                mnp1=-99**123
                prome1 =(prome1 + may1) // div1
                div1 += 1
                
    if prome == prome1:
        print("El promedio entero de los números mayores de cada fila de las matrizes 'son iguales'\n")
    else:
        print("El promedio entero de los números mayores de cada fila de las matrizes 'no son iguales'\n")

    cont()
    
proceso()
