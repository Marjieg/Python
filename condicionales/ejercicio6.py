#Ejercicio 6
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
#el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
#los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
#programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
#que le corresponde.

nombre = str(input('dime tu nombre'))
sexo = input('dime tu sexo')
#A = mujeres con nombres de A hasta M y hombres con nombres de N en adelante
#B = resto
ini_nombres = nombre.split()
if (sexo == "mujer" and nombre < "M"):
    print("perteneces al grupo A")
elif(sexo == "hombre" and nombre >= "N"):
    print("perteneces al grupo A")
else:
     print("perteneces al grupo B")