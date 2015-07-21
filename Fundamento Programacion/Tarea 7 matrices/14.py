#importamos las librerias
import os
import sys
import time


print(' Programa Lee dos matriz 4x5 entera y determina si si la cantidad de números primos almacenados en una matriz es igual a la cantidad de números primos almacenados en la otra matriz.')
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
    may_m,may_m1,c,c1=-99**99,-99**99,0,0
    matriz=[]
    for i in range(4):
        matriz.append([0]*5)
    
    print('Digite un numero y pulse enter hasta que la primera matriz este completa.\n')
    for i in range (4):
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
    for i in range(4):
        matriz1.append([0]*5)
    
    print('Digite un numero y pulse enter hasta que la segunda matriz este completa.\n')
    for i in range (4):
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
        
    for i in range(4):
        for d in range (5):
            p,p1,x,x1 = 1,1,0,0
            while p <= matriz[i][d]:
                if matriz[i][d] % p == 0:
                    x += 1
                p += 1
                
            while p1 <= matriz1[i][d]:
                if matriz1[i][d] % p1 == 0:
                    x1 += 1
                p1 += 1
                
            if x == 2:
                c += 1
               
            if x1 == 2:
                c1 +=1
             
                
    if c == c1:
        print("La cantidad de numeros primos en las matrices son guales\n")
        cont()
    else:
        print("La cantidad de numeros primos en las matrices no son guales\n")
        cont()
proceso()
