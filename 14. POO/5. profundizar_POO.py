
class FabricaTelefonos():
#                      atributo, tupla, diccionario
    def __init__(self, marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos =  modelos

#                           atributo    tupla                   diccionario
telefono = FabricaTelefonos("Alcatel", "Negro", "Azul", "Rojo", zt = 500, zt_pro = 100)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
# crear un atributo temporal
telefono.memoria = 512
print(telefono.memoria)