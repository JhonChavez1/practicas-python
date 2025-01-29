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
    def str(self):
        return "el número de llantas son: ", self.llantas, "\ncolor: ", self.color, "\nPrecio: ", self.precio

class Carro(Fabrica):
    def str(self):
        return "El número de llantas son: ", self.llantas, "\ncolor: ", self.color, "\nPrecio: ", self.precio


carro = Carro(4, "azul", 5000000)
print(carro)

moto = Moto(2, "Verde", 45000000)
print(moto)



