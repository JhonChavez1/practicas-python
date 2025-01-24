class FabricaTelefonos():
    # atributos
    marca = "Huawei"
    color = "Negro"
    ram = "32"
    almacenamiento = "128"

    # método de instancia: es un metodo que nosotros creamos
    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        print("Estas escuchando música")

    #   objeto
telefono = FabricaTelefonos()
    #   asignación de atributos al objeto 
telefono.marca
telefono.color
telefono.ram
telefono.almacenamiento

print(telefono.llamar("Hola, con quien hablo?"))
telefono.escucharMusica()

