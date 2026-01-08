"""Ejercicio 4
Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
a mayor."""

loteria= []
for i in range(6):
    i = input("dime un número para la loteria")
    loteria.append(i) #con esto añado los numeros que me da el usu a la lista
loteria.sort() #con esto ordeno los numero de menor a mayor
print(f'los numeros ganadores son {loteria}')

