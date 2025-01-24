while True:
    try:
        num = int(input("Por favor ingrese un número: "))
        resultado = 100 / num
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre cero")


while True:
    try:
        edad = int(input("Por favor ingrese su edad: "))
        print("Tu edad es: ", edad)
        break
    except ValueError:
        print("Has colocado un valor erroneo")


while True:
    try:
        edad2 = int(input("Por favor ingrese su edad: "))
        print("Tu edad es: ", edad2)
        break
    except KeyboardInterrupt:
        print("\nHas cancelado la ejecución")
        break