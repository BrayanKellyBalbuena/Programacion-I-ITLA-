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
   print('En el numero ',num ,Proce(num),'\n')
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
   m = num
   dig1 = m // 100
   m %= 100
   dig2 = m // 10
   dig3 = m % 10
   if dig1 + dig2 == dig3:
       return("la suma del primer digito y el segundo es igual al tercero")
   elif dig1 + dig3 == dig2:
       return("la suma del primer digito y el tercero es igual al segundo")  
   elif dig2 + dig3 == dig1:
       return("la suma del segundo digito y el tercero es igual al primero")
   else:
       return("la suma de los digitos entre ellos no es igual a ninguno de ellos")
          

cal()
