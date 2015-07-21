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
   m = num 
   dig1 = m // 100
   m %= 100
   dig2 = m // 10
   dig3 = m % 10
   if dig1 == dig2 and dig1 ==dig3:
      return "Los numeros son iguales y van hacer multiplos entres si"
   elif(dig2 % dig1 == 0 ) and (dig3 %dig1 == 0):
      return "El segundo digito y el ultimo son multiplos del primero"
   elif(dig1 % dig2 == 0) and (dig3 % dig2 == 0):
      return "El primer digito y el ultimo son multiplos del segundo"
   elif(dig1 % dig3 == 0) and (dig2 % dig3 == 0):
      return "El primer digito y el segundo son multiplos del ultimo"
   elif	dig2 % dig1 == 0:
      return "El segundo digito es multiplo del primero"
   elif dig3 % dig1 == 0:
      return "El ultimo digito es multiplo del primero"
   elif dig1 % dig2 == 0:
      return "El primer digito es multiplo del segundo"
   elif dig3 % dig2 == 0:
      return "El ultimo digito es multiplo del segundo"	
   elif dig1 % dig3 == 0:
      return "El primer digito es multiplo del tercero"
   elif dig2 % dig3 == 0:
      return "El segundo digito es multiplo del tercero"
   else:
      return "Ninguno de los digitos es multiplo del otro"
	  
   
	  
cal()   