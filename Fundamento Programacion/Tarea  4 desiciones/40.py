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
      num = int(input("Digite el primer numero entero\n"))
      num1 =int(input("Digite el segundo numero entero \n"))
      if num == 0:
         cal
         print ("Numero no valido\n")
      if num1 == 0:
         print ("Numero no valido\n")
         cal()  
   except (ValueError):
       print("!Error! Deben ser dos numeros enteros \n")
       cal()
       
   if num - num1 <= 10:
      c = num1 
      print("Estos son los numeros comprendidos entre",num,"que es el mayor y ",num1, "que es el menor:\n") 
      while c < (num-1):
         c += 1
         print(c)
   elif num1 - num <= 10 and num1 - num > 0:
       c = num 
       print("Estos son los numeros comprendidos entre",num1,"que es el mayor y ",num, "que es el menor:\n") 
       while c < (num1-1):
          c += 1
          print(c)
   else:
       print("Estos numeros no proceden")

cal()          
