#Ejercicio 4
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si
#es par o impar

numero = int(input('escribe un número entero'))

resto = int(numero % 2)
if (numero >= 2 and resto == 0):
    print (f'{numero} es entero')
else:
    print (f'{numero} es impar')   
