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
      if Errormuchosdig(num) == True:
         print("!Error! Debe ser un numero entero de dos digitos\n")
         cal()      
   except (ValueError):
       print("!Error! Debe ser un numero entero de dos digitos\n")
       cal()
   if Proce(num) == 0:
       print("El numero ",num,"tiene dos numeros pares\n")
   elif Proce(num) == 1:
       print("El numero ",num,"tiene solo un numero par\n")
   else:
       print("El numero ",num,"no tiene un numero par\n")    
   cont()
   
def Proce(num):
   if num < 0:
     num *= -1 
   dig1 = num // 10
   dig2 = num % 10
   if dig1 % 2 == 0 and dig2 % 2 == 0:
       rep = 0
       return rep
   elif dig1 % 2 == 0 or dig2 % 2 == 0:
       rep = 1
       return rep
   
def Errormuchosdig(num):
   if abs(num) <10 or abs(num) >99:
      return True
   else:
      return False
   
   
 
cal()  
  
