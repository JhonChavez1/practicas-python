
'''
En la siguiente lista, debes hacer un programa que muestre los valores al usuario,
a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos 
en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]
'''

lista = [20, 50, "Curso", 'Python', 3.14]
print(lista)

dato1 = input("Por favor ingerese el primer dato a modificar: ")
dato2 = input("Por favor ingrese el segundo dato a modificar: ")

lista[0] = dato1
lista[1] = dato2

print(lista)
'''
lista2 = [20, 50, "Curso", 'Python', 3.14]

1 = int(input("Por favor ingerese el primer dato a modificar: "))
2 = int(input("Por favor ingerese el segundo dato a modificar: "))
list.insert[0, 1]
list.insert[1, 2]
print(lista2)
'''