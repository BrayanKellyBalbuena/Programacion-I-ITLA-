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
      num = int(input("Digite un numero entero de dos digitos\n"))
      if num == 0:
          print ("Numero no valido\n")
          cal()
      if Errormuchosdig(num) == True:   
         print("!Error! Deb ser un numero entero de dos digitos\n")
         cal()      
   except (ValueError):
     print("!Error! Debe ser un numero entero de dos digitos\n")
     cal()
   print (Proce(num))
   cont()
      

def Errormuchosdig(num):
   if  abs(num) < 10 or abs(num) > 99:  
      return True
   else:
      return False

def Proce(num):
   if num < 0 : 
      num1 = num * (-1)
   num1 = num
   x =int(0)
   p =int(1)
   while p <= num1:
      if num1 % p == 0:
         x += int(1)
      p += 1
   if x > 2 and num < 0:
      pri = "no es primo pero es negativo"
      return pri
   elif x == 2 and num < 0:
      pri = " es primo y  es positivo"
      return pri
   elif x > 2 and num > 0:
      pri = " es primo pero es positivo"
      return pri
   else:
      pri = " es primo pero es negativo"
      return pri
      
cal()
