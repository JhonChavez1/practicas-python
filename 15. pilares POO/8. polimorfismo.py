
class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

# modificar el método hablar de la clase Animales
class Perro(Animales):
    def hablar(self):
        print("yo hago guao")

# modiificar el método hablar de la clase Animales 
class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")

# creamos el objeto llamado perro a partir de la clase Perro 

perro = Perro("Guao")
perro.hablar()

animal = Animales("Miau!")
animal.hablar()

pez = Pez("Nada")
pez.hablar()




            