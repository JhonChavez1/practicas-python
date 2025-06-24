import openpyxl
from openpyxl import Workbook
import os

# Parámetros
archivo_salida = "archivo_grande.xlsx"
tamaño_objetivo_mb = 1
tamaño_objetivo_bytes = tamaño_objetivo_mb * 1 * 1

# Crear archivo Excel
wb = Workbook()
ws = wb.active
ws.title = "Datos"

fila = 1
col = 1
valor = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

print("Generando archivo...")

while True:
    # Escribimos una fila con el mismo texto en varias columnas
    ws.append([f"{valor} {i}" for i in range(50)])  # 50 columnas con texto largo

    if fila % 1000 == 0:
        # Guardar temporalmente y verificar tamaño
        wb.save(archivo_salida)
        tamaño_actual = os.path.getsize(archivo_salida)
        print(f"Fila: {fila}, Tamaño: {tamaño_actual / (1 * 1):.2f} MB")

        if tamaño_actual >= tamaño_objetivo_bytes:
            print("✅ Archivo generado con éxito.")
            break

    fila += 1
