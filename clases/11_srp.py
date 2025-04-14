"""
Las siglas SOLID representan cinco principios fundamentales de la programación orientada a objetos que ayudan a escribir código más mantenible, escalable y limpio. 

🔹 S - Single Responsibility Principle (SRP)
"Una clase debe tener una sola razón para cambiar."

🔹 O - Open/Closed Principle (OCP)
"El código debe estar abierto para extensión, pero cerrado para modificación."

Tenés que poder agregar nuevas funcionalidades sin tener que tocar lo que ya anda bien. Usás herencia, polimorfismo o interfaces para extender, sin romper lo viejo. Es como ponerle DLC a un juego sin reescribir el juego base.

🔹 L - Liskov Substitution Principle (LSP)
"Las clases hijas deben poder sustituir a sus clases padres sin que el programa se rompa."

Si tenés una clase Animal y un Perro hereda de Animal, entonces podés usar un Perro donde esperás un Animal y todo tiene que seguir funcionando. Si no... es porque metiste una clase hija que no respeta las reglas del juego.

🔹 I - Interface Segregation Principle (ISP)
"Es mejor tener muchas interfaces específicas que una sola general que haga de todo."

Evitá forzar a una clase a implementar métodos que no necesita.

🔹 D - Dependency Inversion Principle (DIP)
"Depende de abstracciones, no de concreciones."

Las clases no deberían depender de clases concretas, sino de interfaces o abstracciones. Porque si cambiás la implementación, no deberías tener que cambiar la clase que la usa. Básicamente: no te cases con los detalles, enamorate del concepto.

DEFINICIÖN DADA POR MI AMIGA CHATGPT
"""
from recursos import tittle_format as tf

tf('SRP')

# El siguiente código no representa el principio SRP porque la clase Auto se encarga tanto de mover como del combustible
"""class Carro();
    def __init__(self):
        self.posicion = 0
        self.combustible = 100
    
    def mover(self, distancia):
        if self.combustible >= distancia / 2:
            self.posicion += distancia
            self.combustible -= distancia / 2
        else:
            print('No hay suficiente combustible.')
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible"""
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

class Carro():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2) 
            print('Has movido el carro.')
        else:
            print('No hay suficiente combustible.')
    
    def obtener_posicion(self):
        return self.posicion


tanque = TanqueDeCombustible()
auto = Carro(tanque)
print(auto.obtener_posicion())
auto.mover(15)
print(auto.obtener_posicion())
auto.mover(100)
print(auto.obtener_posicion())
auto.mover(90)
print(auto.obtener_posicion())
auto.mover(60)
print(auto.obtener_posicion())
auto.mover(10)
print(auto.obtener_posicion())
auto.mover(235)
print(auto.obtener_posicion())
auto.mover(5)
print(auto.obtener_posicion())
auto.mover(5)
print(auto.obtener_posicion())