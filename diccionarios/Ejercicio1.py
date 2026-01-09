"""Ejercicio 1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su
símbolo o un mensaje de aviso si la divisa no está en el diccionario"""

d1 = {'Euro':'€','Dollar':'$','Yen':'¥'}

divisa = input('Introduce una divisa ')

if divisa == 'Euro':
    print (d1['Euro'])
elif divisa == 'Dollar':
    print (d1['Dollar'])
elif divisa == 'Yen':
    print (d1['Yen'])
else:
    print ('esa divisa no está disponible en el diccionario')

"""otra forma"""

d1 = {'Euro':'€','Dollar':'$','Yen':'¥'}
divisa = input('Introduce una divisa ')
print(d1.get(divisa.title(), "esa divisa no está disponible"))
