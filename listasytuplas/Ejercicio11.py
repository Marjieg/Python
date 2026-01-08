"""Ejercicio 11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y
muestre por pantalla su producto escalar"""

v1 = (1,2,3)
v2 = (-1,0,2)
producto = 0
for i in range(len(v1)):
    producto += v1[i]*v2[i]
print(f'el producto escalar de los vectores es {producto}')

#otra forma 

v1 = (1,2,3)
v2 = (-1,0,2)

producto = v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]
print(producto)