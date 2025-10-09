#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
#interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
#año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que
#comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
#introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
#la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada
#cantidad a dos decimales.

i = float(4 / 100)
a = float(input('introduce tus ahorros'))


cantidad_ahorros1 = (i * a)
cantidad_ahorros2 = (i * a) + (cantidad_ahorros1)
cantidad_ahorros3 = (i * a) + (cantidad_ahorros2)

print('la cantidad de ahorro obtenido el primer año es: {:.2f} '.format(cantidad_ahorros1),'el segundo año es: {:.2f} '.format(cantidad_ahorros2),'y el tercer año es: {:.2f} '.format(cantidad_ahorros3))