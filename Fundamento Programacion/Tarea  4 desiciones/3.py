def cont():
   m = input("Digite S para continuar o N para salir.\n")
   if m == "S":
      cal()
   elif m == "N":
      print("Good bye.")    
   elif m != "S":
      print("Carater no valido.Debe ser S o N.\n")	
      cal()
def cal():
   try:
      num = int(input("Digite un numero entero.\n"))
   except ValueError:
      print( "!Error¡ Debe ser un numero entero.\n")
      cont()
   if num == 0:
      print("!Hey y ese gancho,el numero ",num,"es neutro\n")
      cont()
   elif num < 0:
      print("El numero",num,"es negativo.\n")
      cont()	  
   else:
      print("El numero",num,"es positivo.\n") 
      cont()
cal()
  
