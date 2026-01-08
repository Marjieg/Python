"""Ejercicio 3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
mensaje En <asignatura> has sacado <nota> donde <asignatura> es
cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
notas introducidas por el usuario."""


bachiller = ("Matemáticas", "Física", "Química", "Historia", "Lengua")
notas = []
for i in bachiller:
    nota= (input(f"¿qué nota has sacado en {i}?"))
    notas.append(nota)   #con append inserto las notas que se van introduciendo en la lista notas
for n in range(len(bachiller)):  #aquí lo que le digo es que recorra la lista entera
    #seria lo mismoo que poner range(5) el número de las asignaturas
    print(f'En {bachiller[n]} has sacado {notas[n]}')


