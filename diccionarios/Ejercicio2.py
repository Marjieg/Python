"""Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
<nombre> tiene <edad> años, vive en <dirección> y su número de
teléfono es <teléfono>."""

nombre = input('¿cual es tu nombre?')
edad = input('¿cuál es tu edad?')
direccion = input ('¿cuál es tu dirección?')
telefono = input ('¿cuál es tu teléfono?')
persona = {'nombre':nombre,'edad':edad,'direccion':direccion,'telefono':telefono}
print(f'{nombre} tiene {edad} años, vive en {direccion} y su telefono es {telefono}') #imprimo de la forma simple
#imprimo recorriendo el diccionario persona --> 
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en',persona['direccion'],'y su telefono es',persona['telefono'])