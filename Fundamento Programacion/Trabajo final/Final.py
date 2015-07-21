import os
import datetime
from datetime import date
import sqlite3
import sys
import time


errord =date.today()
print("Practica Final Casos Chikungunya".center(78,"="))
time.sleep(2)

def d():
    global dia
    try:
        dia = int(input("Digite el dia de nacimiento >>> "))
    except:
        print("\n!Dia no valido!.intente de nuevo")
        time.sleep(2)
        d()
    if dia < 1 or dia > 31:
        print("\n!Dia no valido!.intente de nuevo")
        time.sleep(2)
        d()
    p = dia    
    return p

def m():
    global mes
    try:
        mes = int(input("\nDigite el mes de nacimiento >>> "))
    except:
        print("\nMes no valido!.intente de nuevo")
        time.sleep(2)
        m()
    if mes < 1 or mes > 12:
        print("\n!Mes no valido!.intente de nuevo")
        time.sleep(2)
        m()
    p = mes    
    return p

def a():
    global an,errord
    try:
        an = int(input("\nDigite el año de nacimiento >>> "))
        if an > errord.year:
            print("!Usted no pudo nacer en el futuro intente de nuevo")
            time.sleep(2)
            a()
    except:
        print("\nAño no valido!.intente de nuevo")
        time.sleep(2)
        a()
    if an < 0:
        print("\n!Año  no valido!.intente de nuevo")
        time.sleep(2)
        a()
    p = an    
    return p

def l():
    global l
    try:
        l = float(input("\nDigite la latitud >>> "))
    except:
        print("\nLatitud no valido!.intente de nuevo")
        time.sleep(2)
        l()
    p = l    
    return p

def lo():
    global lo
    try:
        lo = float(input("\nDigite la longitud >>> "))
    except:
        print("\nLongitud no valido!.intente de nuevo")
        time.sleep(2)
        lo()
    p = lo    
    return p

def cal_edad(dd,mm,yy):
    global cal_ed,errord
    dia = dd
    mes = mm
    año = yy
    cal_ed =(errord.year)-año
    if mes < errord.month:
        return cal_ed
    elif mes == errord.month and dia < errord.day:
        print("Su edad es",cal_ed-1)
        return cal_ed
    elif mes == errord.month and dia >= errord.day:
        print("Su edad es",cal_ed)
        return cal_ed
    elif mes > errord.month:
        print("Su edad es",cal_ed-1)
        return cal_ed
        

    
    
def agregar():
    os.system('cls')
    try:
        cedula = int(input("\nDigite la cedula sin guiones ni espacios>>> "))
    except:
        print("!Cedula no valida !.intente de nuevo")
        time.sleep(2)
        agregar()
    nombre = input("Digite el nombre >>>")
    apellido = input("Digite el apellido >>>")
    dias = int(d())
    meses = int(m())
    años=int(a())
    fecha_n = datetime.date(años,meses,dias)
    edad = cal_edad(dias,meses,años)
    latitud = l()
    longitud = lo()
    sexo = str(input("Digite el sexo >>>"))
    coment=str(input("Digite un comentario >>>"))
    con =sqlite3.connect("Database.s3db")
    cursor = con.cursor()        
    cursor.execute("INSERT INTO  Afectados(Cedula,Nombre,Apellido,Fecha_nac,Edad,Latitud,Longitud,Sexo,Comentario,Dia,Mes) VALUES ('"+str(cedula)+"','"+nombre+"','"+apellido+"','"+str(fecha_n)+"','"+str(edad)+"','"+str(latitud)+"','"+str(longitud)+"','"+sexo+"','"+coment+"','"+str(dias)+"','"+str(meses)+"')")
    con.commit()
    con.close
    print("Persona Agregada")
    time.sleep(2)
    menu()

def usuario():
    os.system('cls')
    print("Digite su opción\n")
    print("1-Reintentar\n2-Ir a menu\n")
    resp = input("Digite su opción >>>")
    if resp == '1':
        modificar()
    elif resp == '2':
        menu()
    else:
        print("!Opción no valida!.")
        time.sleep(2)
        usuario()
        
def usuario1():
    os.system('cls')
    print("Digite su opción\n")
    print("1-Reintentar\n2-Ir a menu\n")
    resp = input("Digite su opción >>>")
    if resp == '1':
        eliminar()
    elif resp == '2':
        menu()
    else:
        print("!Opción no valida!.")
        time.sleep(2)
        usuario1()
def usuario2():
    os.system('cls')
    print("Digite su opción\n")
    print("1-Reintentar\n2-Ir a menu\n")
    resp = input("Digite su opción >>>")
    if resp == '1':
        exportar_html()
    elif resp == '2':
        menu()
    else:
        print("!Opción no valida!.")
        time.sleep(2)
        usuario2()
        
def usuario3():
    os.system('cls')
    print("Digite su opción\n")
    print("1-Reintentar\n2-Ir a menu\n")
    resp = input("Digite su opción >>>")
    if resp == '1':
        exportar_zoo()
    elif resp == '2':
        menu()
    else:
        print("!Opción no valida!.")
        time.sleep(2)
        usuario3()
        
def usuario4():
    os.system('cls')
    print("Digite su opción\n")
    print("1-Reintentar\n2-Ir a menu\n")
    resp = input("Digite su opción >>>")
    if resp == '1':
        exportar_map()
    elif resp == '2':
        menu()
    else:
        print("!Opción no valida!.")
        time.sleep(2)
        usuario4()        
    
def modifica():
    os.system('cls')
    print("1-Modificar\n2-Eliminar\n")
    resp = input("Digite su opción >>>")
    if resp == '1':
        modificar()
    elif resp == '2':
        eliminar()
    else:
        print("!Opción no valida!.")
        time.sleep(2)
        modifica()
        
def reportes():
    os.system('cls')
    print("1-Exportar a html\n2-Exportar signos de zoodiaco\n3-Exportar mapa de afectados\n")
    resp = input("Digite su opción >>>")
    if resp == '1':
        exportar_html()
    elif resp == '2':
        exportar_zoo()
    elif resp == '3':
        exportar_map()    
    else:
        print("!Opción no valida!.")
        time.sleep(2)
        reportes()        
        
            
    
def modificar():
    os.system('cls')
    expo =[]
    con =sqlite3.connect("Database.s3db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Afectados")
    print("Personas Agregadas".center(32,"="))
    for ind in cursor:
        expo.append(ind)
        try:
            print("------------------------------")
            print("|    Cedula   |",ind[0])
            print("|    Nombre   |",ind[1])
            print("|   Apellido  |",ind[2])
            print("|   Fecha_nac |",ind[3])
            print("|     Edad    |",ind[4])
            print("|   Latitud   |",ind[5])
            print("|   Longitud  |",ind[6])
            print("|     Sexo    |",ind[7])
            print("|  Comentario |",ind[8])
            print("------------------------------\n")
        except:
            print("\nNo hay datos digitados que modificar")
            time.sleep(2)
            con.commit()
            con.close
            menu()
    try:
        mt = int(input("Digite la  Cedula de la persona a modificar\n>>> "))
    except:
        print("Error Cedula no valida")
        modificar()
    q = int(0)
    for exp in expo:
        if exp[0]== int(mt):
            cedula = exp[0]
            nombre = exp[1]
            apellido = exp[2]
            fecha_nac = exp[3]
            edad = exp[4]
            latitud = str(exp[5])
            longitud = str(exp[6])
            sexo =exp[7]
            comentario =exp[8]
            q +=int(1)
            break 
    else:
        if q == int(0):
            print("Cedula no encontrado \n")
            time.sleep(2)
            usuario()   
    global vd
    os.system('cls')
    try:
        cedula = int(input("Digite la nueva cedula sin guiones ni espacios de "+str(cedula)+" >>>"))
    except:
        print("!Cedula no valida !.intente de nuevo")
        time.sleep(2)
        try:
            cedula = int(input("\nDigite la nueva cedula sin guiones ni espacios de "+str(cedula)+" >>>"))
        except:
            print("!Cedula no valida !.intente de nuevo")
            time.sleep(2)
            try:
                cedula = int(input("\nDigite la nueva cedula sin guiones ni espacios de "+str(cedula)+" >>>"))
            except:
                print("!Cedula no valida !.intente de nuevo")
                time.sleep(2)
                
    nombre = input("Digite el nuevo nombre  de"+nombre+" >>>")
    apellido = input("Digite el nuevo apellido de"+apellido+" >>>")
    dias = int(d())
    meses = int(m())
    años=int(a())
    fecha_n = datetime.date(años,meses,dias)
    edad = cal_edad(dias,meses,años)
    print("Digite el nuevo valor de la latitud"+str(latitud))
    latitud = l()
    print("Digite el nuevo valor de la longitud "+str(longitud))
    longitud = lo()
    print("dias =",dias,"\nmeses =",meses,"\nano =",años,"\nfech_n =",fecha_n,"\nEdad =",edad,"\nlatitud=",latitud,"\nlongitud=",longitud)
    sexo = str(input("Digite el  nuevo sexo de "+sexo+" >>>"))
    coment=str(input("Digite  el nuevo comentario "+comentario+" >>>"))
    con =sqlite3.connect("Database.s3db")
    cursor = con.cursor()
    eli= "UPDATE Afectados SET Cedula ='"+str(cedula)+"',Nombre='"+nombre+"',Apellido='"+apellido+"',Fecha_nac='"+str(fecha_n)+"',Edad='"+str(edad)+"',Latitud='"+str(latitud)+"',Longitud='"+str(longitud)+"',Sexo='"+sexo+"',Comentario='"+comentario+"',Dia='"+str(dias)+"',Mes='"+str(meses)+"' WHERE Cedula="+str(mt)
    cursor.execute(eli)
    con.commit()
    con.close
    print("Persona modificado")
    time.sleep(2)
    menu()
    
def eliminar():
    os.system('cls')
    expo =[]
    con =sqlite3.connect("Database.s3db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Afectados")
    print("Personas Agregadas".center(32,"="))
    for ind in cursor:
        expo.append(ind)
        try:
            print("------------------------------")
            print("|    Cedula   |",ind[0])
            print("|    Nombre   |",ind[1])
            print("|   Apellido  |",ind[2])
            print("|   Fecha_nac |",ind[3])
            print("|     Edad    |",ind[4])
            print("|   Latitud   |",ind[5])
            print("|   Longitud  |",ind[6])
            print("|     Sexo    |",ind[7])
            print("|  Comentario |",ind[8])
            print("------------------------------\n")
        except:
            print("\nNo hay datos digitados que modificar")
            time.sleep(2)
            con.commit()
            con.close
            menu()
    try:
        mt = int(input("Digite la  Cedula de la persona a eliminar\n>>> "))
    except:
        print("Error Cedula no valida")
        eliminar()
    q = int(0)
    for exp in expo:
        if exp[0]== int(mt):
            cedula = exp[0]
            nombre = exp[1]
            apellido = exp[2]
            fecha_nac = exp[3]
            edad = exp[4]
            latitud = str(exp[5])
            longitud = str(exp[6])
            sexo =exp[7]
            comentario =exp[8]
            q +=int(1)
            break 
    else:
        if q == int(0):
            print("Cedula no encontrado \n")
            time.sleep(2)
            usuario1()
    
    os.system('cls')
    cursor.execute("DELETE FROM Afectados where Cedula = "+str(mt))
    con.commit()
    con.close
    print("Persona eliminada")
    time.sleep(2)
    menu()            

def exportar_html():
    expo=[]
    os.system('cls')
    con = sqlite3.connect("Database.s3db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Afectados ORDER BY Edad asc")
    print("Personas Agregadas".center(32,"="))
    for ind in cursor:
        expo.append(ind)
        try:
            print("------------------------------")
            print("|    Cedula   |",ind[0])
            print("|    Nombre   |",ind[1])
            print("|   Apellido  |",ind[2])
            print("|   Fecha_nac |",ind[3])
            print("|     Edad    |",ind[4])
            print("|   Latitud   |",ind[5])
            print("|   Longitud  |",ind[6])
            print("|     Sexo    |",ind[7])
            print("|  Comentario |",ind[8])
            print("------------------------------\n")
        except:
            print("\nNo hay datos digitados que Exportar")
            time.sleep(2)
            con.commit()
            con.close
            menu()
    mt = int (input("Digite una cedula que este para exportar todos los datos>>>"))       
    q = int(0)
    for exp in expo:
        if exp[0]== int(mt):
            cedula = exp[0]
            nombre = exp[1]
            apellido = exp[2]
            fecha_nac = exp[3]
            edad = exp[4]
            latitud = str(exp[5])
            longitud = str(exp[6])
            sexo =exp[7]
            comentario =exp[8]
            q +=int(1)

    else:
        if q == int(0):
            print("Cedula no encontrada")
            time.sleep(2)
            usuario2()   
    
    ht = open("Tabla-ordenada.html","w")
    html='''
     <html> 
         <head> 
 	      <title>Personas afectadas</title> 
         </head>		
 	      <style> 
 		    body{
 			    background-size:100%;	
 		            font-size:50px;
 		        }
 		     td{
 		            border-style:groove
                       }
 		    table{
 		            border-collapse: separate;
 			    background:white;
 			    width:300px;
 			    margin-top:21px;
 			    font-size:19px;
 		         } 
 	      </style>  
 	  
         <body>
             <center><table border ="3">
 	     <tr>
 	        <td bgcolor ="aquamarine"><font color="Red">Cedula</font></td>
		<td bgcolor ="aquamarine"><font color="blue">Nombre</font></td>
		<td bgcolor ="aquamarine"><font color="blue">Apellido</font></td>
                <td bgcolor ="aquamarine"><font color="blue">Fecha_de_nac</font></td>
                <td bgcolor ="aquamarine"><font color="blue">Edad</font></td>
                <td bgcolor ="aquamarine"><font color="blue">Latitud</font></td>
                <td bgcolor ="aquamarine"><font color="blue">Longitud</font></td>
                <td bgcolor ="aquamarine"><font color="blue">Sexo</font></td>
                <td bgcolor ="aquamarine"><font color="blue">Comentario</font></td>
 	     </tr> 
 	     <tr>
    '''
    for exp in expo:
        cedula = exp[0]
        nombre = exp[1]
        apellido = exp[2]
        fecha_nac = exp[3]
        edad = exp[4]
        latitud = str(exp[5])
        longitud = str(exp[6])
        sexo =exp[7]
        comentario =exp[8]
        html +='<td>'+str(cedula)+'</td>'
        html +='<td>'+nombre+'</td>'
        html +='<td>'+apellido+'</td>'
        html += '<td>'+str(fecha_nac)+'</td>'
        html += '<td>'+str(edad)+'</td>'
        html += '<td>'+str(latitud)+'</td>'
        html += '<td>'+str(longitud)+'</td>'
        html += '<td>'+sexo+'</td>'
        html += '<td>'+comentario+'</td>'
        html += "\n"
        html +="""<tr></tr>"""
    html +=''' 			 
               </table>
             </center> 
          </body> 
      </html>
    '''
    ht.write(html)
    ht.close()
    print("Archivo Exportado")
    time.sleep(2)
    menu()

def exportar_zoo():
    expo=[]
    os.system('cls')
    con = sqlite3.connect("Database.s3db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Afectados ORDER BY Edad asc")
    print("Personas Agregadas".center(32,"="))
    for ind in cursor:
        expo.append(ind)
        try:
            print("------------------------------")
            print("|    Cedula   |",ind[0])
            print("|    Nombre   |",ind[1])
            print("|   Apellido  |",ind[2])
            print("|   Fecha_nac |",ind[3])
            print("|     Edad    |",ind[4])
            print("|   Latitud   |",ind[5])
            print("|   Longitud  |",ind[6])
            print("|     Sexo    |",ind[7])
            print("|  Comentario |",ind[8])
            print("------------------------------\n")
        except:
            print("\nNo hay datos digitados que Exportar")
            time.sleep(2)
            con.commit()
            con.close
            menu()
    mt = int (input("Digite una cedula que este para exportar los simbolos del zoodiaco>>>"))       
    q = int(0)
    for exp in expo:
        if exp[0]== int(mt):
            q +=int(1)

    else:
        if q == int(0):
            print("Cedula no encontrada")
            time.sleep(2)
            usuario3()
    ht = open("Signos.html","w")
    aries,tauro,geminis,cancer,leo,virgo,libra,escorpion,sagitario = 0,0,0,0,0,0,0,0,0
    capricornio,acuario,picis = 0,0,0
    for exp in expo:
        if (exp[9] >= 21 and exp[10] == 3) or (exp[9] <=20 and exp[10] == 4):
            aries +=int(1)
        elif(exp[9] >= 21 and exp[10] == 4) or (exp[9] <=21 and exp[10] == 5):
            tauro +=int(1)
        elif(exp[9] >= 22 and exp[10] == 5) or (exp[9] <=21 and exp[10] == 6):
            geminis +=int(1)
        elif(exp[9] >= 22 and exp[10] == 6) or (exp[9] <=22 and exp[10] == 7):
             cancer +=int(1)
        elif(exp[9] >= 23 and exp[10] == 7) or (exp[9] <=22 and exp[10] == 8):
             leo+=int(1)
        elif(exp[9] >= 23 and exp[10] == 8) or (exp[9] <=22 and exp[10] == 9):
             virgo+=int(1)
        elif(exp[9] >= 23 and exp[10] == 9) or (exp[9] <=22 and exp[10] == 10):
             libra+=int(1)     
        elif(exp[9] >= 23 and exp[10] == 10) or (exp[9] <=22 and exp[10] == 11):
             escorpion+=int(1)
        elif(exp[9] >= 23 and exp[10] == 11) or (exp[9] <=21 and exp[10] == 12):
             sagitario+=int(1)     
        elif(exp[9] >= 22 and exp[10] == 12) or (exp[9] <=20 and exp[10] == 1):
             sagitario+=int(1)
        elif(exp[9] >= 21 and exp[10] == 1) or (exp[9] <=19 and exp[10] == 2):
             capricornio+=int(1)
        else:
            picis +=int(1)
    html ='''
     <html> 
         <head> 
 	      <title>Personas afectadas</title> 
         </head>		
 	      <style> 
 		    body{
 			    background-size:100%;	
 		            font-size:50px;
 		        }
 		     td{
 		            border-style:groove
                       }
 		    table{
 		            border-collapse: separate;
 			    background:white;
 			    width:300px;
 			    margin-top:21px;
 			    font-size:17px;
 		         } 
 	      </style>  
 	  
         <body>
             <center><table border ="3">
             <tr><td bgcolor ="aquamarine"><font color="blue">Aries</font></td><td bgcolor ="aquamarine"><font color="blue">Tauro</font></td><td bgcolor ="aquamarine"><font color="blue">Geminis</font></td><td bgcolor ="aquamarine"><font color="blue">Cancer</font></td><td bgcolor ="aquamarine"><font color="blue">Leo</font></td>
             <td bgcolor ="aquamarine"><font color="blue">Virgo</font></td><td bgcolor ="aquamarine"><font color="blue">Libra</font></td><td bgcolor ="aquamarine"><font color="blue">Escorpion</font></td><td bgcolor ="aquamarine"><font color="blue">Sagitario</font></td><td bgcolor ="aquamarine"><font color="blue">Capricornio</font></td>
             <td bgcolor ="aquamarine"><font color="blue">Acuario</font></td><td bgcolor ="aquamarine"><font color="blue">Picis</font></td></tr>
 	     <tr>
 	        <td><a><img src="aries.png"/></a></td>
		<td><a><img src="tauro.png"/></a></td>
		<td><a><img src="geminis.png"/></a></td>
                <td><a><img src="cancer.png"/></a></td>
                <td><a><img src="leo.png"/></a></td>
                <td><a><img src="virgo.png"/></a></td>
                <td><a><img src="libra.png"/></a></td>
                <td><a><img src="escorpion.png"/></a></td>
                <td><a><img src="sagitario.png"/></a></td>
                <td><a><img src="capricornio.png"/></a></td>
                <td><a><img src="acuario.png"/></a></td>
                <td><a><img src="picis.png" alt=""/></a></td>
 	     </tr> 
 	     <tr>
    '''
    html +='<td><font color="red">'+str(aries)+'</font></td>'
    html +='<td><font color="green">'+str(tauro)+'</font></td>'
    html +='<td><font color="yellow">'+str(geminis)+'</font></td>'
    html +='<td><font color="light grey">'+str(cancer)+'</font></td>'
    html +='<td><font color="gold">'+str(leo)+'</font></td>'
    html +='<td><font color="dark wood">'+str(virgo)+'</font></td>'
    html +='<td><font color="sea green">'+str(libra)+'</font></td>'
    html +='<td><font color="dark purple">'+str(escorpion)+'</font></td>'
    html +='<td><font color="violet">'+str(sagitario)+'</font></td>'
    html +='<td><font color="black">'+str(capricornio)+'</font></td>'
    html +='<td><font color="blue">'+str(acuario)+'</font></td>'
    html +='<td><font color="grey">'+str(picis)+'</font></td>'
    html +=''' </tr>			 
           </table>
          </center> 
	</body> 
    </html>
    '''
    ht.write(html)
    ht.close()
    print("Archivo Exportado")
    time.sleep(2)
    menu()

def exportar_map():
    expo=[]
    os.system('cls')
    con = sqlite3.connect("Database.s3db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Afectados ORDER BY Edad asc")
    print("Personas Agregadas".center(32,"="))
    for ind in cursor:
        expo.append(ind)
        try:
            print("------------------------------")
            print("|    Cedula   |",ind[0])
            print("|    Nombre   |",ind[1])
            print("|   Apellido  |",ind[2])
            print("|   Fecha_nac |",ind[3])
            print("|     Edad    |",ind[4])
            print("|   Latitud   |",ind[5])
            print("|   Longitud  |",ind[6])
            print("|     Sexo    |",ind[7])
            print("|  Comentario |",ind[8])
            print("------------------------------\n")
        except:
            print("\nNo hay datos digitados que Exportar")
            time.sleep(2)
            con.commit()
            
            menu()
    mt = int (input("Digite una cedula que este para exportar el mapa>>>"))       
    q = int(0)
    for exp in expo:
        if exp[0]== int(mt):
            q +=int(1)

    else:
        if q == int(0):
            print("Cedula no encontrada")
            time.sleep(2)
            usuario4()
            
    ht= open("Mapa.html","w")        
    html='''
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Info windows</title>
    <style>
      html, body, #map-canvas {
        height: 100%;
        margin: 0px;
        padding: 0px
      }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp"></script>
    <script>
// This example displays a marker at the center of Australia.
// When the user clicks the marker, an info window opens.
     
function initialize() {'''+"\n  " 
    num = 1
    for i in expo:
        ubi= str(i[5])+","+str(i[6])
        html+="""var myLatlng"""+str(num)+"""=new google.maps.LatLng("""+ubi+""");
  """
        num+=1
    html+='''
  var mapOptions = {
    zoom: 10,
    center: myLatlng1
  };

  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);'''+"\n"+''''''
    
    vr = 1
    for i in expo:
        apellido = exp[2]
        fecha_nac = exp[3]
        age = exp[4]
        latitud = str(exp[5])
        longitud = str(exp[6])
        sexo =exp[7]
        inf =i[8]
        nomb = i[1]
        sec = exp[0]
        html+="""
  var contentString"""+str(vr)+""" = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h3 id="firstHeading" class="firstHeading">Afectado por chikuguya :</h3>'+
      '<div id="bodyContent">'+
      '<p>Nombre: """+nomb+"""</p>'+
      '<p>Apellido: """+apellido+"""</p>'+
      '<p>Latitud: """+str(latitud)+"""</p>'+
      '<p>Longitud: """+str(longitud)+"""</p>'+
      '<p>Comnetario: """+inf+"""</p>'+
      '<p>Cuarentena</p>'+
      '</div>'+
      '</div>';"""+"\n"
        vr+=1    
    lm = 1    
    for i in expo:
       html+=""" 
  var infowindow"""+str(lm)+""" = new google.maps.InfoWindow({
      content: contentString"""+str(lm)+"""
  });"""+"\n"
       lm += 1
    mv = 1
    for i in expo:
        cas = "'Caso Chikungunya #"+str(mv)+"'"
        html+="""
  var marker"""+str(mv)+"""= new google.maps.Marker({
      position: myLatlng"""+str(mv)+""",
      map: map,
      title:"""+cas+"""
  });"""+"\n"
        mv +=1
    mk=1    
    for i in expo:
        html+="""
  google.maps.event.addListener(marker"""+str(mk)+""", 'click', function() {
    infowindow"""+str(mk)+""".open(map,marker"""+str(mk)+""");
  });"""+"\n"
        mk +=1
    html+="""    
}
    
google.maps.event.addDomListener(window, 'load', initialize);

    </script>
  </head>
  <body>
    <div id="map-canvas"></div>
  </body>
</html>
    """
    ht.write(html)
    ht.close()
    print("Archivo Exportado")
    time.sleep(2)
    menu()

def menu() :
    os.system('cls')
    print("1-Agregar Caso\n2-Modificar Caso\n3-Reportes\n4-Salir\n")
    resp =input("Digite su opcion\n>>> ")
    if resp == '1':
        agregar()
    elif resp == '2':
        modifica()
    elif resp == '3':
        reportes()
    elif resp == '4':
        c = 5
        while c != 0 :
            print("El programa se cirra en",c,"segundos\n")
            time.sleep(1)
            os.system('cls')
            c-=1
            if c == 0:
                print("ADIOS".center(78,"*"))
                time.sleep(1)
                sys.exit(1)
            
    else:
        print("\n!Opción no valida! ")
        time.sleep(2)
        menu()

menu()    
