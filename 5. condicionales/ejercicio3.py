'''Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.'''

palabra1 = input("Por favor ingrese una palabra: ")
palabra2 = input("Por favor ingrese otra palabra: ")

if len(palabra1) <3 or len(palabra2) <3:
    print("No rima porque tienen menos de 3 letras")
elif palabra1.lower()[-3] == palabra2.lower()[-3]:
    print("Las palabras riman")
elif palabra1.lower()[-2] == palabra2.lower()[-2]:
    print("las palabras riman un poco")
else:
    print("Las palabras no riman")


