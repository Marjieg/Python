"""Ejercicio 9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el
número de veces que contiene cada vocal."""

palabra = input("introduce una palabra")
vocales = ["a","e","i","o","u"]

for vocal in vocales:
    veces = 0
    for p in palabra:
        if p == vocal:
            veces +=1
    print(f'la vocal {vocal} aparece {veces} en la palabra {palabra}')


