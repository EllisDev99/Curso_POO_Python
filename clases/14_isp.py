"""
Las siglas SOLID representan cinco principios fundamentales de la programación orientada a objetos que ayudan a escribir código más mantenible, escalable y limpio. 

🔹 I - Interface Segregation Principle (ISP)
'Es mejor tener muchas interfaces específicas que una sola general que haga de todo.'

DEFINICIÖN DADA POR MI AMIGA CHATGPT

En este caso con 'INTERFAZ' nos referimos a las clases abstractas.
"""
from abc import ABC, abstractmethod

"""
# Trabajador no ppuede incluir a la gente que come y duerma
# esto puede limitar a otro objeto que herede de trabajador pero no requiera comer ni dormir
class Trabajador(ABC):

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def trabajar(self):
        pass

    @abstractmethod
    def dormir(self):
        pass
"""
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Decansar(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador, Comedor, Decansar):
    def comer(self):
        print('El trabajador esta comiendo.')

    def trabajar(self):
        print('El trabajador esta chambeando.')

    def dormir(self):
        print('El trabajador esta durmiendo.')

class Robot(Trabajador):
    def trabajar(self):
        print('El robot esta chambeando.')


robot = Robot()
robot.trabajar()