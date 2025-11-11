"""Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas"""

num = int(input("introduce un número entero positivo"))

for i in range(num,0,-1): # inicializo con el número que introduzco hasta que llegue a 0 y voy contando en -1
    print(i, end=", ")