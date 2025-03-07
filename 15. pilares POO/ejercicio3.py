'''
Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. 
Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno
'''
class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

class Moto(Fabrica):
    def datos(self):
        print("el número de llantas de la moto son", self.llantas) 
        print("El color de la moto es", self.color)
        print("El precio de la moto es $",self.precio)

class Carro(Fabrica):
    def datos(self):
        print("El número de llantas del carro son", self.llantas) 
        print("El color del carro es", self.color) 
        print("El precio del carro es $", self.precio)


carro = Carro(4, "azul", 50000000)
carro.datos()

moto = Moto(2, "Verde", 4500000)
moto.datos()





