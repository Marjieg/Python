"""Ejercicio 6
Escribir un programa que cree un diccionario vacío y lo vaya llenado con
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo
electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato
debe imprimirse el contenido del diccionario."""
#con el .update() voy actualizando el diccionario, introduciéndole los datos nuevos que pongo entre ()
d1= {}
nombre = input('¿cual es tu nombre?')
d1['nombre']= nombre
d1.update({'nombre':nombre})
print(d1)

edad = input('¿cuál es tu edad?')
d1['edad']=edad
d1.update({'edad':edad})
print(d1)

direccion = input ('¿cuál es tu dirección?')
d1['direccion']=direccion
d1.update({'direccion':direccion})
print(d1)

telefono = input ('¿cuál es tu teléfono?')
d1['telefono']=telefono
d1.update({'telefono':telefono})
print(d1)


"""otra forma, de esta puedo introducir cualquier valor, sin que esté predefinido"""

d1= {}
continuar = True
while continuar: #así creo el diccionario-- diccionario = clave: valor, clave: valor..
    clave = input('¿qué dato quieres introducir?')
    valor = input(clave + ': ')
    d1[clave] = valor
    print(d1)
    continuar = input('¿quieres añadir más informacion (si/no)?') =="si"