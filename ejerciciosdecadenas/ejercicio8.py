#ejercicio 8.Escribir un programa que pregunte por consola el precio de un producto en euros
#con dos decimales y muestre por pantalla el número de euros y el número de
#céntimos del precio introducido.

precio = input("Introduce el precio del producto con dos decimales:  ")
x = precio.split(",")

print (f"{x[0]} euros y {x[1]} centimos")