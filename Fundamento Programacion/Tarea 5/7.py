def cal():
    try:
        num =int(input("Digite un numero entero\n"))
    except:
        print(" Error! Debe ser un numero entero\n")
        cal()
    p = 1
    x = 0
    if num < 0:
        num *= -1
    while p <= num:
        if num % p == 0:
            x += 1
        p += 1
    if x > 2:		
        print("El numero",num,"no es primo\n")
        cont()
    if x == 2:
        print("El numero" ,num,"es primo")
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
