"""Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
año que dura la inversión."""

cantidad = int(input("¿cuánto deseas invertir?"))
interes = float(input("Ingresa el interés anual en porcentaje"))
anios = int(input("Introduce el número de años"))


#quiero que me muestre año a año como va aumentando el capital

for i in range(anios):
    cantidad = cantidad * (1 + interes / 100) # cantidad = cantidad *, se puede poner cantidad *=
    print(f'Capital tras '+ str(i+1) + ' años: '+ str(round(cantidad,2)))