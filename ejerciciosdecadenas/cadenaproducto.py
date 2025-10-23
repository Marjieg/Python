#Ejercicio 11
#Escribir un programa que pregunte el nombre el un producto, su precio y un número
#de unidades y muestre por pantalla una cadena con el nombre del producto seguido
#de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
#tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.


producto = (input('Introduce el nombre del producto: '))
precio = float(input('Introducde el precio unitario: '))
unidades = float(input('Introduce el número de unidades: '))
precio_total = float(precio * unidades)


print(f"el nombre del producto es: {producto}, el precio es: {precio:2f}, el numero de unidades son :{unidades:3f}, en total: {precio_total:2f} euros")




