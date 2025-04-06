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

    def __add__(self, otro_pj):
        mas_fuerza = round(((self.fuerza + otro_pj.fuerza) / 2) ** 2)
        mas_defensa = round(((self.defensa + otro_pj.defensa) / 2) ** 2)
        nuevo_latigo = f'{self.latigo}-{otro_pj.poder}'
        return Cazador(nuevo_latigo, mas_fuerza, mas_defensa)

class Bruja:
    def __init__(self, poder, fuerza, defensa):
        self.poder = poder
        self.fuerza = fuerza
        self.defensa = defensa
    
    def __repr__(self):
        return f'Bruja(Poder = {self.poder}, Fuer = {self.fuerza}, Def = {self.defensa})'
    


tf('Ejercicio III')

belmont = Cazador('Latigo', 10, 5)
print(belmont) 

belnades = Bruja('Fuego', 5, 2)
print(belnades)

julius_belmont = belmont + belnades
print(julius_belmont)
