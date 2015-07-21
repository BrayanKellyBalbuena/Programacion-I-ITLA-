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
#-----------------------------------------------   
   dig1 = num // 10
   dig2 = num % 10
   suma = dig1 + dig2   
   if num < 0:
      num *= -1
#----------------------------------------------      
   if dig2 == 1:
      print("el primer digito es",dig1,'\n')
   if dig2 == 2:
      print("La suma de los digitos es",suma,'\n')
   if dig2 == 3:
      print("El producto de los digitos es",dig1 *dig2,'\n')  
   cont()
def Errormuchosdig(num):
   if abs(num) <10 or abs(num) >99:
      return True
   else:
      return False
   
   
 
cal()  
  
 
