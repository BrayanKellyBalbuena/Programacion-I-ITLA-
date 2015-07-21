import os
import sys
import time
print(("Programa Almacena en un vector de 10 posiciones los 10 números primos comprendidos entre 100 y 300. Luego muestra en pantalla.\n"))
def clear():
    if os.name == "Posix":
        return os.system('clear')
    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        return os.system('cls')

def cont():
    resp = input("Digite S para continuar o N para salir\n")
    if resp == 'S':
        proceso()
    elif resp == 'N':
        c = int (5)
        while c != 0:
            time.sleep(1)
            clear()
            print("El programa se cirra en",c,"segundos !Good Bye!\n")
            c -= 1
            if c == 0:
                sys.exit(1)
    else:
        print("!Error debe ser S o N!\n")
        cont()

def proceso():
    vector=[]
    x,p,i,ind = 0,1,100,0       
    while i< 300 :
        x=0
        p=1
        while p < i:
            if i % p == 0:
                x +=1
            p+=1
        if x <= 2:
            vector.append(i)
            ind+=1
        if ind == 10:
            break
        
        i+=1
    print("Estos son los numeros primos entre 100 y 300\n")
    print (vector)
    
          
    cont()
    
proceso()
