class Cuenta_bancaria():
    def __init__(self):
        self._titular = str(input("Por favor ingrese su nombre: "))
        self._saldo = 0
        print(f"Hola {self._titular} \nSu saldo es: {self._saldo}")
        self._historial = []
        
        while True:
            try:            
                if opcion not in [1, 4]:
                    print("Por favor ingrese un valor válido")
                    continue
                break
            except ValueError:
                    print("Debe ingresar un número valido")
                  

    def movimiento(self):
        self._historial = [f"Depósito inicial de {self.deposito}"]        
        self.deposito = 0
        self.retiro = 0   

        if opcion == 1:
            while True:
                try:
                    self.deposito = int(input("Por favor ingrese el valor a depositar: "))
                    if self.deposito <= 0:
                        print("Por favor ingrese un valor mayor a 0")
                        continue
                    break
                except ValueError:
                    print("Por favor ingrese un valor válido")
        
            print("Su saldo es: ", self._saldo + self.deposito)
            self._historial.append(f"Depósito de {self.deposito}")

        elif opcion == 2:
            while True:
                try:
                    self.retiro =int(input("Por favor ingrese su valor a retirar: "))
                    if self.retiro > self._saldo:
                        print("Saldo insuficiente")
                        continue
                    break
                except ValueError:
                    print("Por favor ingrese un valor válido")

        elif self.retiro == 0:
            print("Por favor ingrese un valor mayor a 0")
            self._historial.append(f"Retiro de {self.retiro}")
        else:
            print("Opción incorrecta")

    def mostrar_historial(self):
        print(f"Historial de movimientos para: {self._titular}: ")
        for movimiento in self._historial:
            print(movimiento)

cuenta_bancaria = Cuenta_bancaria()


while True:
    opcion = int(input("Por favor seleccione una opción: \n1. Depositar \n2. Retirar \n3. Ver historial \n4.Salir \n "))
    if opcion ==1 or opcion == 2:
        cuenta_bancaria.movimiento(opcion)
    elif opcion == 2:
        cuenta_bancaria.movimiento(2)
    elif opcion == 3:
        cuenta_bancaria.mostrar_historial()
        break
    else:
        print("Hasta pronto!")
        break


