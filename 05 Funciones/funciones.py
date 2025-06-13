#1.	Crear una función llamada imprimir_hola_mundo que imprima por pantalla el
#mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("hola mundo!") 
    
imprimir_hola_mundo()

#2.	Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un 
#nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con 
#saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función
#desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print (f"Hola {nombre}!")
    
nombre = input("ingrese su nombre: ")
saludar_usuario(nombre)

#3.	Crear una función llamada informacion_personal(nombre, apellido, edad, residencia)
#que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años 
#y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores 
#ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"{nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    
nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = int(input("ingrese su edad: "))
residencia = input("ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#4.	Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
#y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio    
#como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y 
#llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    area = 3.14 * radio ** 2
    print(f"El area del circulo es {area}")
    
def calcular_perimetro_circulo(radio):
    perimetro = 2 * radio * 3.14
    print(f"El perimetro del circulo es {perimetro}")
    
radio = float(input("ingrese el radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#5.	Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de 
#segundos como parámetro y devuelva la cantidad de horas correspondientes. 
#Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos = float(input("ingrese una cantidad de segundos: "))
print (f"equivale a {segundos_a_horas(segundos)} horas")

#6.	Crear una función llamada tabla_multiplicar(numero) que reciba un número como 
#parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al 
#usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        
numero = int(input("ingrese un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#7.	Crear una función llamada operaciones_basicas(a, b) que reciba dos números como 
#parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, 
#multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    print(f"el resultado de la suma es: {suma}")
    print(f"el resultado de la resta es: {resta}")
    print(f"el resultado de la multiplicacion es: {multiplicacion}")
    print(f"el resultado de la division es: {division}")
    return (suma, resta, multiplicacion, division)

a = float(input("ingrese el valor del primer numero: "))
b = float(input("ingrese el valor del segundo numero: "))

operaciones_basicas(a, b)

#8.	Crear una función llamada calcular_imc(peso, altura) que reciba el peso en 
#kilogramos y la altura en metros, y devuelve el indice de masa corporal (IMC). Solicitar 
#al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    dos_decimales = round(imc, 2)
    print(f"tu indice de masa corporal (IMC) es: {dos_decimales}")

peso = float(input("ingrese su peso en kilogramos: "))
altura = float(input("ingrese su altura en metros: "))

calcular_imc(peso, altura)

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura
#en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la
#temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print (f"El equivalente a {celsius}°C (celsius) a fahrenheit es {fahrenheit}°F (fahrenheit).")
    
celsius = int(input("ingrese una temperatura en grados celcius: "))

celsius_a_fahrenheit(celsius)

#10. Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como 
# parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar 
# el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio es: {promedio}")
    
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))

calcular_promedio(a, b, c)