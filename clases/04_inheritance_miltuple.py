from recursos import Persona, Estudiante, Empleado
from recursos import tittle_format as tf

tf('Herencia Multiple')

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f'Mi habilidad es: {self.habilidad}'
    
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)

        self.salario = salario
        self.empresa = empresa
    
    def presentarce(self):
        return f'Hola mi nombre es {self.nombre} y {super().mostrar_habilidad().lower()}'


persona = EmpleadoArtista('Brayan', 25, 'venezolano', 'Pixelart', 250, 'Google')
print(persona.mostrar_habilidad())
print(persona.presentarce())


# Como identificar de quien hereda una subclase
herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)
herencia = issubclass(EmpleadoArtista, Persona)
print(herencia)
herencia = issubclass(EmpleadoArtista, Empleado)
print(herencia)
herencia = issubclass(EmpleadoArtista, Estudiante)
print(herencia)
print('='*80)

# Como identificar si un objeto es una instacia de una clase
instancia = isinstance(persona, EmpleadoArtista)
print(instancia)
instancia = isinstance(persona, Artista)
print(instancia)
instancia = isinstance(persona, Persona)
print(instancia)
instancia = isinstance(persona, Estudiante)
print(instancia)
instancia = isinstance(persona, Empleado)
print(instancia)