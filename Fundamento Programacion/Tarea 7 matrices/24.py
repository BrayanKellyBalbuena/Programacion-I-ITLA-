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
    promec,promec1 = 0,0
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
            p,x,p1,x1=1,0,1,0
            while p < abs (matriz[i][d]):
                x += 1
                p += 1
            if x == 2:
                if matriz[i][d] > mnp:
                    mnp = matriz[i][d]
                    may = matriz[i][d]
                if d == 4:
                    mnp = -99**123
                    promec = (promec + may ) // div
                    div += 1
            p,x,p1,x1=1,0,1,0        
            while p1 < abs(matriz1[i][d]):
                x1 +=1
                p1 +=1
            if x1 == 2:
                if matriz1[i][d] > mnp1:
                    mnp1 = matriz1[i][d]
                    may1 = matriz1[i][d]    
                if d == 4:
                    mnp1=-99**123
                    promec1 =(promec1 + may1) // div1
                    div1 += 1
                    
    mnp,mnp1,may,may1,div,div1 = -99**123,-99**123,0,0,1,1              
    p,x =1,0
    for i in range (5):
        for d in range (1):
            while p < abs(matriz[i][d]):
                x +=1
                p +=1
            if x == 2:
                if matriz[i][d] > mnp:
                    mnp=matriz[i][d]
                    may =matriz[i][d]
                if d == 0:
                    mnp = -99**123
                    promec = (promec + may)//div
                    div += 1
            p,x =1,0        
            while  p < abs(matriz1[i][d]):
                x +=1
                p +=1
            if x == 2:
                if matriz1[i][d] > mnp1:
                    mnp1=matriz1[i][d]
                    may1=matriz1[i][d]
                if d == 0:
                    mnp1 = -99**123
                    promec1 = (promec1 + may1)//div1
                    div1 += 1
                    
    mnp,mnp1,may,may1,div,div1 = -99**123,-99**123,0,0,1,1              
    p,x =1,0
    for i in range (5):
        for d in range (1,2):
            while p < abs(matriz[i][d]):
                x +=1
                p +=1
            if x == 2:
                if matriz[i][d] > mnp:
                    mnp=matriz[i][d]
                    may =matriz[i][d]
                if d == 1:
                    mnp = -99**123
                    promec = (promec + may)//div
                    div += 1
            p,x =1,0        
            while  p < abs(matriz1[i][d]):
                x +=1
                p +=1
            if x == 2:
                if matriz1[i][d] > mnp1:
                    mnp1=matriz1[i][d]
                    may1=matriz1[i][d]
                if d == 1:
                    mnp1 = -99**123
                    promec1 = (promec1 + may1)//div1
                    div1 += 1

    mnp,mnp1,may,may1,div,div1 = -99**123,-99**123,0,0,1,1              
    p,x =1,0
    for i in range (5):
        for d in range (2,3):
            while p < abs(matriz[i][d]):
                x +=1
                p +=1
            if x == 2:
                if matriz[i][d] > mnp:
                    mnp=matriz[i][d]
                    may =matriz[i][d]
                if d == 2:
                    mnp = -99**123
                    promec = (promec + may)//div
                    div += 1
            p,x =1,0        
            while  p < abs(matriz1[i][d]):
                x +=1
                p +=1
            if x == 2:
                if matriz1[i][d] > mnp1:
                    mnp1=matriz1[i][d]
                    may1=matriz1[i][d]
                if d == 2:
                    mnp1 = -99**123
                    promec1 = (promec1 + may1)//div1
                    div1 += 1 

    mnp,mnp1,may,may1,div,div1 = -99**123,-99**123,0,0,1,1              
    p,x =1,0
    for i in range (5):
        for d in range (3,4):
            while p < abs(matriz[i][d]):
                x +=1
                p +=1
            if x == 2:
                if matriz[i][d] > mnp:
                    mnp=matriz[i][d]
                    may =matriz[i][d]
                if d == 3:
                    mnp = -99**123
                    promec = (promec + may)//div
                    div += 1
            p,x =1,0        
            while  p < abs(matriz1[i][d]):
                x +=1
                p +=1
            if x == 2:
                if matriz1[i][d] > mnp1:
                    mnp1=matriz1[i][d]
                    may1=matriz1[i][d]
                if d == 3:
                    mnp1 = -99**123
                    promec1 = (promec1 + may1)//div1
                    div1 += 1                 

    mnp,mnp1,may,may1,div,div1 = -99**123,-99**123,0,0,1,1              
    p,x =1,0
    for i in range (5):
        for d in range (4,5):
            while p < abs(matriz[i][d]):
                x +=1
                p +=1
            if x == 2:
                if matriz[i][d] > mnp:
                    mnp=matriz[i][d]
                    may =matriz[i][d]
                if d == 4:
                    mnp = -99**123
                    promec = (promec + may)//div
                    div += 1
            p,x =1,0        
            while  p < abs(matriz1[i][d]):
                x +=1
                p +=1
            if x == 2:
                if matriz1[i][d] > mnp1:
                    mnp1=matriz1[i][d]
                    may1=matriz1[i][d]
                if d == 4:
                    mnp1 = -99**123
                    promec1 = (promec1 + may1)//div1
                    div1 += 1 
              
    if prome == promec1:
        print("El promedio entero de los números primos mayores  de cada fila de la matriz 1 'es igual' al promedio de los números primos mayores  de cada columna de la matriz 2\n")
    else:
        print("El promedio entero de los números primos mayores  de cada fila de la matriz 1 'no es igual' al promedio de los números primos mayores  de cada columna de la matriz 2\n")
    if prome1 == promec:
        print("El promedio entero de los números primos mayores  de cada fila de la matriz 2 'es igual' al promedio de los números primos mayores  de cada columna de la matriz 1\n")
    else:
        print("El promedio entero de los números primos mayores  de cada fila de la matriz 2 'no es igual' al promedio de los números primos mayores  de cada columna de la matriz 1\n")
    cont()
    
proceso()
