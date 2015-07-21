def cal():
   
    c = 25
    while c <= 205:
        if c % 10 == 6:
            print(c)
        c += 1
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
