"""Escribir una función que calcule el máximo común divisor de dos números y otra que
calcule el mínimo común múltiplo."""

def mcd(n1,n2):
    r = 0
    while(n2 > 0):
        r = n2
        n2 = n1 % n2
        n1 = r
    return n1

def mcm(n1,n2):
    if n1 > n2:
        greater = n1
    else:
        greater = n2
    while (greater % n1 !=0) or (greater % n2 !=0):
        greater += 1
    return greater


print(mcd(43,58))
print(mcm(43,58))