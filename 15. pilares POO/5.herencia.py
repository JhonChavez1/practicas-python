
class animales():
    def habla(self):
        print("Yo soy un animal")

    def descripcion(self):
        print("Yo soy un ", self.animal)

# la clase perro ha heredado de la clase animales todos los métodos que en la clase animales se almacenan
class perro(animales):
    pass

class Abeja(animales):
    def __init__(self, animal):
        self.animal = animal

# creación de objeto a partir de la clase animales
animal = animales()
animal.habla()

# creación de un objeto a partir de la clase perro
perro = perro()
perro.habla()

# El método descriçion no está dentro de la clase abeja 
abeja = Abeja("Abeja")
abeja.descripcion()

