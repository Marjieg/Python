"""Escribir una función que calcule el área de un círculo y otra que calcule el volumen
de un cilindro usando la primera función."""

radio = int(input('introduce el radio del círculo: '))
def area():
    a = (3.141515) * (radio ** 2)
    return a
print (area())

h = int(input('introduce la altura del cilintro: '))
def volumen():
    v = (4*(area()) * h)/3
    return v
print (f'el volumen de un cilintro con altura {h} y radio {radio} es {volumen()}')

