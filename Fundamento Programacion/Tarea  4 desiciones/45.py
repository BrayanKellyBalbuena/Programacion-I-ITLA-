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
     
   dig1 = num // 10
   dig2 = num % 10
   suma = dig1 + dig2  
   if num < 0:
      num *= -1
   if num % 2 == 0:
      print("La sumade los digitos es",suma,'\n')
   x = 0
   pri = 1
   while pri <= num:
      if num % pri == 0:
         x +=1
      pri += 1
   if num < 10 and x ==2:
       print('El ultio digito es',dig2,'\n')
   if num % 5 == 0 and num < 30:
      print("el primer digito es",dig1)
   cont()
   
def Errormuchosdig(num):
   if abs(num) <10 or abs(num) >99:
      return True
   else:
      return False
   
   
 
cal()  
  
 
