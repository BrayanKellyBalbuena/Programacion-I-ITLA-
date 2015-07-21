#importamos las librerias
import os
import sys
import time


print(' Programa Lee dos matriz 4x6 entera y determina si el promedio de las “esquinas” de una matriz es igual al promedio de las “esquinas” de la otra matriz.')
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
    prome,prome1 = 0,0
    matriz=[]
    for i in range(4):
        matriz.append([0]*6)
    
    print('Digite un numero y pulse enter hasta que la primera matriz este completa.\n')
    for i in range (4):
        for d in range(6):
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
    for i in range(4):
        matriz1.append([0]*6)
    
    print('Digite un numero y pulse enter hasta que la segunda matriz este completa.\n')
    for i in range (4):
        for d in range(6):
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
        
    prome = (matriz[0][0] + matriz[0][5] + matriz[3][0] + matriz[3][5]) // 4
    prome1 = (matriz1[0][0] + matriz1[0][5] + matriz1[3][0] + matriz1[3][5]) // 4        
            
    if prome == prome1:
        print("El promedio de las “esquinas” de una matriz es igual al promedio de las “esquinas” de la otra matriz.\n")
    else:
        print("el promedio de las “esquinas” de una matriz no es igual al promedio de las “esquinas” de la otra matriz.\n")

    cont()
    
proceso()
