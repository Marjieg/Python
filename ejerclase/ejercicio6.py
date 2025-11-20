#

baseexp=int(input('introduce un número : '))
exp=int(input('introduce un exponente : '))
contador=1
for i in range(exp):
    contador=baseexp*contador
print(f'{contador}')