# Escribir un programa que realice la siguiente operación aritmética

print(((3 + 2) / (2*5)) ** 2)

calculo = ((3+2) / (2*5)) **2
print(calculo)


#el número despues de la coma es el número al cual se va a elevar
calculo = pow(5, 2)

calculo = pow(((3+2) / (5 * 2)),2)
print(calculo)


'''Una jugueteria tiene mucho éxito en dos de sus productos: payasos y munñecas. Suele hacer venta por correo y la empresa de logistica 
les cobra por peso de cada paquete, así que deben de calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 
112 g y cada muñeca 75 g. Un cliente fecuente pide la cantidad de 23 payasos y 54 muñecas. Realiza un progrma que muestre el peso total
de toda la venta

23 payasos 112g
54 muñecas 75 g'''

peso_payaso = 112
peso_muñeca = 75
cantidad_payasos = 23
cantidad_muñecas = 54

print("el peso total es", ((peso_payaso * cantidad_payasos) + (peso_muñeca * cantidad_muñecas)))
