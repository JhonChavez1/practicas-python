import tkinter as tk

ventana = tk.Tk()
ventana.title("Menú")

# Menú principal
# Menu = metodo de tkinter
menu_var = tk.Menu(ventana)
ventana.config(menu= menu_var)

# submenú
# posicionar nuestr submenú dentro del menú
archivo_menu = tk.Menu(menu_var)
# creando la cascada
menu_var.add_cascade(label= "Archivo",  menu= archivo_menu)


'''
En Python, lambda es una forma rápida de crear funciones anónimas (sin nombre). Se usa cuando quieres pasar una función con argumentos 
pero sin tener que definirla por separado con def.
'''
# Primera opción del submenú
archivo_menu.add_command(label = "Nuevo", command= lambda: resultado.config(text= "Nuevo Archivo"))
archivo_menu.add_command(label = "Abrir Archivo", command= lambda: resultado.config(text= "Abrir Archivo"))
archivo_menu.add_command(label = "Guardar Archivo", command= lambda: resultado.config(text= "Guarda Archivo"))
# Línea separadora
archivo_menu.add_separator()
archivo_menu.add_command(label= "Salir", command= ventana.quit)

editar_menu = tk.Menu(menu_var, tearoff=0)
menu_var.add_cascade(label= "Editar", menu= editar_menu)

editar_menu.add_command(label = "Cortar", command= lambda: resultado.config(text= "Cortar"))
editar_menu.add_command(label = "Copiar", command= lambda: resultado.config(text= "Copiar"))
editar_menu.add_command(label = "Pegar", command= lambda: resultado.config(text= "Pegar"))

resultado = tk.Label(ventana, text= "")
resultado.pack()


ventana.mainloop()