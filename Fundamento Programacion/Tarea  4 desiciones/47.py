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
   dig1n = num // 10
   dig2n = num % 10
   dig1n1 =num1 // 10
   dig2n1 =num1 % 10
   x = 0
   pri = 1
# ------------------------------------------------------------------------------ 
   if num > num1:
       xnum = num - num1
       if   xnum % 2 == 0: 
           print("La suma de los digitos es",dig1n + dig2n + dig1n1 + dig2n1)
                 
   if num1 > num:
       xnum = num1 - num
       while pri <= num:
           if num % pri == 0:
              x +=1
           pri += 1
   if xnum < 10 and x == 2:
       print('El producto de los dos numeros es',num * num1,'\n')
   if xnum % 10 == 4:
       print(dig1n,' ',dig2n,' ',dig1n1,' ',dig2n2)
       cont()

cal()
