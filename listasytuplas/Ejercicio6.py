"""Ejercicio 6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
usuario tiene que repetir."""


bachiller = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in bachiller:
    nota= int((input(f"¿qué nota has sacado en {asignatura}?")))
    #eliminar las asignaturas aprobadas de la lista osea > 5
    if nota < 5:
       notas.append(asignatura) #creo la lista notas con las asignaturas que están suspensas
print("tienes que repetir estas asiganturas: ")
for asignatura in notas:
    print(asignatura)
