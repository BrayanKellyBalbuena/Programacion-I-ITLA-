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
   print("La suma de los digitos es: ",Proce(num),"\n")
   cont()
   
def Proce(num):
   if num < 0:
      num *= -1
   dig1 = num // 10
   dig2 = num % 10
   suma = dig1 + dig2
   return suma
	 
def Errormuchosdig(num):
   if abs(num) <10 or abs(num) >99:
      return True
   else:
      return False
   
   
 
cal()  
  
 
