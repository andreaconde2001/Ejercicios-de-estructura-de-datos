class deber:
    #Dado un número entero cuya cantidad de dígitos es igual a 5, determine
    #si es capicúa.
    #Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás
    def ejercicio11(self):
        n= int(input("Ingresa un número de 5 dígitos: "))
        s = str(n) 
        reverso = s[::-1]
        if s == reverso:
          print("SI es capicua")
        else:
         print("NO es capicua") 

    #Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como
    #resultado su equivalente en segundos. 
    def ejercicio12(self):
        print("Ingrese una hora y minutos en hh mm (separados con espacio): ", end=" ")
        h, m = map(int, input().split())
        s = (h*3600)+(m*60)
        print("las horas y minutos es: {} hora(s):{} minuto(s)".format(h,m))
        print("\nllevadas a SEGUNDOS es: {} segundos".format(s))
         
    #Para un valor entero positivo que representa una cantidad en segundos, indicar
    #su equivalente en minutos, horas y días.
    def ejercicio13(self):
        seg=int(input("Ingrese los segundos que desee convertir: "))
        if seg>=60:
            min= seg / 60
            print("\n en MINUTOS: {} minuto(seg)".format(min))
        else:
            print("\n en MINUTOS: 0 minuto(seg)")
        if seg>=3600:
           hor= seg / 3600
           print("\n en HORAS: {} hora(seg)".format(hor))
        else:
           print("\n en HORAS: 0 dia(seg)")
        if seg>=86400:
           dia= seg/86400
           print("\n en DIAS: {} dia(seg)".format(dia))
        else:
           print("\n en DIAS: 0 dia(seg)")
           
    #Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el
    #mayor? y ¿cuál es el segundo mayor? 
    def ejercicio14(self):
        n1= int(input("ingrese el primer número positivo: "))
        n2= int(input("ingrese el segundo número positivo: "))
        n3= int(input("ingrese el tercer número positivo: "))
        if n3 > n2 > n1:
           print("\n el número mayor es: {} y el segundo mayor es {} ".format(n3,n2))
        elif n3 > n1 > n2:
           print("\n el número mayor es: {} y el segundo mayor es {} ".format(n3,n1))
        elif n2 > n3 > n1:
           print("\n el número mayor es: {} y el segundo mayor es {} ".format(n2,n3))
        elif n2 > n1 > n3:
           print("\n el número mayor es: {} y el segundo mayor es {} ".format(n2,n1))
        elif n1 > n2 > n3:
           print("\n el número mayor es: {} y el segundo mayor es {} ".format(n1,n2))
        elif n1 > n3 > n2:
           print("\n el número mayor es: {} y el segundo mayor es {} ".format(n1,n3))
           
    #En un estacionamiento el monto a pagar se calcula multiplicando el número de
    #horas que permaneció el automóvil dentro del estacionamiento por Bs. 4 y se
    #incrementa esta cantidad en Bs. 2,50 por cada media hora adicional. 
    #Ahora se desea que usted elabore un algoritmo que a partir de la hora de entrada
    #y la hora de salida de un vehículo (las mismas corresponden a un mismo día)
    #calcule el monto a pagar por el dueño del vehículo.
    #La entrada vendrá dada por dos enteros positivos el primero representa las horas
    #y el segundo los minutos, además por último se debe leer un carácter (A o P) que
    #indica si la hora es AM o PM.
    def ejercicio15(self):
        t1 = [0, 0, "", 0, 0, ""]
        t2 = [0]*2
        pbs = ["la hora de entrada", "los minutos excedentes de entrada", 2, "la hora de salida", "los minutos excedentes de salida", 5]
        ct = 0

        for i in pbs:
            if (ct != 2 or ct != 5):
                if (i != 2 and i != 5):
                    t1[ct] = int(input("Ingrese {}: ".format(i)))
                ct += 1
            if ct == 2 or ct == 5:
                a = input("La hora que ingresó es AM o PM? ")
                t1[(pbs[ct])] = a

        t2[0] = (t1[0] * 3600) + (t1[1] * 60)
        t2[1] = (t1[3] * 3600) + (t1[4] * 60)

        if t1[2] == t1[5]:
            nhp = t2[1] - t2[0]
        else:
            nhp = (43200 - t2[0]) + t2[1]

        t2[0] = (nhp-(nhp % 3600)) / 3600
        t2[1] = (nhp%3600)/60
        print(t2)
        mp = t2[0] * 4

        if t2[1] >= 30:
            mp = mp + 2.50
        print("El dueño del vehículo pagará Bs. ",mp)


    #El IMC resulta de la división de la masa del individuo (en kilogramos) entre el
    #cuadrado de la estatura (en metros). El índice de masa corporal es un indicador
    #del peso de una persona en relación con su altura.
    #Clasificación del IMC de acuerdo con la OMS de la ONU:
    #a. Menor a 16: Criterio de ingreso.
    #b. 16 a 16.9: infra peso.
    #c. 17 a 18.4: bajo peso.
    #d. 18.5 a 24.9: peso normal.
    #e. 25 a 29.9: sobrepeso.
    #f. 30 a 34.9: obesidad pre-mórbida.
    #g. 40 a 45: obesidad mórbida.
    #h. Mayor a 45: obesidad híper-mórbida.
    def ejercicio16(self):
      print("\n")
      masa= float(input("Ingrese la masa en kilogramos: "))
      estatura = float(input("Ingrese su estatura en metros: "))  
      IMC = masa/estatura
      if 16 < IMC < 16.9:
         print("Infra peso")
      elif 17 < IMC < 18.4:
         print("Bajo peso")
      elif 18.5 < IMC < 24.9:
         print("Peso normal")
      elif 25 < IMC < 29.9:
         print("Sobrepeso")
      elif 30 < IMC < 34.9:
         print("Obesidad pre-móbida")
      elif 40 < IMC < 45:
         print("Obesidad mórbida")  
      else:
         print("Obesidad híper-móbida ")

           
    #Escriba un algoritmo que reciba una fecha (día y mes) correspondiente al año
    #2014 e imprima por pantalla el número de días que han pasado desde el 1 de
    #Enero de 2014 hasta la fecha dada.
    def ejercicio17(self):
        año = int(input("Ingrese el año: "))
        mes = int(input("Ingrese el mes: "))
        dia = int(input("Ingrese el dia: "))
        from datetime import date
        fechainicial = date(2014,1,1)
        fechafinal = date(año, mes ,dia)
        dias = fechafinal - fechainicial
        print ("El numero de dias es de: " + str(dias))
        
    #Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho
    #número.  
    def ejercicio18(self):
         n = int(input("Ingrese el numero del mes 1-12 : "))
         if n == 1:
            print("enero")
         elif n == 2:
            print("febrero") 
         elif n == 3:
            print("marzo")   
         elif n == 4:
            print("abril") 
         elif n == 5:
           print("mayo")
         elif n == 6:
           print("junio") 
         elif n == 7:
           print("julio")
         elif n == 8:
           print("agosto")  
         elif n== 9:
           print("septiembre")
         elif n == 10:
           print("octubre")
         elif n == 11:
           print("noviembre")
         elif n == 12:
           print("diciembre")
         else:
           print("El numero no se encuentra en el rango establecido")          

    #En un almacén se hace un 20% de descuento a los clientes cuya compra supere
    #los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto 
    # a pagar por el cliente y arroje como salida el monto aplicando el descuento de
    #ser necesario.
    def ejercicio19(self):
         print("Ingrese Monto : ")
         monto = float(input())
         if monto>1000:
            print("Tendrá un Descuento del 20% : ",monto*0.20)
         else:
            print("El monto no es mayor que 1000 , por lo tanto o hay descuento")
    #Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene 
    #dicho número.
    def ejercicio20(self):
        n= int(input("ingrese un numero: "))
        contador = len(str(n))
        print("El numero ingresado tiene %s digitos" % (contador)) 
                


tarea = deber()                               
tarea.ejercicio11()
tarea.ejercicio12()
tarea.ejercicio13()
tarea.ejercicio14()
tarea.ejercicio15()
tarea.ejercicio16()
tarea.ejercicio17()
tarea.ejercicio18()
tarea.ejercicio19()
tarea.ejercicio20()
