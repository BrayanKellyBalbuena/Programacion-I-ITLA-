#importamos las librerias
import os
import sys
import time


print(' Programa Lee dos matriz 4x5 entera y determina cuántos datos tienen en común\n')
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
    b,sw,bw=0,0,0
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
            for f in range(4):
                for c in range(5):
                    if matriz[i][d]==matriz1[f][c]:
                        b+=1
                        bw = sw
                        sw += 1
                        break
                
    if b ==0 :
        print("Las matrizes no tienen datos en comun\n")
        cont()
    else:
        print("Las matrizes tienen",b,"datos en comun\n")
        
proceso()
