"""
Crear la clase 'Estudiante', con lo siguientes atriutos: 
* Nombre 
* Edad 
* Grado

además de crear un Método 'estudiar()' -> el estudiante (nombre) está estudiando

El objetivo es crear un objeto 'Estudiante' y usar el método 'estudiar()', se debe
interactuar con el usuario y este debe brindar los atributos.
"""
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f'El estudiante {self.nombre} de {self.edad} años del grado {self.grado}')


alumno = Estudiante(str(input().capitalize()), int(input()), str(input().upper()))
Estudiante.estudiar(alumno)