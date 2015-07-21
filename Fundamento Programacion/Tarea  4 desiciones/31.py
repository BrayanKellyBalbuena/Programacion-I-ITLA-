def cont():
    m = input("Digite S para continuar o N para salir\n")
    if m == "S":
       cal()
    elif m == "N":
       print("Goog bye")
       print('')
    else:
       print(" !Error !Debe ser S o N\n")
       cont()

def cal():
    try:
        num = int(input("Digite un numero entero\n"))
    except ValueError:
        print("!Debe ser un numero entero!\n")
        cal()
    print("El numero",num,proce(num))
    cont()

def proce(num):
    if num == 10:
        return "es igual a 10\n"
    else:
        return "no es igual a 10\n"

cal()    
