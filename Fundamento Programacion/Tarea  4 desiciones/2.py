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
      num = int(input("Digite un numero que desea comprobar si tienes 3 digitos\n"))
   except ValueError:
      print("Debe ser un numero\n")
      cal()
   if num < 0:
      num *= -1   
   c = int(1) 
   m = int(num)
   ct = int(10) 
   while ct <= m:
      m = m / ct 
      c = c + 1
      
   if c == 3:
      print("El numero",num,"tiene  tres dig\n")
      cont()
   elif c > 3:
      print("El numero",num,"tiene mas de tres dig\n")
      cont()
   else:
      print("El numero",num,"tiene menos de tres dig\n")
      cont()
   	  
cal()   

