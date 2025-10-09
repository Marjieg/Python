#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
#paquete así que deben calcular el peso de los payasos y muñecas que saldrán en
#cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un
#programa que lea el número de payasos y muñecas vendidos en el último pedido y
#calcule el peso total del paquete que será enviado.

p_payasos =int(112)
p_muñecas =int(75)
c_payasos =int(23)
c_muñecas =int(15)

pedido = (p_payasos * c_payasos)+(p_muñecas * c_muñecas)

print ('el peso total del paquete que será enviado es de',(pedido),'gramos')