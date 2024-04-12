#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 
#hasta su edad)

age = int(input("¿Cuantos años tienes? "))
for i in range(age):
    print("Has cumplido " + str(i + 1) + " años")