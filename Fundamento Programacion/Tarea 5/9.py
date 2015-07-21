def cal():
    try:
        num =int(input("Digite un numero entero\n"))
    except:
        print(" Error! Debe ser un numero entero\n")
        cal()
    if num < 0:
        num *= -1
    c = 1
    co = 0	
    while c < num:
        if num % c == 0:
            co += c
        c +=1
    if num < co:
        print("El numero",num,"es abundante\n")
        cont()
    else:
        print("El numero" ,num," no es abundante\n")
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
