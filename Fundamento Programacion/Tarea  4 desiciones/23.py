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
      num = int(input("Digite un numero entero de tres digitos\n"))
      if num == 0:
          print ("Numero no valido\n")
          cal()
      if Errormuchosdig(num) == True:   
         print("!Error! Deb ser un numero entero de tres digitos \n")
         cal()      
   except (ValueError):
     print("!Error! Debe ser un numero entero de tres digitos\n")
     cal()
   print(Proce(num),'\n')
   cont()
      

def Errormuchosdig(num):
   if  abs(num) < 100 or abs(num) > 999:  
      return True
   else:
      return False
    
def Proce(num):
   if num < 0:
      num *= -1
   x = 0  
   p = 1  
   m = num 
   dig1 = m // 100
   m %= 100
   dig2 = m // 10
   dig3 = m % 10
   while p <= dig1:
      if dig1 % p == 0:
         x += int(1)
      p += 1
      
   p = 1
   while p <= dig2:
      if dig2 % p == 0:
         x += int(1)
      p += 1
      
   p = 1   
   while p <= dig3:
      if dig3 % p == 0:
         x += int(1)
      p += 1
      
   if x == 2 or x == 10 :
        return "Solo hay un  digito primo"
   elif x == 4 :
       return "Solo hay dos digitos primos"
   elif x == 5 or x == 6:
       return "Los  tres digitos primos son primos"
   elif x == 7:
       return "Solo hay dos digitos primos"
   elif x == 8:
       return "Solo hay un  digito primo"
   else:
       return "Ninguno de los digitos son primos"
       

cal()
