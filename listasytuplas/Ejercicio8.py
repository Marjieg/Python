"""Ejercicio 8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
palíndromo"""

palabra = input("introduce una palabra")
palabra = list(palabra) #convierto palabra en una lista
palindromo = list(palabra) #convierto palindromo en una lista de palabra
palindromo.reverse() #le doy la vuelta a la palabra


if palabra == palindromo:
    print (f'la palabra {palabra} es un palíndromo')
else:
    print (f'la palabra {palabra} no es palíndroma')