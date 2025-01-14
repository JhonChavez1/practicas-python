
# el break se combina con un if
# detenerse en un valor

for i in range(1, 11):
    print(i)
    if i == 5:
        break

# omitir un dato 
# a diferencia del range primero va la condición luego se imprime
for i in range(1, 10):
    if i == 6:
        continue
    print(i)