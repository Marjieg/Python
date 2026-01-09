"""Ejercicio 10
Escribir un programa que permita gestionar la base de datos de clientes de una
empresa. Los clientes se guardarán en un diccionario en el que la clave de cada
cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre,
dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se
trata de un cliente preferente. El programa debe preguntar al usuario por una opción
del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4)
Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la
opción elegida el programa tendrá que hacer lo siguiente:
1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a
la base de datos.
2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
3. Preguntar por el NIF del cliente y mostrar sus datos.
4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y
nombre.
6. Terminar el programa."""

clientes = {}
opciones = ''

while opciones != '6':
    if opciones == '1':
        nif = input ('Introduzca el nif del cliente: ')
        nombre = input ('Introduzca el nombre del cliente: ')
        direccion = input ('Introduzca la dirección del cliente: ')
        telefono = input ('Introduzca el teléfono del cliente: ')
        email = input ('Introduzca el email del cliente: ')
        vip = input ('¿Es un cliente preferente (si/no)? ') 
        cliente = {'nombre':nombre,'direccion':direccion,'telefono':telefono,'email':email,'vip':vip}
        clientes[nif]=cliente
    elif opciones == '2':
        nif = input ('introduzca el nif del cliente: ')
        if nif in clientes:
            del clientes[nif]
        else:
            print('No existe ningún cliente con ese nif')
    elif opciones == '3':
        nif = input ('introduzca el nif del cliente')
        if nif in clientes:
            print('NIF:',nif)
            for clave, valor in clientes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe ningún cliente con ese nif', nif)
    elif opciones == '4':
        print('lista de clientes:')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    elif opciones == '5':
        print('lista de clientes preferentes:')
        for datos, clientes in clientes.items():    
            if valor['preferente']:
                 print(clave, valor['nombre'])
    else:
        print ('saliendo de la base de datos')
    opciones = input('Escoja una de las siguientes opciones: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4)Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar')