"""
La abstracción es el concepto de ocultar los detalles y mostrar solo lo esencial, en pocas palabras permite
al usuario interactuar con una clase sin necesidad de preocuparse de cómo funciona por dentro.

* Clases Abstractas:
Es una clase que no se puede instanciar pero sirve como plantilla para crear otras clases.

* Implementación:
Implementar un método quiere decir definir como va a funcionar.
"""
from recursos import tittle_format as tf
from abc import ABC, abstractclassmethod # Importamos ABC y abstractmethod para crear una clase abstracta


class Persona(ABC):
    """
    Clase abstracta que representa una persona.
    Requiere que cualquier subclase implemente el método hacer_actividad.
    """
    @abstractclassmethod # Indicamos que este método debe ser implementado en las subclases
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_activiad(self):
        """
        Método abstracto que debe ser implementado por las subclases.
        """
        pass
    
    def presentarse(self):
        print(f'Hola, soy {self.nombre} y tengo {self.edad} años.')

class Estudiante(Persona):
    """
    Representa a un estudiante, que es una subclase de Persona.
    """
    def __init__(self, nombre, edad, sexo, actividad):
        """
        Inicializa un estudiante con los mismos atributos de Persona.
        """
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_activiad(self):
        """
        Implementa el método abstracto, describiendo qué estudia el estudiante.
        """
        print(f'Estoy estudiando: {self.actividad}')

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_activiad(self):
        print(f'Estoy trabajando como: {self.actividad}')




tf('abstraction')

# Creación de instancias y prueba de los métodos
maestra = Trabajador('Angela', 47, 'F', 'Maestra')
estudiante = Estudiante('Brayan', 25, 'M', 'Programación')

maestra.presentarse()
maestra.hacer_activiad()

estudiante.presentarse()
estudiante.hacer_activiad()