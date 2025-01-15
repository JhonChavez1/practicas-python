'''
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%
'''
'''
def calcular_iva():
    valor_factura = float(input("Por favor ingrese el valor de la factura: "))
    valor_iva = int(input("Por favor ingresa el valor del IVA: "))
    if valor_iva >0:
        factura_iva = valor_factura * valor_iva / 100
        return valor_factura + factura_iva
    else:
        factura_sin_iva = valor_factura * 21 / 100
        return valor_factura + factura_sin_iva

print((calcular_iva()))

# solución del curso 
'''
def calcular_iva2():
    monto = float(input("Ingresa el valor del producto que estamos pagando: "))
    iva = int(input("Ingresa el valor del iva: "))

    if iva != 0:
        if iva > 0:
            total_pagar = ((monto * iva) / 100) + monto
            return total_pagar

        else:
            return "El valor de IVA es negativo"

    else:
        total_pagar = (monto * 0.21) + monto
        return total_pagar
    
print("El total de su monto es: ", calcular_iva2())
