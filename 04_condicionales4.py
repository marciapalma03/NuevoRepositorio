#Escribir un programa que pida al usuario un numero entero y muestre por pantalla si es par o impar

n = int(input("Introduce un numero entero: "))
if n % 2 == 0:
    print("El numero " + str(n) + " es par")
else:
    print("El numero " + str(n) + " es impar")