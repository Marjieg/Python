#Escribir un programa que pregunte el correo electrónico del usuario en la consola y
#muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante
#de la arroba @) pero con dominio ceu.es.

correo = input('¿cuál es tu correo electrónico?')

#print(correo[:correo.find('@')] + '@ceu.es') --> esto sería otra forma de hacerlo
#split utiliza cadenas de caracteres los trata 
#como arrays separados por el caracter que le asigne

x = correo.split("@")
nombre = x[0]

print (nombre+"@ceu.es")