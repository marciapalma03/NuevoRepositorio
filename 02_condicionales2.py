#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la 
#contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable
#sin tener en cuenta mayusculas y minusculas

key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password.lower():
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")