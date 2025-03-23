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

tf('getters and setters')

class Datos:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad

    def get_nombre(self): # Con get accedemos al atributo que técnicamente es privado
        return self.__nombre
    
    def set_nombre(self, nombre): # Con set definimos el valor del atributo nombre que ess provido
        self.__nombre = nombre


persona = Datos('Brayan', 25)
nombre = persona.get_nombre()
print(nombre)

persona.set_nombre('Ellis')
print(persona.get_nombre())