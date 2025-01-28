
class A():
    def __init__(self, ):
        self._contador = 0

    def incrementar(self):
        self._contador += 1

    def cuenta(self):
         return self._contador
        
# esto es una mala práctica de programación 

a = A()
# llamar al método 
print(a.cuenta())
# modificar los valores de un atributo
a.cuenta = 20
print(a.cuenta)

