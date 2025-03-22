"""
Herencias - Ejercicio II

Ejercicio de herencia y uso de super:
Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales:
* Persona
* Estudiante

La clase Persona tendrá los atributos nombre y edad y un método que imprime el nombre y 
la edad de la persona. La clase Estudiante heredará de la clase Persona y también tendrá un 
atributo adicional: semestre y un método que imprima el semestre del estudiante.

Deberás utilizar en el método de inicialización (init) para reutilizar el código de la
clase padre (Persona). Luego crea una instancia de la clase Estudiante e imprime sus
atributos y utiliza sus métodos para asegurarse de que todo funciona correctamente.


Ejercicio de herencia múltiple y MRO

Imagina que estás modelando animales en un zoo. Crear tres clases:
* Animal
* Mamifero
* Ave

La clase 'Animal' debe tener un método llamado 'comer'. La clase 'Mamifero' de tener el 
método llamado 'Amamantar' y la clase 'Ave' un método llamado 'volar'.

ahora, crea una clase llamada 'Murcielago' que herede de 'Mamifero' y 'Ave', en ese orden, y 
por lo tanto debe ser capaz de 'amamantar' y 'volar', además de 'comer'

Finalmente, juega con el orden de herencia de la clase 'Murcielago' y observa cómo cambia el
MRO y el comportamiento de los métodos al usar super().
"""
from recursos import tittle_format as ft

class People:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def datos(self):
        print(f'Mi nombre es: {self.nombre} y tengo {self.edad} años.')

class Estudent(People):
    def __init__(self, nombre, edad, semestre):
        super().__init__(nombre, edad)
        self.semestre = semestre
    
    def semestre_actual(self):
        print(f'Estoy cursando el {self.semestre}° de la carrera.')
    

ft('ejercicio II')

estudiante = Estudent('Brayan', 25, 5)
estudiante.datos()
estudiante.semestre_actual()