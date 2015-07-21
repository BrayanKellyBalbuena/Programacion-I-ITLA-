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
   except ValueError:
      print("!Error! Debe ser dos numeros enteros\n")
      cal() 
   if num > num1 or num == num1:
      try:
         num1 = int(input("Digite el otro numero"))
      except ValueError:
         print("!Error! Debe ser un numero entero\n")
         cal()
      if num == num1:
         print("Los tres digitos son iguales")
         cont()
      elif num > num1:
         print("El primer numero que es:",num,"Es el mayor de los tres numeros\n")
         cont()
      else:
         print("El tercer numero que es:",num1,"Es el mayor de los tres numeros\n")
         cont()		   
   elif num1 > num:
      try:
         num = int(input("Digite el otro numero"))
      except ValueError:
         print("!Error! Debe ser un numero entero\n")
      if num1 > num:
         print("El segundo numero que es:",num1,"Es el mayor de los tres numeros\n")
         cont()
      else:
         print("El tercer numero que es:",num,"Es el mayor de los tres numeros\n")
         cont()	
   else:
      print("Los numeros son iguales, por tanto ninguno es mayor que el otro")
      cont()
   
      
cal()
