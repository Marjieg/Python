"""Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario
con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el
diccionario generado con la función anterior y devuelva una tupla con la palabra más
repetida y su frecuencia."""

def contador(frase):
    frase = frase.split() #convierto la frase en palabras
    palabras = {} #almaceno las palabras en un diccionario
    for i in frase: # si cada palabra i en la frase:
        if i in palabras: # si i está en palabras, suma 1 +
            palabras[i] += 1
        else:
            palabras[i] = 1 # si no está, i es 1      
    return palabras

def mas_repetida(palabras):
    max_frecuencia = 0
    max_palabra = ""
    for palabra, freq in palabras.items():
        if freq > max_frecuencia:
            max_palabra = palabra
            max_frecuencia = freq
    return max_palabra, max_frecuencia

frase = "tres tristes tigres comieron tigro en un trigal, que tigre más triste comió más trigo en el trigal "
print (contador(frase))
print(mas_repetida(contador(frase)))

        
    