#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la 
#evaluacion comienzan en 0.0 y pueden ir aumentando, traduciendose en mejores beneficios. Los puntos que pueden conseguir 
#los empleados pueden ser 0.0, 0.4, 0.6 o mas, pero no valores intermedios entre las cifras mencionadas. A continuacion 
#se muestra una tabla con los niveles correspondientes a cada puntuacion. La cantidad de dinero conseguida en cada nivel 
#es de 2.400€ multiplicada por la puntuacion del nivel.
# ________________________________
#|    Nivel    |    Puntuacion    |
#|Inaceptable  |       0.0        |
#|Aceptable    |       0.4        |
#|Meritorio    |     0.6 o mas    |
#|________________________________|
#Escribir un programa que lea la puntuacion del usuario e indique su nivel de rendimiento, asi como la cantidad de dinero 
#que recibira el usuario

bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuacion: "))
#Clasificacion por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
#Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuacion no es valida")
else:
    print("Tu nivel de rendimiento  es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))