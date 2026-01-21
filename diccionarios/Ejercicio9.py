"""Ejercicio 9
Escribir un programa que gestione las facturas pendientes de cobro de una
empresa. Las facturas se almacenarán en un diccionario donde la clave de cada
factura será el número de factura y el valor el coste de la factura. El programa debe
preguntar al usuario si quiere añadir una nueva factura, pagar una existente o
terminar. Si desea añadir una nueva factura se preguntará por el número de factura
y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará
por el número de factura y se eliminará del diccionario. Después de cada operación
el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la
cantidad pendiente de cobro"""

facturas = {}
pendiente = 0
cobrado= 0
accion = ''
while accion != 'terminar':
    accion = input('qué desea hacer añadir una nueva factura, pagar una existente o terminar')
    if accion == 'nueva factura':
        clave = input('introduzca el número de factura : ')
        valor = float(input('introduzca el coste'))
        facturas[clave]= valor
        pendiente += valor

    if accion == 'pagar':
        clave = input('introduzca el número de factura : ')
        valor = facturas.pop(clave, 0)  #le digo que elimine la factura que he introducido en clave
        cobrado += valor
        pendiente -= valor
    print('pagado:', cobrado)
    print('pendiente de pagar:', pendiente)
