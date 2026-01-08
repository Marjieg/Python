"""Ejercicio 13
Escribir un programa que pregunte por una muestra de números, separados por
comas, los guarde en una lista y muestre por pantalla su media y desviación típica."""



num = input ("escribe una lista de números separados por una coma")
num = num.split(',')
n = len(num)


for i in range(n):
    num[i] = int(num[i])
num = tuple(num)

#tengo que hallar las diferencias al cuadrado respecto a la media
#sumar las diferencias obtenidas y entonces la desviacion será la raiz cuadrada de
#calculo la desv poblacional (no hago lo de -1)
suma = 0
for i in num:
    suma += i
media = suma / n

sumadiferencias = 0
for i in num:
    sumadiferencias += (i - media)** 2
s = (sumadiferencias/n)**(1/2)  #nota: elevar a 0.5 es lo mismo que sacar la raiz cuadrada
print(f'la media es {media} y la desviación típica es {s}')