
class FabricaTelefonos():
    marca = "Samsung"

    def ElaborarHuawei(self):
        self.marca = "Huawei"

telefono = FabricaTelefonos()
telefono.ElaborarHuawei()
print(telefono.marca)



class FabricaCarros():
    def __init__(self):
        print("Estoy ejecutando el método init, porqu se ha creado un nuevo objeto")

carro = FabricaCarros()



class FabricaRopa():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

ropa = FabricaRopa("Root + co", "Rojo")
print(ropa.marca)
print(ropa.color)
        