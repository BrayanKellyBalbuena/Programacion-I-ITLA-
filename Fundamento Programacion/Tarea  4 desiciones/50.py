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
      if ErrorMuchodig(num) == True:
          print("El numero debe ser menor que 100")
          cal()
   except (ValueError):
       print("!Error! Deben ser un numero entero \n")
       cal()
   if num < 0:
      num *= -1
   ud = num % 10 
   if num % 4 == 0:
       print("La mitad es",int(num / 2),'\n')
   if num % 5:
       print("Su cuadrado es",num * num,'\n')
   if num % 6:    
      print("El primer digito es",num // 10,'\n')
   cont()

def ErrorMuchodig(num):
    if abs(num) > 100:
        return True
    else:
        return False
cal()
