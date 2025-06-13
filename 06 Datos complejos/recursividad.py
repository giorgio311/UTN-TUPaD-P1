#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
        
        
n = int(input("ingrese un numero: "))

for i in range(0, n + 1):
    print(f"{i}! = {factorial(i)}")
    
#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
serie = int(input("ingrese hasat que posicion desea ver la serie de Fibonacci: "))

for i in range(0, serie):
    print(fibonacci(i))
    
#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛
#𝑚 = 𝑛 ∗ 𝑛(𝑚−1).  Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

print(potencia(2, 3))

#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(num):
    if num <= 0:
        return "El numero ingresado no es valido"
    elif num == 1:
        return "1"
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

num = int(input("Ingrese un numero para convertir a binario: "))
print("El resultado en binario del numero ingresado es:", decimal_a_binario(num))

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.
# Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed()

def es_palindromo(palabra, inicio = 0, fin = None):
    if fin is None:
        fin = len(palabra) - 1
    if inicio >= fin:
        return True
    if palabra[inicio] != palabra[fin]:
        return False
    return es_palindromo(palabra, inicio + 1,fin -1)

palabra = input("Ingrese una palabra para saber si es o no un palindromo: ")
print(es_palindromo(palabra))

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:
#suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
#suma_digitos(9) → 9
#suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n == 0:
        return "El numero ingresado no es valido, intente nuevamente"
    elif n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

n = int(input("Ingrese un numero entero y positivo para sumar sus digitos: "))
print("La suma de los digitos del numero ingresado es la siguiente:", suma_digitos(n))

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.

#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.
# Ejemplos:
#contar_bloques(1) → 1 (1)
#contar_bloques(2) → 3 (2 + 1)
#contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
print(contar_bloques(1))  
print(contar_bloques(2))  
print(contar_bloques(4))

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.
# Ejemplos:
#contar_digito(12233421, 2) → 3
#contar_digito(5555, 5) → 4 
#contar_digito(123456, 7) → 0 

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
        
print(contar_digito(12233421, 2))  
print(contar_digito(5555, 5))      
print(contar_digito(123456, 7))    

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito a contar (0-9): "))

resultado = contar_digito(numero, digito)

print(f"El dígito {digito} aparece {resultado} veces en {numero}.")