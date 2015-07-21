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
         print("!Error! Deb ser un numero entero de dos digitos \n")
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
      num *= -1    
   dig1 = num // 10
   dig2 = num % 10
   x =int(0)
   p =int(1)
   p1 = int(1)
   x1 = int(0)
   while p <= dig1:
      if dig1 % p == 0:
         x += int(1)
      p += 1
   while p1 <= dig2:
       if dig2 % p1 == 0:
          x1 += int(1)
       p1 += 1		  
   if x == 2 and x1 == 2:
      lop ="Los dos son primos\n"
      return lop
   elif	x == 2 or x1 == 2:
      lop ="Solo uno es primo\n"   
      return lop
   else:
      lop = "Ninguno es primo\n"
      return lop    

cal()
