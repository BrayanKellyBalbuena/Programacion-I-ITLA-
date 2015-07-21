m=["&"]
c =[]
def a():
    global m
    b=(input("/n>>>"))
    r = len(m)
    for i in range(0,r):
        print(r)
        print(b)
        if b == m[i]:
            print("Esta repetido")
            print("Intente dde nuevo")
            a()
        
    else:
        print(m)
        m.append(b)
        a()
   
a()
