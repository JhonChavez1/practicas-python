nombre = input("ingresas tu nombre: ")
edad = int(input("ingresa tu edad: "))

# mostrar datos de concatenación 
print(nombre, edad)
print("Hola ", nombre, "tu edad es de ",edad, "años")

# imprimiendo con el format
# el primer corchete hace referencia a la primera variable que tenemos en el format
# el segundo corchete hace referencia a la segunda variable que tenemos en el format
print("Hola {} tienes {}".format(nombre, edad))

print(nombre)
print(edad)