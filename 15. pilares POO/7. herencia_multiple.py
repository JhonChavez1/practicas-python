
class A():
    def primera(self):
        return "Estas es la clase A"
    
class B():
    def segunda(selF):
        return "Esta es la clase B"
    
# la clase C va a ser la herencia de la clase A y B.
#       debemos  colocar las class que van a heredar       
class C(A, B):
    pass

c = C()
print(c.primera())
print(c.segunda())
