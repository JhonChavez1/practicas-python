class Cuenta_bancaria():
    def __init__(self):
        self._titular = str(input("Por favor ingrese su nombre: "))
        self.deposito_inicial = int(input(f"Hola {self._titular} \nsu saldo es: 0 \nPor favor ingrese su valor a despositar: "))
        self._saldo = self.deposito_inicial
        print(f"Su saldo es: {self._saldo}")  
        self._historial = [f"Depósito inicial de {self.deposito_inicial}"]  

    def movimiento(self):
        self.opcion = int(input("Si desea depositar ingrese la opción 1, si desea retirar ingrese la opción 2: "))   
        self.deposito = 0
        self.retiro = 0   

        if self.opcion == 1:
            self.deposito = int(input("Por favor ingrese el valor a depositar: "))
            if self.deposito <= 0:
                print("Por favor ingrese un valor mayor a 0")
                
            print("Su saldo es: ", self._saldo + self.deposito)
            self._historial.append(f"Depósito de {self.deposito}")

        elif self.opcion == 2:
            self.retiro =int(input("Por favor ingrese su valor a retirar: "))
            if self.retiro > self._saldo:
                print("Saldo insuficiente")
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
cuenta_bancaria.movimiento()
cuenta_bancaria.movimiento
cuenta_bancaria.mostrar_historial()

