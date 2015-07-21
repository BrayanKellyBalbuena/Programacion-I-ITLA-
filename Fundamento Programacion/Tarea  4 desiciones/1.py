def cont():
    m = input('Digite S para continuar o N para salir:\n')
    if m == 'S':
        cal()
    elif m == 'N':
        print("Good Bye")
    elif m != 'S':
        print("Debe ser S o N\n")
        cont()
    
def cal():
    try:
        num = int(input("Digite un numero entero:\n"))
    except ValueError:
        print("Es un numero.")
        input()
        cal()
    if num < 0:
       num *= -1	
    if (num % 10) == 4:
        print("Su ultimo digito es cuatro\n.")
        cont()
    else:
        print("Su ultimo digito no es cuatro\n.")
        print("")
        cont()
cal()


