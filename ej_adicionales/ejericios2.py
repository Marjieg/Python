"""Nivel medio

Pide una frase y una letra. Muestra cuántas veces aparece esa letra.

Pide una frase y cámbiale todas las vocales por asteriscos (*).

Pide una palabra y di si es un palíndromo (se lee igual al derecho y al revés).
👉 Ejemplo: reconocer → ✅"""

frase = input("dime una frase")
letra = input("dime una letra")

print (frase.count(letra))

frase2 = input("dime una frase")
for vocal in "aeiouAEIOU":
    frase2 = frase2.replace(vocal, "*")
print(frase2)

palabra = input("introduce una palabra a ver si es palíndromo")
if(palabra == palabra[::-1]):
    print("es palindromo!")
else:
    print("no es palindromo")