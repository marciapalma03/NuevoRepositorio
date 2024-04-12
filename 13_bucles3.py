#Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla todos los numeros impares 
#desde 1 hasta ese numero separados por comas

n = int(input("Introduce un numero entero positivo:"))
for i in range(1, n + 1, 2):
    print(i, end=", ")