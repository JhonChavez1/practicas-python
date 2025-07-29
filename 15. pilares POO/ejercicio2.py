
'''
    Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
    Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos.
    Llamar a la clase Calculadora.
    
    class Calculadora():
        def __init__(self, valor1, valor2):
            self.valor1 = valor1
            self.valor2 = valor2

        def operaciones(self, suma, resta, division, multiplicacion):
            self.suma = valor1 + valor2
            self.resta = valor1 - valor2
            self.division = valor1 / valor2
            self.multiplicacion = valor1 * valor2

            return suma, resta, multiplicacion, division
            
    
        print("El resultado de la suma es: ", suma)
        print("El resultado de la resta es: ", resta)
        print("El resultado de la multiplicacion es: ", multiplicacion)
        print("el resultado de la division es: ", division)

            

        def resta(self):
            resta = self.valor1 + self.valor2
            print("El resultado de la resta es: ", resta)

        def multiplicacion(self):
            multiplicacion = self.valor1 * self.valor2
            print("El resultado de la multiplicacion es: ", multiplicacion)

        def division(self):
            division = self.valor1 / self.valor2 
            print("el resultado de la division es: ", division)
 

    valor1 = int(input("Por favor ingrese el primer valor: "))
    valor2 = int(input("Por favor ingrese el segundo valor: "))
    calculadora = Calculadora(valor1, valor2)
    calculadora.operaciones()


 
    calculadora.suma()
    calculadora.resta()
    calculadora.multiplicacion()
    calculadora.division()

'''

# solución del curso

class Calculadora():
     def __init__(self):
          self.num1 = int(input("Por favor ingrese un número: "))
          self.num2 = int(input("Por favor ingrese un número: "))

     def suma(self):
          self.suma = self.num1 + self.num2
          print("El resultado de la suma es: ", self.suma)
     
     def resta(self):
          self.resta = self.num1 - self.num2
          print("El resultado de la resta es: ", self.resta)
     
     def multiplicacion(self):
          self.multiplicacion = self.num1 * self.num2
          print("El resultado de la multipliciación es: ", self.multiplicacion)
     
     def division(self):
          self.division = self.num1 / self.num2
          print("El resultado de la división es: ", self.division)
     
calculadora = Calculadora()
calculadora.suma()
calculadora.resta()
calculadora.multiplicacion()
calculadora.division()
