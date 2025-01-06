#Crear un programa que pida al usuario una letra, y si es vocal muetre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

letra = input("Por favor ingrese una letra: ")

if letra.lower() == "a":
    print("Es vocal")
elif letra.lower() == "e":
    print("Es vocal")
elif letra.lower() == "i":
    print("Es vocal")
elif letra.lower() == "o":
    print("Es vocal")
elif letra.lower() == "u":
    print("Es vocal")
else:
    print("No es vocal")


# solución mas correcta

letra1 = input("Por favor ingrese una letra: ")

if letra1.lower() in "aeiou":
    print("Es una vocal")
else:
    print("No es una vocal")
