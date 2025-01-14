# La función rango se utiliza par establecer un rango donde el iterador va recorrer
# con el range hace el incremento automaticamente al iterador
for i in range(1, 10):
    print(i)

# el último número del rango equivale a que el iterador va a ir de dos en dos
for i in range(1, 11, 2):
    print(i)

# con los números negativos hay que tener en cuenta que el iterador empieza desde 0 
for i in range(-10, -1):
    print(i)