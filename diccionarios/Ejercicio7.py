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
total = 0
while continuar:
    producto = input('¿qué producto desea añadir a la lista?: ')
    precio = input(f'introduce el precio de {producto :} : ')
    cesta[producto]= precio
    precio = int(precio)
    total += precio
    print('Lista de la compra')
    for producto,precio in cesta.items():
       print(f'{producto} {precio}')
    print(f'el total de la compra es {total}')
    continuar = input('¿desea continuar? si/no : ') == 'si'
