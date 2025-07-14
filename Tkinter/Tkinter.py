# Imortando toda la libreria
import tkinter as tk



# Metódo Tk que inicializa una ventana
ventana = tk.Tk()
# Titulo a la ventan
ventana.title("Mi primerea aplicación en tkinter")

# Dar tamaño a la ventana
#ventana.geometry("500x500")

# Fijar el tamaño de la ventana (ancho, alto)
ventana.resizable(True, True)


# Agregar un widget 
marco = tk.Frame(ventana, width=150, height=100, bg="lightgray", borderwidth=2, relief="solid")
# False= El tamaño siempre sera fijo
# True = para que el contenido siempre se adapte al tamaño del frame 
marco.pack_propagate(False)
# Posiciona el marco
# pad = dar un espacio en el contorno de la ventana
marco.pack(pady=50, side="left", fill="y")


# LABEL
# Agregar una etiqueta
etiqueta = tk.Label(ventana, text="Hola, bienvenidos a tkinter!")
# Posicioner la etiqueta
etiqueta.pack(side="top")

etiqueta2 = tk.Label(ventana, text="Este es un segundo Label")
etiqueta2.pack()

etiqueta.config(text= "Funcionalidades: ")

botones= tk.Label(ventana, text="Botones:")
botones.pack()


# Button
# Agregar un botón
boton = tk.Button(ventana, text="Esto es un botón")
boton.pack()

def cambiar_texto():
# config = modifica al botón o widge
    mensaje_cambiante.config(text= "Texto cambiado")

def restablecer_texto():
    mensaje_cambiante.config(text="Mensaje original")
    
mensaje_cambiante = tk.Label(ventana, text= "Texto original")
mensaje_cambiante.pack()

boton1 = tk.Button(ventana, text= "Cambiar texto", command= cambiar_texto)
boton1.pack()

boton2 = tk.Button(ventana, text= "Testablecer texto", command = restablecer_texto)
boton2.pack()

# Personalizar una etiqueta
texto_personalizado = tk.Label(
    ventana, 
    text ="Bienvenidos a tkinter", 
    bg = "lightblue", 
    fg = "darkblue",
    width = 50,
    height = 1,
    font =("Arial", 24, "italic")
)
texto_personalizado.pack(pady= 10)

# Modifica la etiqueta llamada texto personalizado al presionar el botón personalizado
def accion_boton():
    texto_personalizado.config(text = "Botón presionado", bg = "green", fg = "black")

# Pesonalizar botón
boton_personalizado = tk.Button(
    ventana,
    text = "Botón personalizado",
    font =("Arial", 25, "bold"),
    bg = "orange",
    fg = "white",
    activebackground = "red",
    activeforeground = "yellow",
    width = 15,
    command = accion_boton
)
boton_personalizado.pack()

def mostrar_nombre():
    nombre_obtenido = nombre.get()
    resultado.config(text= f"Hola, bienvenido, {nombre_obtenido}")

# ENTRY
# Ingresar datos 
# Entry = input 
etiqueta3 = tk.Label(ventana, text = "Ingrese su nombre: ")
etiqueta3.pack()

# Almacenar un tipo de valor 
nombre = tk.StringVar()
entrada_nombre = tk.Entry(ventana, width= 25, textvariable= nombre)
entrada_nombre.pack()

boton = tk.Button(ventana, text="Saludar", command= mostrar_nombre)
boton.pack()

resultado = tk.Label(ventana, text= "")
resultado.pack()


# TEXT
# Agrega un input mucho mas extenso que el ENTRY sin necesidad de crear una variabla para almacenar el comentario obtenido

def mostrar_comentario():
# Tomar todo el comentario del comentario desde el caracter 1 hasta el último inculyendo saltos de lineas, puntos, comas, simbolos y tabulaciones 
    comentario_obtenido = comentario.get("1.0", tk.END)
    resultado.config(text=f"comentario:  {comentario_obtenido}")

etiqueta4 = tk.Label(ventana, text= "Escriba su comentario")
etiqueta4.pack()

comentario = tk.Text(ventana, width= 40, height= 5, wrap= "word")
comentario.pack()

boton4 = tk.Button(ventana, text="Mostrar comentario", command= mostrar_comentario)
boton4.pack()

resultado4 = tk.Label(ventana, text= "")
resultado4.pack()


# CHECKBUTTON
opcion_var = tk.IntVar()

check_opciones = tk.Checkbutton(
    ventana,
    text= "Desea recibir notificaciones?",
    variable= opcion_var,
    onvalue= 1,
    offvalue= 0
)
check_opciones.pack()

def mostrar_estado():
    if opcion_var.get() ==1:
        resultado5.config(text= "Notificaciones activadas")
        print(opcion_var.get())
    else:
        resultado5.config(text="Notificaciones desactivadas")
        print(opcion_var.get())

boton5 = tk.Button(ventana, text = "Confirmar", command= mostrar_estado)
boton5.pack()

resultado5 = tk.Label(ventana, text="")
resultado5.pack()



# RADIOBUTTON
seleccionar_var = tk.StringVar()

opcion1 = tk.Radiobutton(ventana, text= "Opción 1", variable= seleccionar_var, value= "Opcion1")
opcion1.pack()

opcion2 = tk.Radiobutton(ventana, text= "Opción 2", variable= seleccionar_var, value= "Opcion2")
opcion2.pack()

opcion3 = tk.Radiobutton(ventana, text= "Opción 3", variable= seleccionar_var, value= "Opcion3")
opcion1.pack()









# Mantiene la ventana abierta 
ventana.mainloop()


