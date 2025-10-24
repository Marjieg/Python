#Ejercicio 2
#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña e imprima por pantalla si la
#contraseña introducida por el usuario coincide con la guardada en la variable sin
#tener en cuenta mayúsculas y minúsculas.

contraseña = input("introduzca la contraseña").lower()
contraseña2 = ('marina')

if contraseña == contraseña2:
    print("contraseña correcta")
else:
    print("contraseña erronea")
