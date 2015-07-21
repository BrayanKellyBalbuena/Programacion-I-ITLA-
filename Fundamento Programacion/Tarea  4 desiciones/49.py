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
      num = int(input("Digite un numero entero\n"))
      if num == 0:
         print ("Numero no valido\n")
         cal()  
   except (ValueError):
       print("!Error! Deben ser un numero entero \n")
       cal()

   if num < 0:
      num *= -1
   ud = num % 10 
   if num % 4 == 0:
      pri = 1
      x = 0
      while pri <= ud:
         if ud % pri == 0:
             x += 1
             pri += 1
      if x == 2:
         print("El ultimo digito es primo")
         cont()
      else:
         print("El ultimo digito no es primo")
         cont()
cal()
