class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

#   para mandar a llamar al método como si fuera un atributo se utiliza el: @property
    @property
    def cuenta(self):
        return self._cuenta
    
    @property
    def contador(self):
        return self._contador

a = A() 
# llamar al método como un atributo 
print(a.cuenta)
print(a.contador)