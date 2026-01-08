"""Ejercicio 7
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista
resultante"""

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(alfabeto),1,-1): #haz el bucle empezando en el total del alfabeto(osea empiezo desde atrás hacía adelante), para en 1 y da saltos en -1
    if i % 3 == 0: #si la letra ocupa un índice divisible entre 3 y que de resto sea 0(múltiplo)
        alfabeto.pop(i-1) #pop() elimina por defecto el último elemento de la lista,pero si se pasa un parametro
        #permite borrar elementos diferentes al último, así que si i es un multiplo de 3, quítalo de la lista
print(alfabeto)

#otra forma

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
resultado = []

for i in range(len(alfabeto)):
    if (i + 1) % 3 != 0:
        resultado.append(alfabeto[i])
print(resultado)