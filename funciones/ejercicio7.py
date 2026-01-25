"""Escribir una función que reciba una muestra de números en una lista y devuelva otra
lista con sus cuadrados."""
def cuadrados(lista):
    c = []
    for i in lista:
        c.append(i**2)
    return c


lista = [1,2,3,4,5]

print(cuadrados(lista))