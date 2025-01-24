
class FabricaTelefonos():
    def __init__(self, marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos =  modelos

telefono = FabricaTelefonos("Alcatel", "Negro", "Azul", "Rojo", zt = 500, zt_pro = 100)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)