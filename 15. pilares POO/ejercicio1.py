'''
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
'''

class Estudiante():
    def __init__(self, nombre, nota):
      self.nombre = nombre
      self.nota = nota

    def imprimir(self):
      print("Nombre:" , self.nombre, "\nNota: " , self.nota)

    def resultados(self):
      if self.nota < 7:
         print("Has REPROBADO!")
      else:
         print("Has APROBADO!")

estudiante1 = Estudiante("Jhon", 4)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("Carol", 9)
estudiante2.imprimir()
estudiante2.resultados()

