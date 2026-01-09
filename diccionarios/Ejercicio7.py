"""Ejercicio 7
Escribir un programa que cree un diccionario simulando una cesta de la compra. El
programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta
que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la
compra y el coste total, con el siguiente formato
Lista de la compra
Artículo 1 Precio
Artículo 2 Precio
Artículo 3 Precio
… …
Total Coste"""

cesta = {}
continuar = True
while continuar:
    producto = input('¿qué producto quieres comprar?')
    valor = float(input(f'introduce el precio de {producto} ": "'))
    cesta[producto] = valor
    continuar = input('¿quieres añadir más informacion (si/no)?') =="si"
total= 0
print ('Lista de la compra')
for item, valor in cesta.items(): #el método items() devuelve una lista con los keys y values del diccionario
    print (f'{item}  {valor}')
    total += valor
print (f'coste total {total}')
