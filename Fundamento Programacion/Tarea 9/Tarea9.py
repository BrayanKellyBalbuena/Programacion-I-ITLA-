
import os
import sqlite3
import sys
import time

print('Programa guarda datos de vehiculos inserta,modificar,eliminar y exportar los vehiculos.\n')



print("La base de datos de abrio correctamente")

def insertar():
    os.system('cls')
    info = input("\nDigite la informacion\n>>> ")
    marca = input("Digite la marca\n>>> ")
    modelo = input("Digite el modelo\n>>> ")
    try:
         año = int(input("Digite el año\n>>> "))
    except:
        print("Año no Valido intente nuevo\n")
        try:
            año = int(input("Digite el año\n>>> "))
        except:
            print("Año no Valido intente nuevo\n")
            año = int(input("Digite el año\n>>> "))
    color = input("Digite el color\n>>> ")
    matricula = input("Digite la matricula\n>>> ")
    try:
         valor = float(input("Digite el valor\n>>> $"))
    except:
        print("Valor no Valido intente nuevo\n")
        try:
            valor = float(input("Digite el valor\n>>> $"))
        except:
            print("Valor no Valido intente nuevo\n")
            valor = float(input("Digite el valor\n>>> $"))
    try:
        puertas = int(input("Digite el numero de puertas\n>>> "))
    except:
        print("Numero no no Valido intente nuevo\n")
        try:
            puertas = float(input("Digite el numero de puertas\n>>> "))
        except:
            print("Numero ni valido intente nuevo\n")
            puertas = float(input("Digite el numero de puertas\n>>> "))
    try:
         km = int(input("Digite el numero de klometros\n>>> "))
    except:
        print(" no Valido intente nuevo\n")
        try:
            km = int(input("Digite el numero de kilometraje\n>>> "))
        except:
            print("no Valido intente nuevo\n")
            km = int(input("Digite el numero de kilometraje\n>>> "))
    con =sqlite3.connect("Tarea9 -.s3db")
    cursor = con.cursor()        
    cursor.execute("INSERT INTO  Carros(Informacion,Marca,Modelo,Ano,Color,Matricula,Valor,Puertas,Kilometraje) VALUES ('"+info+"','"+marca+"','"+modelo+"','"+str(año)+"','"+color+"','"+matricula+"','"+str(valor)+"','"+str(puertas)+"','"+str(km)+"')")
    con.commit()
    con.close
    menu()

def modificar():
    print()

def ver():
    con = sqlite3.connect("Tarea9 -.s3db")
    cursor = con.cursor()
    cursor = execute("SELECT * FROM Carros")
    print("Por favor maximice su ventana para ver los resultados completos\n")
    print("Carros Agregados ")
    print("\t Marca    \t    Modelo    \t    Año    \t    Color    \t    Matricula      \t     Valor    \t    Puertas    \t    Kilometraje    \t    informacion")
    print("--"*83)
    for ind in cursor:
        car ="\t "+ind[1]+"    \t    "+ind[2]+"    \t    "+str(ind[3])+"    \t    "+ind[4]+"    \t    "+ind[5]+"      \t     "+str(ind[6])+"    \t    "+str(ind[7])+"    \t    "+str(ind[8])+"    \t    "+ind[0]+"
    
    print()
    
def eliminar():
    print()
    
def exportar():
    print()
    
    
def menu():
    print("1-Insertar\n2-Modificar\n3-Ver\n4-Eliminar\n5-Exportar a html\n6-salir")
    resp =input("\nDigite su opción\n>>>  ")
    
    if resp == '1':
        insertar()
    elif resp == '2':
        modificar()
    elif resp == '3':
        ver()
    elif resp == '4':
        eliminar()   
    elif resp == '5':
        exportar()
    elif resp == '6':
        c = 5
        while c !=5:
            time.sleep(1)
            clear()
            print("El programa se cirra en",c,"segundos !Good Bye!\n")
            c-=1
            if c == 0:
                sys.exit(1)
    else:
        print()
    

menu()
    
