#Ejercicio 3
#Escribir un programa que pida al usuario dos números y muestre por pantalla su
#división. Si el divisor es cero el programa debe mostrar un error.

numero1 = float(input('escribe un número'))
numero2 = float(input('escribe otro número'))
division = numero1 / numero2
resto = numero1 % numero2

if numero2 == 0:
     print ("error")
else:
    print (f"el resultado de la división es {division},y el resto es, {resto}")