"""Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por
comas."""

num = int(input("introduce un número entero positivo"))
 

for i in range(1, num+1):
    if i % 2 != 0: #si el resto de dividir i entre 2 es distinto de 0, es un número primo
        print(i, end=", ") # por lo tanto, imprime i



