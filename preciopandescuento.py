#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
#un descuento del 60%. Escribir un programa que comience leyendo el número de
#barras vendidas que no son del día. Después el programa debe mostrar el precio
#habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
#coste final total.

precio_barra = float(3.49)
pandiaanterior = float(precio_barra * 0.40)
c_barras_vendidasdehoy = int(43)
c_barras_vendidasdeayer = int(20)
coste_final_total = int(precio_barra * c_barras_vendidasdehoy)+(pandiaanterior * c_barras_vendidasdeayer)

print('el precio de la barra de pan fresca es', precio_barra, 'el precio de la barra de pan de ayer es',pandiaanterior)
print('el coste total es', coste_final_total)