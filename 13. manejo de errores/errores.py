while True:
    try:
        edad = int(input("Por favor ingrese su esdad: "))
        print("Tu edad es: ", edad)
        break
    except:
        print("Ingresaste un valor erroneo")
    finally:
        print("La ejecución ha finalizado")