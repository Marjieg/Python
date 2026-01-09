"""Ejercicio 3
Escribir un programa que guarde en un diccionario los precios de las frutas de la
tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe
mostrar un mensaje informando de ello.
Fruta Precio
Plátano 1.35
Manzana 0.80
Pera 0.85
Naranja 0.70"""

frutas = {'Plátano':1.35,'Manzana':0.80,'Pera':0.85,'Naranja':0.70}
fruta= input('¿qué fruta quieres?')
kilos= float(input('¿cuántos kg quieres?'))
if fruta in frutas: #esto es para comprobar que fruta está 
    print (f'el precio del kg de {fruta} es {frutas[fruta]}')
    total= kilos * (frutas[fruta])
    print (f'el precio total es de {total} euros')
else: #si la fruta introducida no está
    print(f'{fruta} no está disponible')