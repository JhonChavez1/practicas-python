'''
Realizar un programa que conste de una clase llamada alumno que tenga como atributos el nombre y la nota del alumno.
Luego definir los metodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota
y si ha aprobado o no.
'''

class Alumno():
    def _init_(self, nombre, nota):

        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Alumno:", self.nombre)
        print("Nota: ", self.nota)
        print("")

    def resultado(self):
        if self.nota < 5:
            print("El alumno ha reprobado")

        else:
            print("El alumno ha aprobado ")

alumno1 = Alumno("Diego", 4)
alumno2 = Alumno("Sofia", 2)

alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()