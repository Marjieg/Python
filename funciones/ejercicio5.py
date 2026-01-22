"""Escribir una función que calcule el área de un círculo y otra que calcule el volumen
de un cilindro usando la primera función."""

#las funciones las ponemos al principio del código
def area(radio):
    a = (3.141515) * (radio ** 2)
    return a


def volumen(h):
    v = (4*(area(radio)) * h)/3
    return v


# la declaración de variables globales las ponemos juntas debajo
h = int(input('introduce la altura del cilintro: '))
radio = int(input('introduce el radio del círculo: '))

# invocamos a las funciones todas juntas debajo del todo
print (area(radio))
print (f'el volumen de un cilintro con altura {h} y radio {radio} es {volumen(area(radio))}')

