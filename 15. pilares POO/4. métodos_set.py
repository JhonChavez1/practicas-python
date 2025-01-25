
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
    
a = A()
print(a.cuenta)
a.cuenta = 20
print(a.cuenta)
print(a.contador)