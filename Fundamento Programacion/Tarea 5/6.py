def cal():
    try:
        num =int(input("Digite un numero entero\n"))
    except:
        print(" Error! Debe ser un numero entero\n")
        cal()
    c = 1
    s = 0
    while c <= num:
        s += c
        c += 1
    print("La suma de 1 hasta el numero",num,'=',s)
    cont()
	
def cont():
    resp =input("Digite S para continuar o N para salir\n")
    if resp == 'S':
        cal()
    if resp == 'N':
        print("Good bye")
    else:
        print("!Error! deber ser S o N\n")
        cont()
cal()
