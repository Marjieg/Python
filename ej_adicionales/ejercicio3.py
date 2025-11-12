"""Bucles (for, while)
🔹 Nivel básico

Muestra los números del 1 al 10 con un for.

Muestra los números pares del 1 al 20.

Pide un número y muestra su tabla de multiplicar."""

for i in range(1,10):
    print(i)

for j in range(0,20,2):
    print(j)

num = int(input("introduce un número"))
for i in range(1,10):
    multi= num * i
    print(f'{num} x {i} = {multi}')