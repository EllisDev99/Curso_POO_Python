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
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificador(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f'Enviando mensaje a {self.usuario.email}')

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f'Enviando mensaje a {self.usuario.sms}')

# Extendemos la funcionalidad de la clase Notificador creando una subclase de esta