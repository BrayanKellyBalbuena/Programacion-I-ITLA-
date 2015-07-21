
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
      num = int(input("Digite el primer numero entero \n"))
      num1 =int(input("Digite el segundo numero entero\n"))
      num2 =int(input("Digite el segundo numero entero\n"))
      if num == 0:
          print ("Numero no valido\n")
          cal()
      if num1 == 0:
          print ("Numero no valido\n")
          cal()
      if num2 == 0:
          print ("Numero no valido\n")
          cal()
      if Errormuchosdig(num,num1,num2) == True:
          print("!Error! Deben ser dos numeros enteros de dos digitos\n")
          cal()      
   except (ValueError):
     print("!Error! Debe ser dos numeros enteros de dos digitos\n")
     cal()

   d1n = num // 10
   d2n = num % 10
   d1n1 = num1 // 10
   d2n1 = num1 % 10
   d1n2 = num2 // 10
   d2n2 = num2 % 10
   if d1n == d2n and d2n ==d1n1 and d1n1 == d2n1 and d2n1 == d1n2 and  d1n2 == d2n2:
      print("Todos los digitos son iguales no se puede proceder\n")
      cont()
   elif(d1n > d2n and d1n > d1n1) and (d1n > d2n1 and d1n > d1n2) and (d1n > d2n2):
      print("El mayor digito se encuentra en",num,"en la primera posicion\n")
      cont()
   elif (d2n > d1n and d2n > d1n1) and (d2n > d2n1 and d2n > d1n2) and (d2n > d2n2):
      print("El mayor digito se encuentra en",num,"en la segunda posicion\n")
      cont()
   elif (d1n1 > d1n and d1n1 > d2n) and (d1n1 > d2n1 and d1n1 > d1n2) and (d1n1 > d2n2):
      print("El mayor digito se encuentra en",num1,"en la primera posicion\n")
      cont()
   elif (d2n1 > d1n and d2n1 > d2n) and (d2n1 > d1n1 and d2n1 > d1n2) and (d2n1 > d2n2):
      print("El mayor digito se encuentra en",num1,"en la segunda posicion\n")
      cont()
   elif (d1n2 > d1n and d1n2 > d2n) and (d1n2 > d1n1 and d1n2 > d2n1) and (d1n2 > d2n2):
      print("El mayor digito se encuentra en",num2,"en la primera posicion\n")
      cont()
   elif (d2n2 > d1n and d2n2 > d2n) and (d2n2 > d1n1 and d2n2 > d2n1) and (d2n2 > d1n2):
      print("El mayor digito se encuentra en",num2,"en la segunda  posicion\n")
      cont()
   else:
      print("Los numeros ",num,'',num1,'',num2,'Hay numeros que tienen digitos iguales y no se puede proceder\n')
      cont()
            
def Errormuchosdig(num,num1,num2):
   if  (abs(num) < 10 or abs(num) > 99) or (abs(num1) < 10 or abs(num1) > 99) or (abs(num2) < 10 or abs(num2) > 99): 
      return True
   else:
      return False

cal()                                                                                  
