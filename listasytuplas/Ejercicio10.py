"""Ejercicio 10
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46,
22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios."""

precios = [50, 75, 46, 22, 80, 65, 8]
precios.sort() #los ordeno de menor a mayor
print (precios)
ultimo = precios.pop(len(precios)-1) # elimino el total de la lista menos el último
print (f'el precio máximo es {ultimo}') #me dará el precio mayor (el último de la lista ordenada)
primero = precios[0] #cojo el primer precio que será el más bajo
print (f'el precio minimo es {primero}')

"""otra forma"""

precios = [50, 75, 46, 22, 80, 65, 8]
#inicializo variables
min = max = precios[0]
for precio in precios:
    if precio < min: #si el precio es menor que el min
        min = precio
    elif precio > max:
        max = precio
print(f"El mínimo es {min}")
print(f'el máximo es {max}')