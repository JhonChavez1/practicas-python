'''Atributos: titular (nombre) y saldo.
Métodos: depositar(monto), retirar(monto), mostrar_saldo().'''

class Cuenta_bancaria():
    def __init__(self):
        self.titular = str(input("Por favor ingrese su nombre: "))
        self.saldo = 3556030
        print(f"Hola, {self.titular}, su saldo es: {self.saldo}")
        
    def movimiento(self):
        self.opcion = int(input("Si desea depositar ingrese la opción 1, si desea retirar ingrese la opción 2: "))
        if self.opcion == 1:
            self.monto = int(input("Por favor ingrese su monto a depositar: "))
            print("Su saldo es:", self.saldo + self.monto)
        elif self.opcion == 2:
            self.monto = int(input("Por favor ingrese su monto a retirar: "))
            print("Su saldo a retirar es: ",self.monto,"\n Su saldo restante es: ",self.saldo - self.monto)
        else:
            print("Opción incorrecta")

cuenta_bancaria = Cuenta_bancaria()
cuenta_bancaria.movimiento()

        