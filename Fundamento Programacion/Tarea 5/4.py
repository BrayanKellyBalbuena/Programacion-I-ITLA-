def cal():
    c = 1
    while c <= 100:
        if c % 2 == 0:
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
