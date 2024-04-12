#Escribir un programa que almacene las asignaturas de un curso (por ejemplo matematicas, fisica, quimica, historia y 
#lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las 
#asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir

subjects = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
passed = []
for subject in subjects:
    score = float(input("¿Que nota has sacado en " + subject + "? "))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))