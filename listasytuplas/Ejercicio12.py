"""Ejercicio 12
Escribir un programa que almacene las matrices en una lista y muestre por pantalla
su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando
cada vector fila en una lista.
A= (1 2 3)  B= (-1 0)
   (4 5 6)       0 1
                 1 1)     """

a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],  #el producto es filas por columnas será el resultado de una matriz de n filas por m columnas
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])

"""otra forma"""

a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))

producto = producto = (
    (
        a[0][0]*b[0][0] + a[0][1]*b[1][0] + a[0][2]*b[2][0],
        a[0][0]*b[0][1] + a[0][1]*b[1][1] + a[0][2]*b[2][1]
    ),
    (
        a[1][0]*b[0][0] + a[1][1]*b[1][0] + a[1][2]*b[2][0],
        a[1][0]*b[0][1] + a[1][1]*b[1][1] + a[1][2]*b[2][1]
    )
)

print(producto)

