"""Nivel básico

Pide al usuario su nombre y muéstralo todo en mayúsculas.


Pide una frase y muestra cuántas letras tiene (sin contar espacios).

Pide una palabra y muéstrala al revés.
"""

nombre = input("introduce tu nombre")
print (nombre.upper())

frase = input("introduce una frase")
sin_espacios = frase.replace(" ","")
print (len(sin_espacios))

palabra = input("introduce una palabra")
print (palabra[::-1])

