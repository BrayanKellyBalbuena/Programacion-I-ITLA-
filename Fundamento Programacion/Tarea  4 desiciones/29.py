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
      num = int(input("Digite un numero entero de cinco digitos\n"))
      if num == 0:
          print ("Numero no valido\n")
          cal()
      if Errormuchosdig(num) == True:   
         print("!Error! Deb ser un numero entero de cinco digitos \n")
         cal()      
   except (ValueError):
     print("!Error! Debe ser un numero entero de cinco digitos\n")
     cal()
   print("El numero ",num,Proce(num),'\n')
   cont()
      

def Errormuchosdig(num):
   if  abs(num) < 10000 or abs(num) > 99999:  
      return True
   else:
      return False

def Proce(num):
   if num <0:
      num *= -1 
   m = num
   dig1 = m // 10000
   m %= 10000
   dig2 = m // 1000
   m %=1000
   dig3= m // 100
   m %= 100
   dig4 = m // 10
   dig5 = m % 10
    
   if dig1 == dig5 and dig2 == dig4:
        return "es capicuo"
   else:
       return " no es capicuo"
       
cal()      
