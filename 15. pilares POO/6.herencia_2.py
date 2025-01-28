
class Animales():
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animales):
#   heredando el método init usando el método super
    def __init__(self, nombre, sonido):
#   palabra clave y el método que queremos heredar 
        super().__init__(nombre)
        self.sonido = sonido

perro = Perro("Firulais", "guaoo!")
print(perro.nombre)
print(perro.sonido)