
class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("el objeto", self.marca, "ha sido creado")

    #def __str__(self):
    #    return "El objeto es {}".format(self.marca)

    def __del__(self):
        print("El aobjeto", self.marca, "ha sido destruido")

telefono = FabricaTelefonos("Nokia", "Negro")
print(telefono.marca)
print(telefono)