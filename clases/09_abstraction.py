"""
La abstracción es el concepto de ocultar los detalles y mostrar solo lo esencial, en pocas palabras permite
al usuario interactuar con una clase sin necesidad de preocuparse de cómo funciona por dentro.
"""

from recursos import tittle_format as tf

class Auto():
    def __init__(self):
        self._estado = 'apagado'
    
    def encender(self):
        self._estado = 'encendido'
        print('El auto está encendido.')
    
    def conducir(self):
        if self._estado == 'apagado':
            self.encender()
        print('Conduciendo el auto.')


tf('abstraction')

mi_auto = Auto()
mi_auto.conducir()