#Escribir un programa que pregunte al usuario los numeros ganadores de la loteria primitiva, los almacene en una lista 
#y los muestre por pantalla ordenados de menor a mayor

awarded = []
for i in range(6):
    awarded.append(int(input("Introduce un numero ganador: ")))
awarded.sort()
print("Los numeros ganadores son: " + str(awarded))