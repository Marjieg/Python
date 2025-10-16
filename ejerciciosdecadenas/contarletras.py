#Ejercicio 3
#Escribir un programa que pregunte el nombre del usuario en la consola y después
#de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n>
#letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el
#número de letras que tienen el nombre.



nombre = input('¿nombre?')

# Convertir el nombre a mayúsculas
nombre_mayusculas = nombre.upper()

# Obtener la cantidad de letras
numero_letras = len(nombre)

# Mostrar el resultado por pantalla
print(f"{nombre_mayusculas} tiene {numero_letras} letras")