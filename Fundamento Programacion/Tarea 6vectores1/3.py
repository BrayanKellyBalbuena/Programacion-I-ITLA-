import os
import sys
import time
print(("Programa lee 10 enteros, almacena en un vector y determina en qué posición del vector está el mayor número primo leído.\n"))
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
    print("Digite un numero y pulse enter hasta que sean 10 numeros enteros\n")
    for ind in range(10):
        try:
            vector.insert(ind,int(input('>>> ')))
        except ValueError:
            print("!Error debe ser numeros enteros vuelva a intentar\n!")
            proceso()
    mp,pos_may = 0,0        
    for ind in range (1,10):
        x,c,p=0,1,0
        while c <= vector[pos_may]:
            if vector[pos_may] % c == 0:
                x +=1
                mp=pos_may+1
            c+=1
        c=1    
        while c <= vector[ind]:
            if vector[ind] % c==0:
                p=p+1
            c+=1    
        if (x != 2) and (p == 2):
            mp=ind+1
            pos_may=ind
        if (x == 2) and (p == 2)and(vector[ind]> vector[pos_may]):
            pos_may=ind
            mp=pos_may+1
                    
    print("El mayor numero primo se encuentra en la posicion",mp,'\n')
    cont()
    
proceso()
