"""
El polimorfismo es un concepto de la programación orientada a objetos (POO) que permite que un mismo método o función se comporte de manera diferente dependiendo del objeto que lo use. En otras palabras, es la capacidad de una misma operación o función para trabajar con diferentes tipos de datos o clases.
"""
from recursos import tittle_format as tf

class Gato():
    def sonido(self):
        return '¡Miau!'

class Perro():
    def sonido(self):
        return '¡Guau!'

def hacer_sonido(animal):
    print(animal.sonido())


tf('Polymorphism')

# Instanciamos las clases
felino = Gato() # El tipo declarado es 'felino' pero el tipo real es 'Gato'
can = Perro() # el tipo real es lo que realmente es el objeto en memoria

print(can.sonido()) # aka cambia el objeto para el método
print(felino.sonido())

hacer_sonido(can) # aka cambia el argumento para la función
hacer_sonido(felino)