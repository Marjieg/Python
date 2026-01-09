"""Ejercicio 8
Escribir un programa que cree un diccionario de traducción español-inglés. El
usuario introducirá las palabras en español e inglés separadas por dos puntos, y
cada par <palabra>:<traducción> separados por comas. El programa debe
crear un diccionario con las palabras y sus traducciones. Después pedirá una frase
en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra
no está en el diccionario debe dejarla sin traducir"""

dic ={}
continuar = True
while continuar:
    palabra = input('introduce una palabra en español')
    word = input(f'introduce la traducción en inglés de {palabra} :')
    dic[palabra]=word
    continuar = input('¿quieres añadir más informacion (si/no)?') =="si"
frase = input('introduce una frase para traducir')
palabras = frase.split(' ')

resultado= []
for i in palabras:
    if i in dic:
        resultado.append(dic[i])
    else:
        resultado.append(i)
print('traduccion:', ' '.join(resultado))

"""otra forma"""

dic = {}
palabras = input('introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ')
for i in palabras.split(','):
    clave, valor = i.split(':')
    dic[clave] = valor
frase = input ('introduce una frase en español: ')
for i in frase.split():
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(i, end= ' ')