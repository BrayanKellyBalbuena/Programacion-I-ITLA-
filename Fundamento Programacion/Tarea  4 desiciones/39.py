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
      num2 = int(input("Digite el tercer numero entero\n"))
      if num == 0:
         cal
         print ("Numero no valido\n")
      if num1 == 0:
         print ("Numero no valido\n")
         cal()
      if num2 == 0:
         print ("Numero no valido\n")
         cal()   
   except (ValueError):
       print("!Error! Deben ser tres numeros enteros \n")
       cal()
   if ((abs(num) % 100) // 10 == (abs(num1) % 100) // 10) and ((abs(num1) % 100) // 10 == (abs(num2) % 100) // 10):
      print("Los penultimos digitos de los numeros",num,' ',num1,' ',num2,"son iguales\n")
      cont()
   else:
      print("Los penultimos digitos de los numeros",num,num1,num2,"no son iguales\n")
      cont()
   
        
    


    
        
        
    
cal()      
