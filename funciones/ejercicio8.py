"""Escribir una función que reciba una muestra de números en una lista y devuelva un
diccionario con su media, varianza y desviación típica."""
def cuadrados(lista):
    c = []
    for i in lista:
        c.append(i**2)
    return c


def dic(lista):
    d = {}
    d['media'] = sum(lista) / len(lista)
    d['varianza'] = sum(cuadrados(lista))/len(lista)-d['media']**2
    d['desviacion tipica'] = d['varianza']**0.5
    return d

lista = [1,2,4,3,2]

print(dic(lista))