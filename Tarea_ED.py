#Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.
class Tarea:
    def ejercicio1(self):
        print("Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.")
        costo=float(input("Costo de la cena: $"))
        servicio=costo*0.062
        propina=costo*0.1
        print("El costo total de la comida: $", costo+servicio+propina)
        
    def ejercicio2(self):
        print("\n")
        print("Solicitar al usuario que ingrese el dia, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numerica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa. Hacer otra version del programa, pero esta vez almacenando todo en una unica variable numerica, en la forma DDMMAAAA. ¿Y si la variable fuera de tipo string?")
        fecha=int(input("Fecha en formato DDMMAAA: "))
        anio=fecha%10000
        dia=fecha//1000000
        mes=(fecha//10000)%100
        print(str(dia),"/",str(mes), "/",str(anio))

    def ejercicio3(self):
        print("\n")
        print("Solicitar al usuario que ingrese el dia, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numerica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa. Hacer otra version del programa, pero esta vez almacenando todo en una unica variable numerica, en la forma DDMMAAAA. ¿Y si la variable fuera de tipo string?")
        fecha=input("Fecha en formato DDMMAAA: ")
        anio=fecha[4:]
        dia=fecha[:2]
        mes=fecha[2:4]
        print(str(dia),"/",str(mes), "/",str(anio))

    def ejercicio4(self):
        print("\n")
        print("Solicitar al usuario que ingrese el dia, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numerica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa. Hacer otra version del programa, pero esta vez almacenando todo en una unica variable numerica, en la forma DDMMAAAA. ¿Y si la variable fuera de tipo string?")
        dia=input("Dia de tu nacimiento: ")
        mes=input("Mes de tu nacimiento: ")
        anio=input("Año de tu nacimiento: ")
        print(dia,"/",mes,"/",anio)

    def ejercicio5(self):
        print("\n")
        print("Solicitar al usuario que ingrese el dia, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numerica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa. Hacer otra version del programa, pero esta vez almacenando todo en una unica variable numerica, en la forma DDMMAAAA. ¿Y si la variable fuera de tipo string?")
        dia=int(input("Dia de tu nacimiento: "))
        mes=int(input("Mes de tu nacimiento: "))
        anio=int(input("Año de tu nacimiento: "))
        print(dia,"/",mes,"/",anio)

    def ejercicios6(self):
        print("\n")
        print("Una pareja de motociclistas necesita hacer ciertos calculos antes de emprender un viaje en moto, para saber cuantos tanques de combustible consumira el viaje entero. Para eso deben ingresar: cuantos kilometros puede recorrer su moto con 1 litro de combustible, que capacidad (en litros) tiene el tanque y cuantos kilometros en total recorreran. Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustibles necesarios.")
        capacidad=float(input("Capacidad del tanque: "))
        kmxl=float(input("Rendimiento (km por litro): "))
        recorrido=float(input("Km totales a recorrer: "))
        kmxtanque=capacidad*kmxl
        print("Seran necesarios", recorrido/kmxtanque, "tanques.")

    def ejercicios7(self):
        print("\n")
        print("Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).")
        numero=int(input("Número:"))
        if numero<0:
            numero=numero*-1
        print("Valor absoluto:", numero)

    def ejercicios8(self):
        print("\n")
        print("Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación, imprimir “coincidencia” si los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. Si no es así, imprimir “no hay coincidencia”.")
        nombre1=input("Un nombre: ")
        nombre2=input("Otro nombre: ")
        indice_final_nombre1=len(nombre1)-1
        indice_final_nombre2=len(nombre2)-1
        if nombre1[0] == nombre2[0] or nombre1[indice_final_nombre1] == nombre2[indice_final_nombre2]:
            print("coincidencia")
        else:
            print("no hay coincidencia")

    def ejercicios9(self):
        print("\n")
        print("Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.")
        candidato=input("Candidato elegido: ")
        if candidato.upper()=="A":
            print("Usted ha votado por el partido rojo")
        elif candidato.upper()=="B":
            print("Usted ha votado por el partido verde")
        elif candidato.upper()=="C":
            print("Usted ha votado por el partido azul")
        else:
            print("Opción errónea")

    def ejercicios10(self):
        print("\n")
        print("Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.")
        letra=input("Letra:")
        if len(letra)!=1:
            print("Debe ser sólo una letra")
        else:
            if letra.lower() in "aeiou":
                print("Es vocal")

    def ejercicios11(self):
        print("\n")
        print("Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.")
        anio=int(input("Año:"))
        if anio%4 == 0:
            if anio%100 != 0 or anio%400 == 0:
                print("Bisiesto")
            else:
                print("No bisiesto")
        else:
            print("No bisiesto")

    def ejercicios12(self):
        print("\n")
        print("Escribir un programa que muestre la sumatoria de todos los números entre el 0 y el 100.")
        total=0
        for i in range(101):
            if i%3==0:
                total=total+i
        print("Sumatoria:", total)

    def ejercicios13(self):
        print("\n")
        print("Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.")
        numero=int(input("Número:"))
        f=1
        if numero!=0:
            for i in range(1,numero+1):
                f=f*i
        print("Factorial:", f)

    def ejercicios14(self):
        print("\n")
        print("Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…")
        n1=0
        n2=1
        print(n1)
        print(n2)
        for i in range(8):
            n3=n1+n2
            print(n3)
            n1=n2
            n2=n3

    def ejercicios15(self):
        print("\n")
        print("Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.")
        print("No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error si no se ingresaron números positivos.")
        sumaPositivos=0
        cantidadPositivos=0
        sumaNegativos=0
        for i in range(6):
            nro=int(input("Número: "))
            if nro>0:
                sumaPositivos=sumaPositivos+nro
                cantidadPositivos=cantidadPositivos+1
            else:
                sumaNegativos=sumaNegativos+nro
        print("Sumatoria de los negativos: ", sumaNegativos)
        if cantidadPositivos!=0:
            print("Promedio de los positivos: ",sumaPositivos/cantidadPositivos)
        else:
            print("No se ingresaron números positivos")

    def ejercicios16(self):
        print("\n")
        print("Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.")
        print("Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.")
        total=0
        monto=float(input("Monto de una venta: $"))
        while monto!=0:
            if monto<0:
                print("Monto no válido.")
            else:
                total+=monto
            monto=float(input("Monto de una venta: $"))
        if total>1000:
            total-=total*0.1
        print("Monto total a pagar: $", total)

    def ejercicios17(self):
        print("\n")
        print("Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.")
        print("Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.")
        numero=int(input("numero: "))
        totalPares=0
        totalImpares=0
        while numero!=0:
            pares=0
            impares=0
            while numero!=0:   
                ultimodigito=numero%10
                if ultimodigito%2==0:
                    pares+=1
                    totalPares+=1
                else:
                    impares+=1
                    totalImpares+=1
                numero=numero//10
            print("El número ingresado tiene ",pares," digitos pares y ",impares," digitos impares")
            numero=int(input("Otro número: "))
        print("Total de dígitos pares:", totalPares)
        print("Total de dígitos impares:", totalImpares)

    def ejercicios18(self):
        print("\n")
        print("Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.")
        print("**Ejemplo de ejecución:**")
        print("Libro: Los 3 mosqueteros")
        print("Libro: Historia de 2 ciudades")
        print("Libro: /")
        print("Línea completa. Aparecen 2 dígitos numéricos.")
        print("Libro: 20000 leguas de viaje submarino")
        print("Libro: El señor de los anillos")
        print("Libro: /")
        print("Línea completa. Aparecen 5 dígitos numéricos.")
        print("Libro: 20 años después")
        print("Libro: *")
        print("Fin. Se leyeron 2 líneas completas.")
        digitosEnLaLinea=0
        cantLineas=0
        titulo=input("Titulo del libro: ")
        while titulo!="*":
            if titulo =="/":
                cantLineas+=1
                print("Linea completa. Aparecen", digitosEnLaLinea, "digitos")
                digitosEnLaLinea=0
            else:
                for caracter in titulo:
                    if caracter in "0123456789":
                        digitosEnLaLinea+=1
            titulo=input("Titulo del libro: ")
        print("Fin. Se leyeron", cantLineas, "lineas")

    def ejercicios19(self):
        print("\n")
        print("Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”. La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”. Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales. Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento. Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”. Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27 Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.")
        corrimiento=int(input("Corrimiento: "))
        alfabeto="abcdefghijklmnñopqrstuvwxyz"
        for i in range(5):
            mensaje=input("Mensaje a encriptar: ")
            encriptado=""
            for caracter in mensaje:
                if caracter.lower() in alfabeto:
                    indice=alfabeto.find(caracter.lower())
                    indice=(indice+corrimiento)%27
                    encriptado+=alfabeto[indice]
                else:
                    encriptado+=caracter
                print("Mensaje encriptado: ", encriptado)

    def ejercicios20(self):
        print("\n")
        print("Analizar el codigo mostrado a continuacion y, sin ejecutarlo previamente, describir que hace.")
        print("¿Que salida se mostraria en pantalla si se ejecuta el programa sucesivamente con los siguientes datos?")
        print("Frase: hola buen dia")
        print("frase: """)
        print("frase: 1234")
        print("frase: hola ¡buen dia!")
        frase=input("Frase: ")
        frase=frase.strip()
        cantidad=0
        len_p_mas_larga=0
        while len(frase) !=0:
            cantidad=cantidad+1
            i=frase.find(" ")
            if i != -1:
                palabra=frase[0:i]
                while i < len(frase) and frase[i] == " ":
                    i=i+1
                frase=frase[i:]
            else:
                palabra=frase
                frase=""
            if len(palabra) > len_p_mas_larga:
                len_p_mas_larga=len(palabra)
                p_mas_larga=palabra
            if cantidad > 0:
                print("Palabra mas larga:",p_mas_larga)
            print("Cantidad de palabras:", cantidad)

    def ejercicios21(self):
        print("\n")
        print("Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.")
        cantidad=0
        n=int(input("Número: "))
        while n!=0:
            primo=True
            for i in range(2,n):
                if n%i==0:
                    primo=False
            break
        if primo:
            cantidad+=1
            n=int(input("Número: "))
        print("primos: ", cantidad)

    def ejercicios22(self):
        print("\n")
        print("Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10. Nota: para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.")
        anioInicio=int(input("Año inicial:"))
        anioFin=int(input("Año final:"))
        for anio in range(anioInicio, anioFin+1):
            if not anio%10==0:
                continue
            if not anio%4==0:
                continue
            if anio%100!=0 or anio%400==0:
                print(anio)

    def ejercicios23(self):            
        def coordenadaZ (x,y):
            print("\n")
            print("Sin ejecutar el siguiente programa, determinar cuál es la salida en pantalla si se ingresan los valores x=6, y=7:")
            x = x + 10
            y = y + 15
            return x + y
        #programa principal

        x = int(input("Coordenada eje x: "))
        y = int(input("Coordenada eje y: "))
        for i in range(3):
            z = coordenadaZ (x,y)
            x = x + 1
            y = y + 1
        # print (x, " . ", y)
        def maximo(a,b):
            print("\n")
            print("El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?")
            if a>b:
                return a
            else:
                return b
        def minimo(a,b):
            if a<b:
                return a
            else:
                return b
        #programa principal
        x = int(input("Un número: "))
        y = int(input("Otro número: "))
        print(maximo(x-3, minimo(x+2, y-5)))

    def ejercicio24(self):
        def validaDNI():
            print("\n")
            print("#Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.")
            num = input('Digite su identificación: ')
            if len(num)>=7 and len(num)<=8:
                return True
            else:
                return False
        print(validaDNI())
        print("\n")
        frase = str(input('Escriba una frase: '))

        def len_ultima_palabra(str):
            print("\n")
            print("#Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío. Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. Si un socio tuviera más de un apellido, el usuario sólo ingresará uno. Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto. Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su DNI. Ejemplo: Nombre: Alba María Linares DNI: 25834910 Alba7258")
            longitud = 0
            str = str.strip()
            for i in str:
                if not i.isspace():
                    longitud += 1
                else:
                    longitud = 0
            return(longitud)
        print(len_ultima_palabra(frase))
        
    def ejercicio25(self):
        def lenUltimaPalabra(cadena):
            longitud=len(cadena)
            if longitud==0:
                return 0
            cantidad=0
            for i in range(longitud):
                if cadena[i]!=' ':
                    cantidad+=1
                else:
                    if cadena[i]==' ' and i<(longitud-1) and cadena[i+1]!=' ':
                        cantidad=0
            return cantidad
        print(lenUltimaPalabra("hola soy"))

    def ejercicios26(self):
        def DNIvalido(dni):
            print("\n")
            cantidad=0
            while dni != 0:
                cantidad+=1
                dni//=10
            return cantidad == 7 or cantidad ==8
        
        def lenUltimaPalabra(cadena):
            longitud=len(cadena)
            if longitud == 0:
                return 0
            cantidad = 0
            for i in range(longitud):
                if cadena[i] != " ":
                    cantidad+=1
                else:
                    if cadena[i] == " " and i<(longitud-1) and cadena[i+1] != " ":
                        cantidad = 0
            return cantidad

        def primerosTresDigitos(numero):
            while numero >= 1000:
                numero /= 10
            return(int(numero))

        def obtenerIdentificador(nombre,dni):
            nombre=nombre.strip()
            i = nombre[0:nombre.find(" ")]
            i=i+str(lenUltimaPalabra(nombre))
            i = i + str(primerosTresDigitos(dni))
            return i

        nombre=input("Nombre del socio: ")
        while nombre != "":
            dni = int(input("DNI del socio: "))
            while not(DNIvalido(dni)):
                print("Número inválido")
            dni = int(input("DNI del socio: "))
            identificador=obtenerIdentificador(nombre,dni)
            print("El identificador del socio es: ",identificador)
            nombre= input("Nombre del socio: ")

    def ejercicios27(self):
        print("\n")
        print("Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse. A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar. Recorrer la lista para imprimir la sumatoria de todos los elementos. Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella. Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]")
        def sumatoria(lista):
            suma=0
            for n in lista:
                suma+=n
            return suma

        def numerosMenores(lista, limite):
            nueva=[]
            for n in lista:
                if n<limite:
                    nueva.append(n)
            return nueva

        def frecuencias(lista):
            nueva=[]
            for n in lista:
                if [n, lista.count(n)] not in nueva:
                    nueva.append([n, lista.count(n)])
            return nueva
        #A
        numeros=[]
        nro=int(input("Número: "))
        while nro!=0:
            numeros.append(nro)
            nro=int(input("Número: "))
        #B
        print("Sumatoria de los números:", sumatoria(numeros))
        eliminar=int(input("Número a eliminar: "))
        #C
        if eliminar in numeros:
            numeros.remove(eliminar)
        else:
            print("Ese número no está entre los ingresados")
        #D
        limite=int(input("Filtrar números menores a: "))
        for n in numerosMenores(numeros, limite):
            print(n)
        #E
        print("Frecuencias:")
        for tupla in frecuencias(numeros):
            print(tupla[0],"aparece",tupla[1],"veces.")

    def ejercicios28(self):
        print("\n")
        print("#Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo: [(Manuel Juarez, 19823451, Liverpool), (Silvana Paredes, 22709128, Buenos Aires), (Rosa Ortiz, 15123978, Glasgow), (Luciana Hernandez, 38981374, Lisboa)] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: [(Buenos Aires,Argentina), (Glasgow,Escocia), (Lisboa, Portugal), (Liverpool,Inglaterra), (Madrid,España)] Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones: Agregar pasajeros a la lista de viajeros. Agregar ciudades a la lista de ciudades. Dado el DNI de un pasajero, ver a qué ciudad viaja. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad. Dado el DNI de un pasajero, ver a qué país viaja. Dado un país, mostrar cuántos pasajeros viajan a ese país. Salir del programa.")
        def agregarPasajeros(pasajeros):
            nombre = input("Nombre -x para cortar: ")
            while nombre != "x":
                dni=int(input("DNI: "))
                destino = input("Ciudad destino: ")
                pasajeros.append((nombre, dni, destino))
                nombre = input("Nombre -x para cortar: ")
            return pasajeros

        def agregarCiudades(ciudades):
            ciudad = input("Ciudad -x para cortar: ")
            while ciudad != "x":
                pais = input("Pais: ")
                ciudades.append((ciudad,pais))
                ciudad = input("Ciudad -x para cortar: ")
            return ciudades

        def buscarCiudad(pasajeros, dni):
            for viaje in pasajeros:
                if viaje[1]==dni:
                    return viaje[2]
            return ""

        def cantidadPasajerosCiudad(pasajeros, ciudad):
            cantidad = 0
            for viaje in pasajeros:
                if viaje[2] == ciudad:
                    cantidad+=1
            return cantidad

        def buscarPaisDestino(pasajeros, ciudades, dni):
            ciudadBuscada=buscarCiudad(pasajeros, dni)
            for ciudad in ciudades:
                if ciudad[0] == ciudadBuscada:
                    return ciudad[1]
            return ""

        def cantidadPasajerosPais(pasajeros, ciudades, pais):
            cantidad = 0
            for viaje in pasajeros:
                if pais == buscarPaisDestino(pasajeros, ciudades, viaje[1]):
                    cantidad+=1
            return cantidad

        pasajeros =[("Manuel Juarez", 12345678, "Liverpool"),("Silvana Paredes", 22709128, "Buenos Aires"),("Rosa Ortiz", 12534563, "Inglaterra")]
        ciudades = [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Lisboa", "Portugal"), ("Liverpool", "Inglaterra"), ("Madrid", "España")]
        while True:
            print("1. Agregar pasajeros\n2. Agregar ciudades \n3. Buscar ciudad destino mediante el DNI \n4. Cantidad de pasajeros que viajan a una ciudad \n5. Buscar país destino mediante DNI \n6. Cantidad de pasajeros que viajan a un país\n7. Salir del programa")
            opcion = int(input("Acción a ejecutar: "))
            if opcion == 1:
                print("AGREGAR PASAJEROS")
                pasajeros=agregarPasajeros(pasajeros)
            elif opcion == 2:
                print("AGREGAR CIUDADES")
                ciudades=agregarCiudades(ciudades)
            elif opcion == 3:
                dni=int(input("DNI: "))
                print("El pasajero viaja a", buscarCiudad(pasajeros, dni))        
            elif opcion == 4:
                ciudad = input("Ciudad: ")
                print("Viajan", cantidadPasajerosCiudad(pasajeros, ciudad),"pasajeros")
            elif opcion == 5:
                dni = int(input("DNI: "))
                print("Viaja a", buscarPaisDestino(pasajeros, ciudades, dni))
            elif opcion == 6:
                pais=input("País: ")
                print("Viajan", cantidadPasajerosPais(pasajeros, ciudades, pais),"pasajeros")
            elif opcion == 7:
                break
    def ejercicios29(self):
        print("\n")
        print("Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar “x”. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar “x”.")
        print("Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.<>")
        print("Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.")
        print("Informar qué nombres de nivel primario no se repiten en los de nivel secundario.")
        def cargarNombres(alumnos):
            nombre = input("Nombre: ")
            while nombre != "x":
                alumnos.add(nombre)
                nombre= input("Nombre: ")
            return alumnos

        primaria = set()
        secundaria=set()
        print("ALUMNOS DE PRIMARIA")
        primaria = cargarNombres(primaria)
        print("ALUMNOS DE SECUNDARIA")
        secundaria = cargarNombres(secundaria)

        print("NOMBRES DE TODOS LOS ALUMNOS: ")
        for nombre in primaria|secundaria:
            print(nombre)

        print("NOMBRES COMUNES:")
        for nombre in primaria&secundaria:
            print(nombre)

        print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA")
        for nombre in primaria-secundaria:
            print(nombre)

    def ejercicios30(self):
        print("\n")
        print("Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual contiene tuplas con informacion de cada venta: (cliente, dia del mes, monto, domicilio del cliente). Ejemplo:")
        print("[(Nuria Costa, 5, 12780.78, Calle Las Flores 355), (Jorge Russo, 7, 699, Mirasol 218), (Nuria Costa, 7, 532.90), Calles Las Flores 355), (Julian Rodriguez, 12, 5715.99, La Mancha 761), (Jorge Russo, 15, 958, Mirasol 218)]")
        print("Escribir una funcion que reciba como parametros una lista con el formato mencionado anteriormente y retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente puede haber hecho mas de una compra al mes, por lo que la funcion debe retornar una estructura que contenga cada domicilio una sola vez")
        def direcciones(ventas):
            domicilios=set()
            for venta in ventas:
                domicilios.add(venta[3])
            return domicilios
        
        direcc = [("Nuria Costa", 5, 12790.78, "Calle las Flores 355"), ("Jorge Russo", 7, 669, "Mirasol 218"), ("Nuria Costa", 9, 532.90, "Calle las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
        print(direcciones(direcc))

    def ejercicios31(self):
        print("\n")
        print("Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo: r:5, %:3, a:8, 9:1.")
        print("¿Cómo se podrían informar las ocurrencias de las letras del alfabeto únicamente, incluyendo el valor 0 para las letras que no aparecieron?")
        contadores = {}
        alfabeto="abcdefghijklmnñopqrstuvwxyz"
        for letra in alfabeto.upper():
            contadores[letra] = 0
        for i in range(3):
            cadena = input("Cadena de caracteres: ")
            for caracter in cadena:
                if caracter.lower() in alfabeto:
                    contadores[caracter]+=1
        
        for caracter,cantidad in contadores.items():
            print(caracter, ":", cantidad)

    def ejercicios32(self):
        def cargarSocios(socios):
            print("\n")
            print("Crear un programa para gestionar datos de los socios de un club, permitiendo:")
            print("Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar con los datos de los socios fundadores ya cargados:")
            print("Socio nº1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.")
            print("Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.")
            print("Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.")
            print("Informar cantidad de socios del club.")
            print("Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.")
            print("Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018.")
            print("Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).")
            print("Imprimir el listado de socios completo.")
            numero = int(input("Número de socio:"))
            while numero != 0:
                nombre = input("Nombre y apellido: ")
                fecha = input("Fecha de ingreso: ")
                cuota = input("Cuota al día s/n: ")
                pago = cuota.lower() == "s"
                socios[numero] = [nombre,fecha,pago]
                numero = int(input("Número de socio: "))
            return socios 
    
        def modificarFecha(socios, fecha_anterior, fecha_nueva):
            for datos in socios.values():
                if datos[1]==fecha_anterior:
                    datos[1]= fecha_nueva
            return socios

        def numeroSocio(socios,nombre):
            for numero, datos in socios.items():
                if datos[0].lower() == nombre.lower():
                    return numero
            return 0

        def formatoFecha(fecha):
            return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

        def imprimirListado(socios):
            for numero, datos in socios.items():
                print("-Número: ",numero)
                print("-Nombre: ",datos[0])
                print("-Fecha de ingreso: ",formatoFecha(datos[1]))
                if datos[2]:
                    print("-Cuota al día")
                else:
                    print("-En deuda")
                print("~~~~")
            return None
        socios_activos={1:["Amanda Núñez", "17032009", True], 2:["Bárbara Molina","17032009"], 3:["Lautaro Campos","17032009"]}
        print("***Cargar Socios")
        socios_acitvos=cargarSocios(socios_activos)

        print("El club tiene", len(socios_activos), "socios")

        print("***Registrar pago de cuotas")
        numero = int(input("Número de socio: "))
        socios_activos[numero][2] = True

        print("***Modificando fecha de ingreso...")
        socios_activos = modificarFecha(socios_activos, "13032018", "14032018")
        
        print("***Eliminar socio: ")
        nombre = input("Nombre y Apellido: ")
        numero = numeroSocio(socios_activos, nombre)
        del socios_activos[numero]

        imprimirListado(socios_activos)

ejercicios = Tarea()
ejercicios.ejercicio1()
ejercicios.ejercicio2()
ejercicios.ejercicio3()
ejercicios.ejercicio4()
ejercicios.ejercicio5()
ejercicios.ejercicios6()
ejercicios.ejercicios7()
ejercicios.ejercicios8()
ejercicios.ejercicios9()
ejercicios.ejercicios10()
ejercicios.ejercicios11()
ejercicios.ejercicios12()
ejercicios.ejercicios13()
ejercicios.ejercicios14()
ejercicios.ejercicios15()
ejercicios.ejercicios16()
ejercicios.ejercicios17()
ejercicios.ejercicios18()
ejercicios.ejercicios19()
ejercicios.ejercicios20()
ejercicios.ejercicios21()
ejercicios.ejercicios22()
ejercicios.ejercicios23()
ejercicios.ejercicio24()
ejercicios.ejercicio25()
ejercicios.ejercicios26()
ejercicios.ejercicios27()
ejercicios.ejercicios28()
ejercicios.ejercicios29()
ejercicios.ejercicios30()
ejercicios.ejercicios31()
ejercicios.ejercicios32()