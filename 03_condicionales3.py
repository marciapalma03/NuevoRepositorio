#Escriba un programa que pida al usuario dos numeros y muestre por pantalla su division. Si el divisor es cero el 
#programa debe mostrar un error

n = float(input("Introduce el dividendo: "))
m = float(input("Introduce el divisor: "))
if m == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(n/m)