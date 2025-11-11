"""Ejercicio 10 Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no."""

num = int(input("introduce un número entero"))

while (num % 2 != 0):
    print("has introducido un número primo")
    break
else:
    print("has introducido un número no primo")