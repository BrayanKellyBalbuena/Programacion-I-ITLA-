def cont():
   m = input("Digite S para continuar o N para salir\n")
   if m == "S":
      cal()
   elif m == "N":
      print("Goog bye")
      print('')
   else:
      print(" !Error !Debe ser S o N\n")
      cont()


def cal():
   try:
      num = int(input("Digite un numero entero de cuatro digitos\n"))
      if num == 0:
          print ("Numero no valido\n")
          cal()
      if Errormuchosdig(num) == True:   
         print("!Error! Deb ser un numero entero de cuatro digitos \n")
         cal()      
   except (ValueError):
     print("!Error! Debe ser un numero entero de cuatro digitos\n")
     cal()
   print("En el numero ",num,Proce(num),'\n')
   cont()
      

def Errormuchosdig(num):
   if  abs(num) < 1000 or abs(num) > 9999:  
      return True
   else:
      return False

def Proce(num):
   if num <0:
      num *= -1 
   m = num
   dig1 = m // 1000
   m %= 1000
   dig2 = m // 100
   m %=100
   dig3 = m // 10
   dig4 = m % 10
   x = 0
   y = 0
   if dig1 % 2 == 0:
       x += int(1)
   else:
       y += int(1) 
   if dig2 % 2 == 0:
       x += int(1)
   else:
       y += int(1)
   if dig3 % 2 == 0:
       x += int(1)   
   else:
       y += int(1)
   if dig4 % 2 == 0:
       x += int(1)
   else:
       y += int(1)
      
   if x > y:
        return "hay mas digitos pares que impares" 
   if x < y:
       return "hay mas digitos impares que pares"
   if x == y:
       return "hay igual cantidad de  digitos pares  que impares"
       
cal()      
