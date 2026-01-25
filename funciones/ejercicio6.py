"""Escribir una función que reciba una muestra de números en una lista y devuelva su
media."""

def media(lista):
    n = int(len(lista))
    sum = 0
    for i in lista: #esto se puede hacer con sum
        sum += i
    m = sum /n
    return m


lista = [1,4,1,1,1]


print (media(lista))


