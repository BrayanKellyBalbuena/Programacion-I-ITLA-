# Programa crea archivo html desde python

import os

#---------------Declaración de las variables-----------

mat = (input("Digite su matricula: "))
name = str (input("Digite su nombre: ")) 
lastname = str(input("Digite su apellido: "))
ced = str(input("Digite su cedula con todo y guines: "))
año = int(input("Digite su año de nacimiento: ")) 
mes = int(input("Digite el mes: "))
dias = int(input("Digite el dia: "))
carrera = str(input("Digite su carrera: "))
nacionalida = str(input("Digite su nacionalidad: "))
link_f = str(input("Digite su link de facebook: "))
correo = str(input("Digite su correo electronico: "))
fecha_d = str(dias)+ "/"+str(mes)+"/"+str(año)

#-----------------Datos Calculados---------------

cant_dign = len(name)
cant_dil = len(lastname)
age = 2014-año

if age <= 10:
   color = "blue"
elif age <= 30:
    color = "green"
elif age <= 51:
    color = "black"
else:
   color =  "red"


if age <= 10:
   color_t = "red"
elif age <= 30:
   color_t = "yellow"
elif age <= 51:
    color = "white"
else:
   color = "blue"   
   

if (dias>=21 and mes==3) or (dias<=20 and mes==4):
   signo_sodiacal = "Aries"
elif (dias>=21 and mes==4) or (dias <=21 and mes==5):
   signo_sodiacal = "Tauro"
elif  (dias>=22 and mes == 5) or(dias <= 21 and mes == 6):
   signo_sodiacal = "Geminis"
elif  (dias >= 22 and mes == 6) or (dias <= 22 and mes == 7):
   signo_sodiacal = "Cancer"
elif  (dias >= 23 and mes == 7) or (dias <= 22 and mes == 8):
   signo_sodiacal = "Leo"
elif  (dias >= 23 and mes == 8) or (dias <= 22 and mes == 9):
   signo_sodiacal = "Virgo"
elif  (dias >= 23 and mes == 9) or (dias <= 22 and mes == 10):
   signo_sodiacal = "Libra"
elif  (dias >= 23 and mes == 10) or (dias <= 22 and mes == 11):
   signo_sodiacal = "Escorpión"
elif  (dias >= 23 and mes == 11) or (dias <= 21 and mes == 12):
   signo_sodiacal = "Sagitario"
elif  (dias >= 22 and mes == 12) or (dias <= 20 and mes == 1):
   signo_sodiacal = "Capricornio"
elif  (dias >= 21 and mes == 1) or (dias <= 19 and mes == 2):
   signo_sodiacal = "Acuario"
else:
   signo_sodiacal = "Picis"


#----------------------Procedimiento html---------------------

carpeta = "c:\\xfiles";

if os.path.exists(carpeta) == False:
    os.mkdir(carpeta)

html = open(carpeta+'\\'+ced+'.html','w')
html.write('<html>')
html.write('    <head>')
html.write('	    <title>+Crear archivo html desde python+</title>')
html.write('		<style>')
html.write('		    body{')
html.write('			    background:'+color+';')
html.write('			    background-size:100%;')	
html.write('		    }       font-size:50px;')	    
html.write('		    table{')
html.write('			    background:white;')
html.write('			    width:300px;')
html.write('			    margin-top:10px;')
html.write('			    font-size:16px;')
html.write('		    }')
html.write('                table{')
html.write('                     color: #green;')  
html.write('			 background:white;')
html.write('			 width:300px;')
html.write('			 margin-top:10px;')
html.write('			 font-size:16px;')
html.write('                 }')                
html.write('		</style>') 
html.write('	 </head>')
html.write('     <body>')
html.write('	     <h2><center>Datos digitados</center></h2>')
html.write('	     <center>')
html.write('		     <table border=7>') 
html.write('			     <tr>')
html.write('				     <td>Matricula</td>')
html.write('					 <td>'+mat+'</td>')  
html.write('				 </tr>')
html.write('				 <tr>')
html.write('				     <td>Nombre</td>')
html.write('					 <td>'+name+'</td>')  
html.write('				 </tr>')
html.write('				 <tr>')
html.write('				     <td>Apellido</td>')
html.write('					 <td>'+lastname+'</td>')  
html.write('				 </tr>')
html.write('				 <tr>')
html.write('				     <td>Cedúla</td>')
html.write('					 <td>'+ced+'</td>')  
html.write('				 </tr>')
html.write('				 <tr>')
html.write('				     <td>Fecha de nacimiento</td>')
html.write('					 <td>'+fecha_d+'</td>')
html.write('				 </tr>')
html.write('				 <tr>')
html.write('				     <td>Carrera</td>')
html.write('					 <td>'+carrera+'</td>')  
html.write('				 </tr>')
html.write('				 <tr>')
html.write('				     <td>Nacionalidad</td>')
html.write('					 <td>'+nacionalida+'</td>')  
html.write('				 </tr>')
html.write('				 <tr>')
html.write('				     <td>link de facebook</td>')
html.write('					 <td><A href="'+link_f+'">Link facebook </A></td>')  
html.write('				 </tr>')
html.write('				 <tr>')
html.write('				     <td> Correo</td>')
html.write('					 <td>'+correo+' </td>')  
html.write('				 </tr>') 				  
html.write('			 </table>')
html.write('        </center>')
html.write('')
html.write('')
html.write('')			 
html.write('')			 
html.write('')			 
html.write('		  <h2><center><BLINK>Datos calculados</BLINK></center></h2>')
html.write('          <center>')
html.write('              <table border=7>')
html.write('				   <tr>')
html.write('				     <td>Edad</td>')
html.write('					 <td>'+str(age)+'</td>')  
html.write('				 </tr>')
html.write('				 <tr>')
html.write('				     <td>Cantidad de digitos del nombre</td>')
html.write('					 <td>'+str(cant_dign)+'</td>')  
html.write('				 </tr>')
html.write('				 <tr>')
html.write('				     <td>Cantidad de digitos del apellido</td>')
html.write('					 <td>'+str(cant_dil)+'</td>')  
html.write('				 </tr>')
html.write('				 <tr>')
html.write('				     <td>Signo del zoodiacal</td>')
html.write('					 <td>'+str(signo_sodiacal)+'</td>')  
html.write('				 </tr>')
html.write('			  </table>')			 
html.write('		 </center>')
html.write('	 </body>')
html.write('</html>')
html.close()

  
    
	
   
 














