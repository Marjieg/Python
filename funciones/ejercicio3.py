"""Escribir una función que reciba un número entero positivo y 
devuelva su factorial."""

def factorial():
    n = int(input('introduce un número entero positivo : '))
    f = 1
    i = 1
    while (i <= n):
     f = f * i
     i = i + 1
    return f

print(factorial())