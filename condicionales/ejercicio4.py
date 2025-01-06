'''
Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, 
candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje 
“Usted ha votado por el partido [color que corresponda al candidato elegido]”.
 Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar
“Opción errónea”.

Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula
'''

rojo = "usted ha votado por el candidato del partido rojo"
verde = "usted ha votado por el candidato del partido verde"
azul = "usted ha votado por el candidato del partido azul"
candidato = input("Por favor ingrese elige tu candidato por el cúal deseas votar A, B ó C: ")

if candidato.upper() == "A":
    print(rojo)
elif candidato.upper() == "B":
    print(verde)
elif candidato.upper() == "C":
    print(azul)
else:
    print("Opción errónea")


#una forma más simple para no utilizar tantas variables

candidato1 = input("Por favor ingrese elige tu candidato por el cúal deseas votar A, B ó C: ")

if candidato1.upper() == "A":
    print("usted ha votado por el candidato del partido rojo")
elif candidato1.upper() == "B":
    print("usted ha votado por el candidato del partido verde")
elif candidato1.upper() == "C":
    print("usted ha votado por el candidato del partido azul")
else:
    print("Opción errónea")


