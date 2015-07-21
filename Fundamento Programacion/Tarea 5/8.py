def cal():
    try:
        num =int(input("Digite un numero entero\n"))
    except:
        print(" Error! Debe ser un numero entero\n")
        cal()
    
    if num < 0:
        num *= -1
    c = 1
    cn = num	
    while cn > 9:
        cn /= 10
        c +=1
    print("El numero",num,"tiene",c,"digitos\n")
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
