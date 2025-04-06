"""
Crear un juego de fusión

El juego consiste en crear personajes de un juego y que estos personajes se puedan 
funsionar para formar personajes más poderosos que tengan más poder...

Para ello deberemos cambiar el comportamiento del operador '+' para que cuando los
personajes se fusionen, salga un nuevo personaje con habilidades mejoradas.

una posible formula es: el promedio de las habilidades de ambos, al cuadrado
"""
from recursos import tittle_format as tf

class Cazador:
    def __init__(self, latigo, fuerza, defensa):
        self.latigo = latigo
        self.fuerza = fuerza
        self.defensa = defensa
    
    def __repr__(self):
        return f'Cazador(Latigo = {self.latigo}, Fuer = {self.fuerza}, Def = {self.defensa})'

    def __add__(self, otro):
        mas_fuerza = self.fuerza ** otro.fuerza
        mas_defensa = self.defensa ** otro.defensa
        return f'Cazador(Latigo = {self.latigo}-{otro.poder}, Fuer = {mas_fuerza}, Def = {mas_defensa})'
    

belmont = Cazador('Latigo', 250, 250)
print(belmont) 
