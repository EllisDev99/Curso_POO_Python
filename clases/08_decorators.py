"""
Decorators:

Los decoradores son funciones que decoran a otra, es decir, agregan código extra a una
función que ya existía.

Los decoradores son utilizados para la validación de entradas, manejo de excepciones, etc.
"""

from recursos import tittle_format as tf

def decorator(funct):
    def function_modificed():
        print('Antes de llamar a la función.')
        funct()
    return function_modificed

@decorator
def greetings():
    print('Hola Ellis, ¿cómo estás? ')


tf('decorators')

greetings()