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
    if num < 0:
        num *= -1
    if num == 7:
        return "!el numero digitado es 7 por lo tanto es un solo digito y no comienza ni termina!" 
    elif num % 10 == 7:
        return "termina en 7 \n"
    else:
        return "no termina en 7\n"

cal()
