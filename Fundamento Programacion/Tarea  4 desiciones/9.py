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
   if num < 0:
      num *= -1
   dig1 = num // 10
   dig2 = num % 10
   if dig1 % dig2 == 0:
      resu = "El primer numero es multiplo del ultimo\n"
      return resu
   elif dig2 % dig1 == 0:
      resu = "El ultimo numero es multiplo del primer\n"
      return resu
   else:
      resu = "Ninguno de los numeros  es multiplo del otro\n"
      return resu
         
   	  
cal()
