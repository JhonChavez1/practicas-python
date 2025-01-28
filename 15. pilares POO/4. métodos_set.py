
class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    @property
    def cuenta(self):
        return self._cuenta
    
#   método set para permitir que el usuario modifique un atributo    
    @cuenta.setter
    def cuenta(self, cuenta):
        self._cuenta = cuenta 
    
    @property
    def contador(self):
        return self._contador
    
    @contador.setter
    def contador(self, contador):
        self._contador = contador
    
a = A()
print(a.cuenta)
# modificar el atributo _cuenta
a.cuenta = 20
print(a.cuenta)
print(a.contador)
# módificar el atributo _contador 
a.contador = 10
print(a.contador)
