import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Progressbar")
ventana.geometry("500x500")

# Simular la barra de progreso
# mode = es la forma en la que se va a ejecutar la barra cuando se esté ejecutando
barra_progreso = ttk.Progressbar(ventana, mode= "determinate", length= 200)
barra_progreso.pack()

def iniciar_progreso():
# convertir la barra de progreso en una lista
    barra_progreso["value"] = 0
# actualizar la ventana
    ventana.update()

    for i in range(101):
        barra_progreso["value"] = i
        ventana.update()
# Tiempo en cada actualización por milisengundos
        ventana.after(500)

boton = tk.Button(ventana, text= "Iniciar progreso", command= iniciar_progreso)
boton.pack()

ventana.mainloop()