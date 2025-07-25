'''
Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años. 
Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años si cada año se aplica la tasa de interés introducida.
Recordar que un capital C dolares a un interés del x por cien durante n años se convierte en C * (1 + x/100)elevado a n (años). 
Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.
'''

cantidad = int(input("Por favor introduzca el valor en dolares que desea imprimir: "))
tasa_de_interes = float(input("Por favor ingrese la tasa de interes: "))
años = int(input("Por favor ingrese la cantidad de años a la que va a guardar su dinero: "))

print("Total con insteres ganados: ", (cantidad * (1 + tasa_de_interes / 100)) ** años - cantidad)