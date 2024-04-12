#Escribir un programa que pida al usuario un numero entero y muestre por pantalla un triangulo rectangulo como el de 
#mas abajo, de altura el numero introducido
#*
#**
#***
#****
#*****

n = int(input("Introduce la altura del triangulo (entero positivo): "))
for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print("")