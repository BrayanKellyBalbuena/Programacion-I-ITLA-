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
         print("!Error! Debe ser un numero entero de dos digitos\n")
         cal()      
   except (ValueError):
     print("!Error! Debe ser un numero entero de dos digitos\n")
     cal()
   if Proce(num) == 0:
      print("Los dos digitos son iguales\n")
      cont()	  
   else:
      print("El digito ",Proce(num),"es mayor que el otro\n")
      cont()
      

def Errormuchosdig(num):
   
   if  abs(num) < 10 or abs(num) > 99:  
      return True
   else:
      return False

def Proce(num):
   if num < 0:
      num *= -1
   dig1 = num // 10
   dig2 = num % 10
   if dig1 < dig2 :
      return dig2
   elif dig2 < dig1:
      return dig1
   else:
      return 0
         
   	  
cal()
