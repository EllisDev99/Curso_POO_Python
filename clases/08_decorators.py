"""
Decorators:

Los decoradores son funciones que decoran a otra, es decir, agregan código extra a una
función que ya existía.

Los decoradores son utilizados para la validación de entradas, manejo de excepciones, etc.
"""
from recursos import tittle_format as tf

def decorator(funct):
    """
    Decorador que modifica el comportamiento de una función:
    1. Imprime un mensaje antes de ejecutar la función original.
    2. Llama a la función original.
    
    Args:
        funct (function): Función a decorar.
    
    Returns:
        function: Función modificada que incluye el nuevo comportamiento.
    """
    def function_modificed():
        print('Antes de llamar a la función.') # Acción adicional antes de la función original
        funct() # Llamada a la función original
    return function_modificed


@decorator # Aplicamos el decorador a la función 'greetings'
def greetings():
    """Función que imprime un saludo personalizado."""
    print('Hola Ellis, ¿cómo estás? ')


tf('decorators')

greetings()