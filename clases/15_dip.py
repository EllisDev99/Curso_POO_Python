"""
Las siglas SOLID representan cinco principios fundamentales de la programación orientada a objetos que ayudan a escribir código más mantenible, escalable y limpio. 

🔹 D - Dependency Inversion Principle (DIP)
Los módulos de alto nivel no deberían depender de módulos de bajo nivel. Ambos deberían depender de abstracciones.
Las abstracciones no deberían depender de los detalles. Los detalles deben depender de las abstracciones.

Las clases no deberían depender de clases concretas, sino de interfaces o abstracciones. Porque si cambiás la implementación, no deberías tener que cambiar la clase que la usa. Básicamente: no te cases con los detalles, enamorate del concepto.

DEFINICIÖN DADA POR MI AMIGA CHATGPT
"""
from abc import ABC, abstractmethod

# Definimos la abstracción, "interfaz" de ave
class Ave(ABC):
    @abstractmethod
    def comer(self):
        pass

# Definimos nuestras clases concretas
class Pinguino(Ave):
    def comer(self):
        print('El pinguino come pescado.')

class Colibri(Ave):
    def comer(self):
        print('El colibri come nectar.')

# Esta clase no depende de otra en concreto solo de la abstracción
class Alimentador:
    def alimentar(self, ave: Ave):
        ave.comer()


# MAIN
alimentador = Alimentador()
pingu = Pinguino()
coli = Colibri()

alimentador.alimentar(pingu)
alimentador.alimentar(coli)
# 💥 DIP cumplido: el Alimentador puede trabajar con cualquier Ave, sin saber si vuela, nada o baila salsa.