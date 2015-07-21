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
      num = int(input("Digite un numero entero menor que 1000\n"))
      if num == 0:
          print ("Numero no valido\n")
          cal()
      if Errormuchosdig(num) == True:   
         print("!Error! Deb ser un numero entero menor que 1000\n")
         cal()      
   except (ValueError):
     print("!Error! Debe ser un numero entero menor que 1000\n")
     cal()
   print("En el numero",num,Proce(num),'\n')
   cont()
      

def Errormuchosdig(num):
   if  abs(num) > 1000:  
      return True
   else:
      return False

def Proce(num):
   if num <0:
      num *= -1 
   if num > 0 and num < 10:
       return "tiene 1 solo digito"
   elif num >= 10 and num < 100:
       return "tiene 2 solo digitos"
   else:
       return "tiene 3 digitos"
  


cal()
