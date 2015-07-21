def cont():
   m = input("Digite S para continuar o N para salir\n")
   if m == "S":
      cal()
   elif m == "N":
      print("Goog bye")
   else:
      print(" !Error !Debe ser S o N\n")
      cont()


def cal():
   try:
      num = int(input("Digite un numero entero menor que 20\n"))
      if num == 0:
          print ("Numero no valido")
          cal()
      if Errormuchosdig(num) == True:   
         print("!Error! Debe ser un numero entero menor que 20\n")
         cal()      
   except (ValueError):
     print("!Error! Debe ser un numero entero menor que 20 y mayor que 0\n")
     cal()
   print ("El numero",num,Proce(num))
   cont()
      

def Errormuchosdig(num):
   if num >20 :
      return True
   else:
      return False

def Proce(num): 
   num1 = num
   if num1 < 0:
      num1 *= int(-1)
   x =int(0)
   p =int(1)
   while p <= num1:
      if num1 % p == 0:
         x += int(1)
      p += 1
   if x > 2:
      pri = "no es primo\n"
      return pri
   else:
      pri = " es primo\n"
      return pri    

cal()
