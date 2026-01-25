"""Escribir una función que convierta un número decimal en binario y otra que convierta
un número binario en decimal."""

def binario(n):
    if n == 0:
        return "0"
    bits = []    #aqui guardo los 0 y 1 del n binario
    while n > 0:
        # le digo que el resto de dividir n/2 si es 0, el bit es 0, si 1, el bit es 1
        bits.append(str(n % 2)) # ese bit resultante se convierte a str y se agrega al final de la lista
        n //= 2 #divide n entre 2 usando division entera y guarda el resultado en n
    bits.reverse()
    return ''.join(bits) #como los bits se obtienen al reves, esta linea invierte la lista

def decimal(n):
    n = list(n)
    n.reverse()
    dec = 0
    for i in range(len(n)):
        dec += int(n[i]) * 2 ** i
    return dec

print (binario(23))
print (decimal('101011'))