
"""🔹 Nivel avanzado

Dibuja un triángulo de asteriscos según el número de filas introducido:
*
**
***
****
Pide una palabra y construye una pirámide:
"""


num = int(input("introduce un numero"))

for i in range(1,num,2):
    for j in range (i,1,-2):
        print(" ",end="*")
    print(" ")

palabra =input("introduce una palabra")

for i in range(1,len(palabra)+1):
    print(i)