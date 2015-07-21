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
      num = int(input("Digite el primer numero entero de dos digitos\n"))
      num1 =int(input("Digite el segundo numero entero de dos digitos\n"))
      if num == 0:
         cal
         print ("Numero no valido\n")
      if num1 == 0:
         print ("Numero no valido\n")
         cal()
      if Errormuchosdig(num,num1) == True:   
         print("!Error! Deben ser dos numeros enteros de dos digitos\n")
         cal()      
   except (ValueError):
     print("!Error! Deben ser dos numeros enteros de dos digitos\n")
     cal()
   if num < 0:
      num *= -1
   if num1 < 0:
      num1 *= -1  
   dig1n = num // 10
   dig2n = num % 10
   dig1n1 = num1 // 10
   dig2n1 = num1 % 10
   if (dig1n == dig1n1 or dig1n == dig2n1 ) or (dig2n == dig1n1 or dig2n == dig2n1):
       print("Tienen digitos comunes\n")
       cont()
   else:
      print("no tienen digitos comunes\n")
      cont()
      

def Errormuchosdig(num,num1):
   
   if  (abs(num) < 10 or abs(num) > 99) or (abs(num1) < 10 or abs(num1) > 99):  
      return True
   else:
      return False
   
cal()
