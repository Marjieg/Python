
salir = ''
saldo = float(1000)
while salir != '4':
    print ('1 saldo')
    print ('2 ingreso')
    print ('3 reintegro')
    print ('4 salir')
    salir = input('introduce un número del menú')
    if salir == '1':
            print(f'su saldo actual es de{saldo}')
    elif salir == '2':
            ingreso = float(input('dime cuánto dinero quieres ingresas'))
            total = saldo + ingreso
            print(f'tu saldo todal es de {total}')
    elif salir == '3':
            reintegro = float(input('dime cuanto dinero quieres sacar'))
            treintegro = saldo - reintegro
            print (f'el saldo total es de {treintegro}')
    else:
            print('hasta pronto!')