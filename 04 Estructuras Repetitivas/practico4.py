
#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

n = input("ingrese un numero entero:")
c = len(n)
print(f"El numero contiene {c} digitos.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1 = int(input("ingrese el primer numero entero: "))
num2 = int(input("ingrese el segundo numero entero: "))
suma = 0 
if num1 < num2:
    for i in range(num1 + 1, b):
        suma += i
else:
    for i in range(num2+ 1, num1):
        suma += i
print("la suma es:" ,suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

total = 0
num = 1
while num != 0:
    num = int(input("ingrese un numero entero (0 para terminar): "))
    total = total + num
print("La suma total es: ", total)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
intentos = 0 

num_aleatorio = random.randint(0, 9)
num = int(input("ingrese un numero entre el 0 y el 9: "))

while num != num_aleatorio:
    intentos = intentos + 1
    print("opcion incorrecta, pruebe nuevamente")
    num = int(input("ingrese un numero entre el 0 y el 9: "))
    
intentos = intentos + 1
print("el numero es correcto")
print(f"el numero de intentos fue: {intentos}")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for num in range(100,-1,-1):
    if num % 2 == 0:
        print(num)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

num = int(input("ingrese un numero entero positivo: "))
suma = num * (num + 1 ) // 2
print(f"la suma de los numeros enteros entre 0 y {num} es: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad = 100
pares = impares = negativos = positivos = 0

for i in range(cantidad):
    num = int(input("ingrese un numero entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1
    
print("numeros pares: ", pares)
print("numeros impares: ", impares)
print("numeros negativos: ", negativos)
print("numeros positivos: ", positivos)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

cantidad = 100
suma = 0

for i in range(cantidad):
    num = int(input("Ingrese un número entero: "))
    suma += num

prom = suma / cantidad
print("El promedio es:", prom)
    
#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745 

num = input("Ingresa un número: ")
numero_invertido = ""

for digito in num:
    numero_invertido = digito + numero_invertido

print("Número invertido:", numero_invertido)