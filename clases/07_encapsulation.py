"""
El encapsulamiento consiste en proteger los elementos que componen a una clase.
"""
from recursos import tittle_format as tf

class Miclase:
    def __init__(self):
        self._atributo_privado = 'valor'
        #self.__atributo_muy_privado = 'valor más privado'
    
    def _metodo_privado(self):
        print('Hola')


tf('encapsulation')

obj = Miclase()
print(obj._atributo_privado)
#print(obj.__atributo_muy_privado)

obj._metodo_privado()