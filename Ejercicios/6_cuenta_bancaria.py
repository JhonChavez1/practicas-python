class Cuenta_bancaria():
    def __init__(self):
        self._titular = str(input("Por favor ingrese su nombre: "))
        self._saldo = 0
        self._historial = []
        print(f"Hola {self._titular} \nSu saldo es: {self._saldo}")       
                  
    def movimiento(self, opcion):
        if opcion == 1: # Depositar
            while True:
                try:
                    deposito = int(input("Por favor ingrese el valor a depositar: "))
                    if deposito <= 0:
                        print("Por favor ingrese un valor mayor a 0")
                        continue
                    break
                except ValueError:
                    print("Por favor ingrese un valor válido")

            self._saldo += deposito
            self._historial.append(f"Depósito de ${deposito}")                  
            print("Depósito exitoso")
            print("Su saldo es: ", self._saldo)

        elif opcion == 2: # Retirar
            while True:
                try:
                    retiro = int(input("Por favor ingrese su valor a retirar: "))
                    if retiro <= 0:
                        print("Por favor ingrese un valor mayor a 0")
                        continue
                    if retiro > self._saldo:
                        print("Saldo insuficiente")
                        continue
                    break
                except ValueError:
                    print("Por favor ingrese un valor válido")

            self._saldo -= retiro
            self._historial.append(f"Retiro de ${retiro}")
            print(f"Retiro exitoso \nSaldo actual: ${self._saldo}")

        elif self.retiro == 0:
            print("Por favor ingrese un valor mayor a 0")
            self._historial.append(f"Retiro de {self.retiro}")
        else:
            print("Opción incorrecta")

    def mostrar_historial(self):
        print(f"Historial de movimientos para: {self._titular}: ")
        if not self._historial:
            print("No hay movimientos registrados.")
        for movimiento in self._historial:
            print(movimiento)

cuenta_bancaria = Cuenta_bancaria()


while True:
    try:
        opcion = int(input("Por favor seleccione una opción: \n1. Depositar \n2. Retirar \n3. Ver historial \n4.Salir \n "))
        if opcion in [1, 2]:
            cuenta_bancaria.movimiento(opcion)
        elif opcion == 3:
            cuenta_bancaria.mostrar_historial()
        elif opcion == 4:
            print("Hasta pronto!")
            break
        else:
            print("Opción no valida, intente de nuevo")
    except ValueError:
                print("Por favor ingrese un número válido")



