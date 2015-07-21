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
   except ValueError:
      print("!Error! Debe ser tres numeros enteros\n")
      cal()
	  
   if num > num1 and num > num2:
      if num1 > num2:
         print(num2,'',num1,'',num)
         cont()		 
      else:
         print(num1,'',num2,'',num)
         cont()
   elif num1 > num and num1 > num2:
      if num > num2:
         print(num2,'',num,'',num1)
         cont()
      else:
         print(num,'',num2,'',num1)
         cont()
   elif num2 > num and num2 > num1:
      if num > num1:
         print(num1,'',num,'',num2)
         cont()
      else:
         print(num,'',num1,'',num2)
         cont()		 
   else:
      print("Todos son iguales no hay orden descendente") 
	  
cal()
