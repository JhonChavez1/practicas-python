'''
Crea una clase llamada Persona que tenga los atributos nombre, edad y ciudad. Método saludar() que imprima: “Hola, me llamo {nombre} y tengo {edad} años
'''

class Persona():
    def __init__(self):
        self.nombre = str(input("Por favor ingrese su nombre: "))
        self.edad = int(input("por favor ingrese su edad: "))
        self.ciudad = str(input("¿De donde eres? "))

    def saludar(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")

persona = Persona()
persona.saludar()