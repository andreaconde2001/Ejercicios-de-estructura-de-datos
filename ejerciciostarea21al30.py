class deber:
    #Dado un número, determine si es capicúa.
    #Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás.
    def ejercicio21(self):
        n= int(input("Ingresa un número: "))
        s = str(n)
        reverso = s[::-1]
        if s == reverso:
           print("SI es capicua")
        else:
          print("NO es capicua")
    #Dado un número N determinar si es un número primo.
    #Nota: Un número primo es aquel que solo es divisible por 1(uno) y por el mismo.
    def ejercicio22(self):
        numero = int(input("Ingrese un numero: "))
        antecesor = numero - 1
        residuo=0
        contadorDivisibles=0
        while antecesor>1:
            residuo = numero % antecesor
            if residuo == 0:
                contadorDivisibles = contadorDivisibles + 1
            antecesor = antecesor - 1
        if contadorDivisibles == 0:
            print("El numero ingresado es primo")
        else:
            print("El numero no es primo")            
                
                 
    #Construya un programa que dado un valor entero N, haga el cálculo de la función
    #factorial utilizando iterativas. 
    def ejercicio23(self):
        numero=int(input("ingrese numero: "))
        factorial=1
        if numero!=0:
         for i in range(1,numero+1):
          factorial=factorial*i
        print("El factorial:",factorial)
        
    #Dado un número entero N que representa una contraseña y asumiendo que una
    #contraseña debe tener al menos 10 dígitos para ser segura, determine si la
    #contraseña ingresada por el usuario es correcta, de no serlo debe pedirla
    #nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta
    #mostrar un mensaje de éxito al usuario, por salida estándar.  
    def ejercicio24(self):
        validacion = False
        while validacion == False:
            clave = input("Ingrese su contraseña: ")
            if len(clave) == 10:
               print("Ingreso de contraseña exitoso!")
               validacion = True
            else:
               print("La contraseña no es segura, vuelva a intentar!")
               validacion = False
               
    #Dada una secuencia de números terminada en cero (0), elaborar un algoritmo que
    #informe al usuario qué valor tiene el número mayor y qué valor tiene el número
    #menor, sin contar el cero (0).
    def ejercicio25(self):
        lista = []
        a = True
        while a:
            num = int(input("Ingresar un numero(ingrese el 0 si desea terminar)"))
            if num == 0:
                a = False
            else:
                lista.append(num)
        mayor,menor=deber.mayor_menor(lista)
        if len(lista) > 0:
            print("El numero mayor es:",mayor)
            print("El numero menor es:",menor)
    def mayor_menor(lista):       
        mayor = 0
        menor = 9999999999999999999999
        for num in lista:
            if num > mayor:
                mayor = num
            
            if num < menor:
                menor = num
        return mayor,menor

    #Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad,
    #peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con
    #base en dicha secuencia se desea realizar un estudio a fin de conocer:
    #  Edad promedio de todas las personas en la muestra.
    #  Peso promedio de todas las personas en la muestra.
    #  Estatura promedio de todas las personas en la muestra.
    #  Cuántas personas hay con edad entre los 18 y 25 años.
    #  Cuántas personas son mayores a 36 años.
    #  Cuál es el promedio de peso de las personas con edades entre 18 y 35 años.
    def ejercicio26(self):
        edad=[20,18,32,19,22,40]
        peso=[42,52,49,47,50,46]
        estatura=[1.45,1.63,1.52,1.70,1.68,1.57]
        prom_edad=(sum(edad))/len(edad)
        prom_peso=(sum(peso))/len(peso)
        prom_estatura=(sum(peso))/len(estatura)
        c=0
        x=0
        while c<8:
            x+=(edad.count(18+c))
            c+=1  
        c=1
        TreSeis=0  
        while c<150:
            TreSeis+=(edad.count(36+c))
            c+=1
        c=0
        contPos=0
        while c<36:
            contPos=[i for i,x in enumerate(edad) if x>=18 and x<=35]
            c+=1
        suma=0
        c=0
        while c<len(contPos):
            suma+=peso[contPos[0+c]]
            c+=1
        print(f"El promedio de edades de todas las personas es de: {prom_edad:.2f}")
        print(f"El promedio de peso de todas las personas es de: {prom_peso:.2f}")
        print(f"El promdedio de estatura de todas las personas es de: {prom_estatura:.2f}")
        print(f"Hay {x}, personas con edad de entre [18-25] ")
        print(f"Hay {TreSeis}, personas mayor(es) a 36 años")
        print(f"El promedio de peso entre las personas de 18 a 35 años es: {suma/len(contPos):.2f}")

    #Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la
    # tabla del 1 hasta la del 10.
    def ejercicio27(self):
        numero = int(input("Ingrese un numero: "))
        for i in range (1,11):
            print(f' {i} x {numero}={i*numero}')
    #Escribir un algoritmo que muestre todas las fichas de dominó, sin repetir.
    def ejercicio28(self):
        for i in range(1, 7):
            for j in range(i, 7):
                print("todas las fichas de domino {}:{}".format(i, j))
                
    #Dados N número positivos (N>1) calcular el promedio de esta serie. Considere que
    #la serie termina al leer un 0.
    def ejercicio29(self):
        contador = 0
        suma = 0
        numero = 1
        while numero != 0:
            numero = int(input("ingrese un numero entero (0 para terminar):"))
            if numero != 0:
               suma += numero
               contador += 1
        if contador == 0:
            print("no digito ningun numero.")
        else:
           promedio = suma / contador
           print("El promedio de los {} numero es igual a {}.".format(contador, promedio))
    
    #Construya una función que solicite edades al usuario y determine el promedio de
    #las edades mayores a 18 años. El usuario indicará cuando desea dejar de
    #suministrar datos de entrada. En la Acción Principal se informará el promedio
    #calculado.
    def ejercicio30(self):
        acumulador = int(0)
        for x in range (1,5):
           edad = int(input("ingrese la edad: "))
           acumulador = acumulador + edad
        print("El promedio de las edades es de: ", str(acumulador / 5))      
           
tarea = deber()                               
tarea.ejercicio21()
tarea.ejercicio22() 
tarea.ejercicio23() 
tarea.ejercicio24()
tarea.ejercicio25() 
tarea.ejercicio26()
tarea.ejercicio27() 
tarea.ejercicio28()
tarea.ejercicio29() 
tarea.ejercicio30()    
   

              