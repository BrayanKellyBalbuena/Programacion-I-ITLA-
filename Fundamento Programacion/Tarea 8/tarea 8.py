#Programa Calcula hora de inicio y final de una actividad y lo exporta en html

import os
import sys
import time


#Variables
activ,activ_1,activ_2,activ_3,activ_4,activ_5,activ_6,activ_7,activ_8,activ_9 = 0,0,0,0,0,0,0,0,0,0
tin,tin1,tin2,tin3,tin4,tin5,tin6,tin7,tin8,tin9 = 0,0,0,0,0,0,0,0,0,0
tf,tf1,tf2,tf3,tf4,tf5,tf6,tf7,tf8,tf9 = 0,0,0,0,0,0,0,0,0,0
t,t1,t2,t3,t4,t5,t6,t7,t8,t9 = 0,0,0,0,0,0,0,0,0,0


print ('Nota: las horas van en formato 24 horas no se aceptan  los caracteres especiales\nEjemplo 8:00 esta mal 800 bien. y tampoco se aceptan con signo negativo ni los segundos son mayores que 60\n\n')

print("Este programa acepta la hora de inicio de 10 actividades como sus nombres y calcula la hora final de esas actividad y lo exporta en archivo html\n\n")
realizado = input("Digite su nombre >>>")
nom_tours = str(input("Digite el  Titulo del tours >>>"))
descripcion = str(input("Digite la descripcion del tours >>>"))
print()

def clear(): 
    if os.name == "posix":
        return os.system ('clear')
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ('cls')


def cont():
    resp =input("Digite S para continuar o N Para salir'\n")
    if resp == 'S':
        proceso()
    elif resp == 'N':
        c= int(5)
        while c != 0:
            time.sleep(1)
            clear()
            print("El programa se cirra en",c,"segundos !Good Bye!\n")
            c-=1
            if c == 0:
                sys.exit(1)
    else:   
        print("!Error! debe ser S o N\n")
        cont()


def activida():
    global activ
    activ = str(input("Digite el nombre de la primera actividad >>> "))
    tda()
def tda():
    try:
        global tin,t
        tin = int(input("Digite la hora de inicio la primera actividad >>"))
    except:
        print("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda()
    if tin < 0 or tin > 2459:
        print ("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda()    
    ctin = str(tin)
    if len(ctin) == 3:
        if ctin[1] > "5":
            print("Error los segundos deben ser menores o igual que 59  intente de nuevo\n ")
            tda()
    elif len(ctin) == 4:
        if ctin[2] > "5":
            print("Error los segundos deben ser menores o igual que 59  intente de nuevo\n ")
            tda()
    t =str(tin)        
    if len(t) == 3:
        t = t[0]+':'+''+t[1:]+''
    else:
        t = t[:2]+':'+''+t[2:]+''        
    activida1()
    
def activida1():        
    global activ1
    activ1 = str(input("Digite el nombre de la segunda actividad >>> "))
    tda1()
    
def tda1():
    try:
        global tin1,tin,tf,t1
        tin1 = int(input("Digite la hora de inicio la segunda actividad >>"))
    except:
        print("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda1()
    if tin1 < 0 or tin1 > 2459:
        print ("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda1()
    ctin = str(tin1)
    if len(ctin) == 3:
        if ctin[1] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda1()
    elif len(ctin) == 4:
        if ctin[2] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda1()    
    if tin1 < tin or tin1 == tin :
        print ("La primera hora no puede ser mayor que la segunda ni igual intente de nuevo\n")
        tda1()
    tf = str(tin1 - tin)
    if len(tf) == 1:
        tf=str( '00:0'+''+tf+'')
    elif len(tf) == 2:
        tf=str( '00:'+''+tf+'')    
    elif len(tf) == 3:
        tf=str( '0'+''+tf[0]+':'+tf[1:]+'')
    else:
        tf=str(tf[:2]+':'+''+tf[2:]+'')
    t1 =str(tin1)    
    if len(t1) == 3:
        t1 = t1[0]+':'+''+t1[1:]+''
    else:
        t1 = t1[:2]+':'+''+t1[2:]+''    
    activida2()

def activida2():        
    global activ2
    activ2 = str(input("Digite el nombre de la tercera actividad >>> "))
    tda2()
    
def tda2():
    try:
        global tin2,tin1,tf1,tf,t2
        tin2 = int(input("Digite la hora de inicio la tercera actividad >>"))
    except:
        print("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda2()
    if tin2 < 0 or tin2 > 2459:
        print ("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda2()
    ctin = str(tin2)
    if len(ctin) == 3:
        if ctin[1] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda2()
    elif len(ctin) == 4:
        if ctin[2] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda2()    
    if tin2 < tin1 or tin2 == tin1:
        print ("La segunda hora no puede ser mayor ni igual que la tercera intente de nuevo\n")
        tda2()
    tf1 = str(tin2 - tin1)
    if len(tf1) == 1:
        tf1=str( '00:0'+''+tf1+'')
    elif len(tf1) == 2:
        tf1=str( '00:'+''+tf1+'')    
    elif len(tf1) == 3:
        tf1=str( '0'+''+tf1[0]+':'+tf1[1:]+'')
    else:
        tf8=str(tf8[:2]+':'+''+tf8[2:]+'')
    t2 =str(tin2)    
    if len(t2) == 3:
        t2 = t2[0]+':'+''+t2[1:]+''
    else:
        t2 = t2[:2]+':'+''+t2[2:]+''         
    activida3()    

def activida3():        
    global activ3
    activ3 = str(input("Digite el nombre de la cuarta actividad >>> "))
    tda3()
    
def tda3():
    try:
        global tin3,tin2,tf2,tf1,t3
        tin3 = int(input("Digite la hora de inicio la cuarta actividad >>"))
    except:
        print("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda3()
    if tin3 < 0 or tin3 > 2459:
        print ("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda3()
    ctin = str(tin3)
    if len(ctin) == 3:
        if ctin[1] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda3()
    elif len(ctin) == 4:
        if ctin[2] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda3()    
    if tin3 < tin2 or tin3 == tin2:
        print ("La tercera hora no puede ser mayor ni igual que la cuarta intente de nuevo\n")
        tda3()
    tf2 = str(tin3 - tin2)
    if len(tf2) == 1:
        tf2=str( '00:0'+''+tf2+'')
    elif len(tf2) == 2:
        tf2=str( '00:'+''+tf2+'')    
    elif len(tf2) == 3:
        tf2=str( '0'+''+tf2[0]+':'+tf2[1:]+'')
    else:
        tf2=str(tf2[:2]+':'+''+tf2[2:]+'')
    t3 =str(tin3)    
    if len(t3) == 3:
        t3 = t3[0]+':'+''+t3[1:]+''
    else:
        t3 = t3[:2]+':'+''+t3[2:]+''        
    activida4()

def activida4():        
    global activ4
    activ4 = str(input("Digite el nombre de la quinta actividad >>> "))
    tda4()
    
def tda4():
    try:
        global tin4,tin3,tf2,tf3,t4
        tin4 = int(input("Digite la hora de inicio la quinta actividad >>"))
    except:
        print("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda4()
    if tin4 < 0 or tin4 > 2459:
        print ("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda3()
    ctin = str(tin4)
    if len(ctin) == 3:
        if ctin[1] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda4()
    elif len(ctin) == 4:
        if ctin[2] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda4()    
    if tin4 < tin3 or tin4 == tin3:
        print ("La cuarta hora no puede ser mayor ni igual que la quinta intente de nuevo\n")
        tda4()
    tf3 = str(tin4 - tin3)
    if len(tf3) == 1:
        tf3=str( '00:0'+''+tf3+'')
    elif len(tf3) == 2:
        tf3=str( '00:'+''+tf3+'')    
    elif len(tf3) == 3:
        tf3=str( '0'+''+tf3[0]+':'+tf3[1:]+'')
    else:
        tf3=str(tf3[:2]+':'+''+tf3[2:]+'')
    t4 =str(tin4)    
    if len(t4) == 3:
        t4 = t4[0]+':'+''+t4[1:]+''
    else:
        t4 = t4[:2]+':'+''+t4[2:]+''        
    activida5()

def activida5():        
    global activ5
    activ5 = str(input("Digite el nombre de la sexta actividad >>> "))
    tda5()
    
def tda5():
    try:
        global tin5,tin4,tf3,tf4,t5
        tin5 = int(input("Digite la hora de inicio la sexta actividad >>"))
    except:
        print("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda5()
    if tin5 < 0 or tin5 > 2459:
        print ("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda5()
    ctin = str(tin5)
    if len(ctin) == 3:
        if ctin[1] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda5()
    if len(ctin) == 4:
        if ctin[2] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda5()    
    if tin5 < tin4 or tin5 == tin4:
        print ("La quinta hora no puede ser mayor ni igual que la sexta intente de nuevo\n")
        tda4()
    tf4 = str(tin5 - tin4)
    if len(tf4) == 1:
        tf4=str( '00:0'+''+tf4+'')
    elif len(tf4) == 2:
        tf4=str( '00:'+''+tf4+'')    
    elif len(tf4) == 3:
        tf4=str( '0'+''+tf4[0]+':'+tf4[1:]+'')
    else:
        tf4=str(tf4[:2]+':'+''+tf4[2:]+'')
    t5 =str(tin5)    
    if len(t5) == 3:
        t5 = t5[0]+':'+''+t5[1:]+''
    else:
        t5 = t5[:2]+':'+''+t5[2:]+''        
    activida6()

def activida6():        
    global activ6
    activ6 = str(input("Digite el nombre de la septima actividad >>> "))
    tda6()
    
def tda6():
    try:
        global tin6,tin5,tf4,tf5,t6
        tin6 = int(input("Digite la hora de inicio la septima actividad >>"))
    except:
        print("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda5()
    if tin6 < 0 or tin6 > 2459:
        print ("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda6()
    ctin = str(tin6)
    if len(ctin) == 3:
        if ctin[1] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda6()
    elif len(ctin) == 4:
        if ctin[2] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda6()    
    if tin6 < tin5  or tin6 == tin5:
        print ("La sexta hora no puede ser mayor ni que la septima intente de nuevo\n")
        tda6()
    tf5 = str(tin6 - tin5)
    if len(tf5) == 1:
        tf5=str( '00:0'+''+tf5+'')
    elif len(tf5) == 2:
        tf5=str( '00:'+''+tf5+'')    
    elif len(tf5) == 3:
        tf5=str( '0'+''+tf5[0]+':'+tf5[1:]+'')
    else:
        tf5=str(tf5[:2]+':'+''+tf5[2:]+'')
    t6 =str(tin6)    
    if len(t6) == 3:
        t6 = t6[0]+':'+''+t6[1:]+''
    else:
        t6 = t6[:2]+':'+''+t6[2:]+''        
    activida7()

def activida7():        
    global activ7
    activ7 = str(input("Digite el nombre de la octava actividad >>> "))
    tda7()
    
def tda7():
    try:
        global tin7,tin6,tf5,tf6,t7
        tin7 = int(input("Digite la hora de inicio la octava actividad >>"))
    except:
        print("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda7()
    if tin7 < 0 or tin7 > 2459:
        print ("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda7()
    ctin = str(tin7)
    if len(ctin) == 3:
        if ctin[1] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda7()
    elif len(ctin) == 4:
        if ctin[2] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda7()    
    if tin7 < tin6 or tin7 == tin6:
        print ("La septima hora no puede ser mayor ni igual que la octava intente de nuevo\n")
        tda7()
    tf6 = str(tin7 - tin6)
    if len(tf6) == 1:
        tf6=str( '00:0'+''+tf6+'')
    elif len(tf6) == 2:
        tf6=str( '00:'+''+tf6+'')    
    elif len(tf6) == 3:
        tf6=str( '0'+''+tf6[0]+':'+tf6[1:]+'')
    else:
        tf6=str(tf6[:2]+':'+''+tf6[2:]+'')
    t7 =str(tin7)    
    if len(t7) == 3:
        t7 = t7[0]+':'+''+t7[1:]+''
    else:
        t7 = t7[:2]+':'+''+t7[2:]+''        
    activida8()
    
def activida8():        
    global activ8
    activ8 = str(input("Digite el nombre de la novena actividad >>> "))
    tda8()

def tda8():
    try:
        global tin8,tin7,tf6,tf7,t8
        tin8 = int(input("Digite la hora de inicio la novena actividad >>"))
    except:
        print("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda8()
    if tin8 < 0 or tin8 > 2459:
        print ("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda8()
    ctin = str(tin8)
    if len(ctin) == 3:
        if ctin[1] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda8()
    elif len(ctin) == 4:
        if ctin[2] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda8()    
    if tin8 < tin7 or tin8 == tin7:
        print ("La octava hora no puede ser mayor ni igual que la novena intente de nuevo\n")
        tda8()
    tf7 = str(tin8 - tin7)
    if len(tf7) == 1:
        tf7=str( '00:0'+''+tf7+'')
    elif len(tf7) == 2:
        tf7=str( '00:'+''+tf7+'')    
    elif len(tf7) == 3:
        tf7=str( '0'+''+tf7[0]+':'+tf7[1:]+'')
    else:
        tf7=str(tf7[:2]+':'+''+tf7[2:]+'')
    t8 =str(tin8)    
    if len(t8) == 3:
        t8 = t8[0]+':'+''+t8[1:]+''
    else:
        t8 = t8[:2]+':'+''+t8[2:]+''        
    activida9()

def activida9():        
    global activ9
    activ9 = str(input("Digite el nombre de la decima actividad >>> "))
    tda9()

def tda9():
    try:
        global tin9,tin8,tf7,tf8,t9
        tin9 = int(input("Digite la hora de inicio la decima actividad >>"))
    except:
        print("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda9()
    if tin9 < 0 or tin9 > 2459:
        print ("Error debe ser como lo dice la nota del principio intente de nuevo\n")
        tda9()
    ctin = str(tin9)
    if len(ctin) == 3:
        if ctin[1] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda9()
    elif len(ctin) == 4:
        if ctin[2] > "5":
            print("Error los segundos deben ser menores o igual que 59 intente de nuevo\n ")
            tda9()    
    if tin9 < tin8 or tin9 == tin8:
        print ("La novena hora no puede ser mayor ni igual que la decima intente de nuevo\n")
        tda9()
    tf8 = str(tin9 - tin8)
    if len(tf8) == 1:
        tf8=str( '00:0'+''+tf8+'')
    elif len(tf8) == 2:
        tf8=str( '00:'+''+tf8+'')    
    elif len(tf8) == 3:
        tf8=str( '0'+''+tf8[0]+':'+tf8[1:]+'')
    else:
        tf8=str(tf8[:2]+':'+''+tf8[2:]+'')
    t9 =str(tin9)    
    if len(t9) == 3:
        t9 = t9[0]+':'+''+t9[1:]+''
    else:
        t9 = t9[:2]+':'+''+t9[2:]+''    

activida()

tiempo_dura = str(tin9 - tin)
color ="blue"
if len(tiempo_dura) == 1:
    tiempo_dura=str( '00:0'+''+tiempo_dura+'')
elif len(tiempo_dura) == 2:
    tiempo_dura= str('00:'+''+tiempo_dura+'')
elif len(tiempo_dura) == 3:
    tiempo_dura=str('0'+''+tiempo_dura[0]+':'+tiempo_dura[1:]+'')
else:
    tiempo_dura = str(tiempo_dura[:2]+':'+''+tiempo_dura[2:]+'')
   
# Exportar html

html='''
<html> 
     <head> 
 	    <title>+Crear archivo html desde python+</title> 
     </head>		
 	  <style> 
 		    body{ 
 			    background-size:90%; 	
 		    }   font-size:5px; 	    
 		    table{ 
			    border-collapse: separate;
                border-spacing: 2px;
 			    background:white; 
 			    
 			    font-size:10px;
 		    }  
 	  </style>  
 	  
      <body>
'''      
html += "<h2><center>Titulo:  "+nom_tours+"</center></h2>"
html +='''
 	     <center> 
'''
html +='<h4><font color="blue">Descripcion:  '+descripcion+'</font></h4>'
html +='<h3><font color="blue">Itinerario </font></h3>'
html +='<h4><font color="blue">Hora de inicio:  '+t+'</font></h4>'



html +='''
			 
 		     <table> 
 			     <tr> 
				     <td><font color="blue"><ol>Inicio</ol></font></td>
					 <td><font color="blue"><ol>Fin</ol></font></td><td></td>
					 <td><font color="blue"><ol>Tiempo duracion</ol></font></td><td></td>
                                        <td><font color="blue"><ol>Nombre</ol></font></td><td></td> 
 				 </tr> 
 				 <tr>
'''
html +='<td><font color="blue"><ol>'+t+'</ol></font></td>'
html +='<td><font color="blue"><ol>'+t1+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+tf+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+activ+'</ol></font></td><td></td>'    
html +=''' 			 </tr> 
 				 <tr>
'''
html +='<td><font color="blue"><ol>'+t1+'</ol></font></td>'
html +='<td><font color="blue"><ol>'+t2+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+tf1+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+activ1+'</ol></font></td><td></td>'
html +='''
 				 </tr> 
 				 <tr>
'''
html +='<td><font color="blue"><ol>'+t2+'</ol></font></td>'
html +='<td><font color="blue"><ol>'+t3+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+tf2+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+activ2+'</ol></font></td><td></td>'    
html +=''' 			 </tr> 
 				 <tr>
'''
html +='<td><font color="blue"><ol>'+t3+'</ol></font></td>'
html +='<td><font color="blue"><ol>'+t4+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+tf3+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+activ3+'</ol></font></td><td></td>'
html +=''' 			 </tr> 
 				 <tr>
'''
html +='<td><font color="blue"><ol>'+t4+'</ol></font></td>'
html +='<td><font color="blue"><ol>'+t5+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+tf4+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+activ4+'</ol></font></td><td></td>'
html +='''
 				 </tr> 
 				 <tr>
'''
html +='<td><font color="blue"><ol>'+t5+'</ol></font></td>'
html +='<td><font color="blue"><ol>'+t6+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+tf5+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+activ5+'</ol></font></td><td></td>'    
html +=''' 			 </tr> 
 				 <tr>
'''
html +='<td><font color="blue"><ol>'+t6+'</ol></font></td>'
html +='<td><font color="blue"><ol>'+t7+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+tf6+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+activ6+'</ol></font></td><td></td>'
html +=''' 			 </tr> 
 				 <tr>
'''
html +='<td><font color="blue"><ol>'+t7+'</ol></font></td>'
html +='<td><font color="blue"><ol>'+t8+"</ol></font></td><td></td>"
html +='<td><font color="blue"><ol>'+tf7+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+activ7+'</ol></font></td><td></td>'
html +='''
 				 </tr> 
 				 <tr>
'''
html +='<td><font color="blue"><ol>'+t8+'</ol></font></td>'
html +='<td><font color="blue"><ol>'+t9+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+tf8+'</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+activ8+'</ol></font></td><td></td>'   
html +=''' 			 </tr> 
 				 <tr>
'''
html +='<td><font color="blue"><ol>'+t9+'</ol></font></td>'
html +='<td><font color="blue"><ol>00:00</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>00:00</ol></font></td><td></td>'
html +='<td><font color="blue"><ol>'+activ9+'</ol></font></td><td></td>'
html +=''' 			 </tr> 
 				 <tr>


 				 

				 
 			 </table>
'''
html +='<h3><font color="blue"> Tiempo de duracion '+tiempo_dura+'</font></h3>'
html +='<h4><font color="blue"> Hora de fin '+t9+'</font></h4>'
html +='<h5><font color="blue"> Realizado por '+realizado+'</font></h5>'
html +='''
         </center> 
	  </body> 
</html>
'''
ht = open(nom_tours+".html","w")
ht.write(html)
ht.close()

cont()
