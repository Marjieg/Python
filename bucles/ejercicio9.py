"""Ejercicio 9 Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""

contrausu = input('introduce una contraseña')
contra = ("manzana")
while (contrausu != contra):
    print("contraseña incorrecta")
    break
else:
    print("contraseña correcta")