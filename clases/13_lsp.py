"""
Las siglas SOLID representan cinco principios fundamentales de la programación orientada a objetos que ayudan a escribir código más mantenible, escalable y limpio. 

🔹 L - Liskov Substitution Principle (LSP)
"Las clases hijas deben poder sustituir a sus clases padres sin que el programa se rompa."

En criollo: si tenés una clase padre y hacés una subclase, esa subclase debería comportarse como un reemplazo válido de la clase padre. Si no, algo hiciste mal, y estás rompiendo el contrato entre padre e hijo (tipo drama familiar nivel telenovela).
"""
class Ave:
    def cantar(self):
        return 'Pío pío.'

class AveVoladora(Ave):
    def volar(self):
        return 'Estoy volando.'

class Turpial(AveVoladora):
    def volar(self):
        return 'El turpial surca los cielos.'

# Acá se rompe LSP
# El pinguino esta heredando algo que no puede hacer
"""class Pinguino(Ave):
    def volar(self):
        raise Exception('No puedo volar, soy un pinguino')"""

class Pinguino(Ave):
    def nadar(self):
        return 'Me voy a Maracaibo nadando.'

pajarito = Turpial()
print(pajarito.volar())
print(pajarito.cantar())

pingu = Pinguino()
print(pingu.cantar())
print(pingu.nadar())
