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

   if num < 100:
       x = 0
       pri = 1
       while pri <= num:
           if num % pri == 0:
               x += 1
           pri += 1    
   else:
       print(num,"no es menor que 100 por lo tanto no se puede proceder")
cal()
