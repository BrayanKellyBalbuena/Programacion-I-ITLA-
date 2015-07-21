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
       
   if num > num1:
       xnum = num - num1
       if num % xnum == 0 or  num1 % xnum == 0:
           print("La diferencia entre",num,"que es el mayor y ",num1, "que es el menor  oriniga divisor exacto de alguno de los numeros\n") 
       else: 
           print("La diferencia entre",num,"que es el mayor y ",num1, "que es el menor no oriniga divisor exacto de alguno de los numeros\n") 
   if num1 > num:
       xnum = num1 - num
       if num1 % xnum == 0 or  num % xnum == 0:
           print("La diferencia entre",num1,"que es el mayor y ",num, "que es el menor  oriniga divisor exacto de alguno de los numeros\n") 
       else: 
           print("La diferencia entre",num1,"que es el mayor y ",num, "que es el menor no oriniga divisor exacto de alguno de los numeros\n") 
          

cal()
