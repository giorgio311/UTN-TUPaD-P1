#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

#2) Crear un programa que ”pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

a = (input("Ingrese su nombre: "))
print(f"Hola {a}")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

n = input("ingrese su nombre: ")
a = input("ingrese su apellido: ")
e = input("ingrese su edad: ")
l = input("ingrese su lugar de residencia: ")
print(f"Soy {n} {a}, tengo {e} y vivo en {l}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

r = float(input("ingrese el radio de un circulo: "))
a = 3.14 * (r ** 2)
p = (r * 2) * 3.14
print(f"El area es {a} y su perimetro es {p}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

s = float(input("Ingrese una cantidad de segundos: "))
h = s/3600
print(f"equivale a {h} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

n = int(input("ingrese un numero: "))
for i in range (1,11,1):
    t = i * n 
    print(f"{n} x {i} = {t}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("ingrese el primer numero entero: "))
num2 = int(input("ingrese el segundo numero entero: "))
print(f"suma: {num1 + num2}\n Divicion: {num1 / num2}\n Multiplicacion: {num1 * num2}\n Resta: {num1 - num2}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#IMC = peso en kl/(altura en m)²

a = float(input("ingrese su altura en mts: "))
p = float(input("ingrese su peso en kl: "))
imc = p / (a**2)
print(f"El indice de su masa corporal es: {imc} kl/m²") 

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5. 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

t = float(input("ingrese una temperatura en celcius: "))
f = (9/5 * t) + 32
print(f"su equivalencia en grados fahrenheit es: {f}")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
num3 = float(input("ingrese el tercer numero: "))
prom = (num1 + num2 + num3) / 3
print(f"el promedio es: {prom}")
