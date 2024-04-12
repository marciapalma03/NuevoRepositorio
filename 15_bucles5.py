#Escribir un programa que pregunte al usuario una cantidad a invertir, el interes anual y el numero de años, y muestre 
#por pantalla el capital obtenido en la inversion cada año que dura la inversion

amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interes porcentual anual? "))
years = int(input("¿Años? "))
for i in range(years):
    amount *= 1 + interest / 100
    print("Capital tras " + str(i + 1) + "años: " + str(round(amount, 2)))