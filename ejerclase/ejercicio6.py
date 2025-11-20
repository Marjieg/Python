#

baseexp=int(input('introduce un número : '))
exp=int(input('introduce un exponente : '))
contador=1
for i in range(1,exp+1):
    contador=baseexp*contador
print(f'{contador}')