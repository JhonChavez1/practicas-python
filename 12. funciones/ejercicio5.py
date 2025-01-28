'''
Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; 
y la otra el area de un circulo con argumento de radio
'''

def cuadrado(base, altura):
    area = base * altura
    return area

def circulo(radio):
    area = 3.14 * (radio ** 2)
    return area
#   return pow(radio, 2) * 3.14

print("El area del cuadrado es: ", cuadrado(10, 5), "cm")
print("El area del circulo es: ", circulo(10), "cm")
