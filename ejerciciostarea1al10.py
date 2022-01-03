class deber:
    #¿De cuál tipo de dato sería la variable donde almacena lo siguiente?
    def ejercicio1(self):
        variable1 = "Hola mundo"
        variable2 = True
        variable3 = ",,1'"
        variable4 = ",,c'"
        variable5 = 256
        variable6= 8>19
        print("La variable 1 es de tipo: ",type(variable1)) 
        print("La variable 2 es de tipo: ",type(variable2)) 
        print("La variable 3 es de tipo: ",type(variable3)) 
        print("La variable 4 es de tipo: ",type(variable4)) 
        print("La variable 5 es de tipo: ",type(variable5)) 
        print("La variable 6 es de tipo: ",type(variable6))  
    #¿Siguiendo la prioridad de operadores, convierta a expresión matemática,
    #resuelva e indique en cuál tipo de variable almacenará el resultado de las
    #siguientes expresiones: 
    def ejercicio2(self):
        operacion1 = (5 + 3 * 2) + 9 > 3 * 5 * 14 % 3
        operacion2 = 2 * (4 - 10 + 8) /2 * 36 * (1/2)
        operacion3 =  260 / 12 + 54 % 3 - 85 % 7
        operacion4 = (48 < 2 * 3) or  (2 * 7 < 12)
        operacion5 = ((8 > 2) or (932 < 23) ) and (4 == 2)
        print("El resultado de la operacion 1 es de tipo booleano: " + str(operacion1)) 
        print("El resultado de la operacion 2 es de tipo flotante: " + str(operacion2))
        print("El resultado de la operacion 3 es de tipo flotante: " + str(operacion3))
        print("El resultado de la operacion 4 es de tipo booleano: " + str(operacion4))
        print("El resultado de la operacion 5 es de tipo booleano: " + str(operacion5))     
        
    #Dados dos (2) números calcule la suma, resta, multiplicación, división y módulo.
    def ejercicio3(self):
        numero1 = int(input("Ingrese el numero 1: "))
        numero2 = int(input("Ingrese el numero 2: "))
        suma = numero1 + numero2
        resta = numero1 - numero2
        multiplicacion = numero1 * numero2
        division = numero1 / numero2
        modulo = numero1 % numero2
        print("El resultado de la suma es: " + str (suma))
        print("El resultado de la resta es: " + str (resta))
        print("El resultado de la multiplicacion es: " + str (multiplicacion))
        print("El resultado de la division es: " + str (division))
        print("El resultado del modulo es: " + str (modulo))
    #Dados tres (3) números, Hacer una aplicación que calcule la resolvente.    
    def ejercicio4(self):
        import math
        print("ax² + bx + c = 0\n")
        a, b, c = [float(input(f"Ingrese el coeficiente {coef}: ")) for coef in ("a", "b", "c")]
        discriminante =  b * b - 4 * a * c
        if discriminante < 0:   
           print(f"La ecuación no tiene soluciones reales.")
        else:
           raiz = math.sqrt(discriminante)       
           x1 = (-b + raiz) / (2 * a)      
           if discriminante != 0:           
              x2 = (-b - raiz) / (2 * a)  
              print(f"Las soluciones son: {x1} y {x2}.")  
           else:
              print(f"La única solución es: x = {x1}")  
              
    #Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.    
    def ejercicio5(self):
        A = int(input("Ingrese el  valor del primer lado: "))
        B = int(input("Ingrese el  valor del segundo lado: "))
        hipotenusa = (A** + B**2) ** 0.5
        print("El valor de la hipotenusa es: " + str (hipotenusa))
            
    #Dado un (1) número, imprimir 0 si es par y 1 si es impar.
    def ejercicio6(self):
        num =int(input("Ingresa un número: "))  
        if num % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")
            
    #Dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad.  
    # El bit de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.
    def ejercicio7(self):
        a=int(input("Introduce el año: "))
        if a%4==0 and a%100!=0 or a%400==0:
         print(a," es un año bisiesto")
        else:
         print(a," no es un año bisiesto")
            
    #Dado un (1) número binario de cuatro (4) dígitos imprimir su valor.
    def ejercicio8(self):
        numero_binario = input("Ingrese un numero binario de cuatro digitos: ")
        numero_decimal = 0
        for posicion, digito_string in enumerate(numero_binario[::-1]):
            numero_decimal += int(digito_string) * 2 ** posicion
        print("El valor del numero binario es: " + str(numero_decimal))

                  
    #Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades,
    #decenas, centenas y unidades de mil. 
    def ejercicio9(self):
        numero = int(input("ingrese el numero: "))
        unidades = numero % 10
        decenas = (numero % 100 - numero % 10 ) // 10
        centenas = (numero % 1000 - numero % 100) // 100
        unidadesdemil = (numero % 10000 - numero % 1000) // 1000
        print("unidades: " + str(unidades))
        print("decenas: " + str(decenas))
        print("centenas: " + str(centenas))
        print("unidades de mil: " + str(unidadesdemil))
        
    #Todos los años que se dividen exactamente entre 400, o que son divisibles
    #exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos.
    #Usando estas premisas crea un algoritmo que lea una fecha como un número
    #entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si
    #el mismo es un año bisiesto o no.
    def ejercicio10(self):
        print("Ingrese una fecha en dd mm aaaa (separados con espacio): ", end=" ")
        d, m, a = map(int, input().split())
        print("\nla fecha que pusiste es: {}/{}/{}".format(d,m,a))
        
        if a % 400 == 0:
           print("el año {} SI es bisiesto".format(a))
        elif a %100 == 0:
          print("el año {} NO es bisiesto".format(a))
        elif a %4 == 0:
          print("el año {} SI es bisiesto".format(a))
        else:
          print("el año {} NO es bisiesto".format(a))    
        

               
tarea = deber()                               
tarea.ejercicio1()
tarea.ejercicio2()
tarea.ejercicio3()
tarea.ejercicio4()
tarea.ejercicio5()
tarea.ejercicio6()
tarea.ejercicio7()
tarea.ejercicio8()
tarea.ejercicio9()
tarea.ejercicio10()
 
   

 
