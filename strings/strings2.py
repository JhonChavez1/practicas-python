cadena1 = "Hola Jhon"
cadena2 = "Chavez"
numero = 1

# concatenación suma de dos cadenas
print(cadena1 + cadena2)
print(cadena2 * 5)
print("Hola usuario: " + cadena2)
# se puede utilizar el la , en vez de el signo +
print("hola usuario: " , cadena2)
print(numero ,"hola usuario:" ,cadena2)
print(numero, "hola usuario: ", cadena2)

# la función str nos sirve para cnovertir un número a string
print(type(str(numero)))

#debanado de cadenas = sustrings
cadena3 = "este es un ejemplo de substring (debanado de cadenas)"
# metodo llamado (len) sirve para devolver el tamaño de una cadena
print(len(cadena3))

# mostrar el el caracter número 2, empezando desde 0, tambien tiene en cuenta los espacios
print(cadena3[2])
# mostrar un rango de caracteres, por ejemplo del 0 al 11. Pero el caracter de la derecha no es tomado encuenta
print(cadena3[0 : 11])
# mostrar desde el principio hasta el número de caracter que escoja
print(cadena3 [ :20])
# mostrar desde cierto número de caracter hasta el último
print(cadena3 [20: ])
