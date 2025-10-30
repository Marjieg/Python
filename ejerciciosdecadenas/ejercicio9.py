#Ejercicio 9
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
#dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 

#fecha = input('Introduzca su fecha de nacimiento dd/mm/aaaa')--> otra forma de hacerlo

#print('Día', fecha[:2])
#print('Mes', fecha[3:5])
#print('Año', fecha[6:])

#con split sería --> (mejor esta forma)

fecha = input('Introduzca su fecha de nacimiento dd/mm/aaaa')
x = fecha.split("/")
print(f"el dia es {x[0]}, el mes es {x[1]} y el año {x[2]}")



#Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un
#solo carácter.
# funciona igual con split