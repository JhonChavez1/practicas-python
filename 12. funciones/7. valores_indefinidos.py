def argumento(num):
    return type(num)

print(argumento(56.562))

# cuando no sabemos la cantidad de valores que vamos a ingresar podemos recurrir al parametro con un * y será aalmacenado como una tupla 

def argumento2(*num):
    return type(num)

print(argumento2(1, 2, 3, 4))

# otra forma utilizanod el for

def argumento3(*num):
    for i in num:
        print(i)

print(argumento3(1, 2, 3, 4, 5, 6, 7))