#con un bucle for hacer que el usu introduzca 10 numero y que la salida muestre la suma total

num=int(input('di un número'))
sum = num
mayor = num
menor = num
for i in range(1,6):
#una vuelta i=1
#dos vueltas i=2
#tres vueltas i=3
    num = int(input('introduce un número'))
    sum += num
    if mayor < num:
        mayor = num
    if menor > num:
        menor = num
print(f'la suma total es de {sum}')
print(f'el número mayor es{mayor}')
print(f'el número menor es {menor}')