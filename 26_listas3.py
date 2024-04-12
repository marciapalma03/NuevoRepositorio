#Escribir un programa que almacene las asignaturas de un curso (por ejemplo matematicas, fisica, quimica, historia y 
#lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y despues las muestre por 
#pantalla con el mensaje en <asignatura> has sacado <nota> donde <asignatura> es cada una de las asignaturas de la 
#lista y <nota> cada una de las correspondientes notas introducidas por el usuario

subjects = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Que nota has sacado en " + subject + "? ")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])