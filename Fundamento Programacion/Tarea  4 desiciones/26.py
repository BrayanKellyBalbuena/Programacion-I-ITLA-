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
   print("La suma de los digitos es :",Proce(num),'\n')
   cont()
      

def Errormuchosdig(num):
   
   if  abs(num) < 1000 or abs(num) > 9999:  
      return True
   else:
      return False

def Proce(num):
   m = num
   dig1 = m // 1000
   m %= 1000
   dig2 = m // 100
   m %=100
   dig3 = m // 10
   dig4 = m % 10
   resul = dig1 + dig2 + dig3 + dig4
   
   return resul
   
cal()
