"""
Crear un juego de fusión

El juego consiste en crear personajes de un juego y que estos personajes se puedan 
funsionar para formar personajes más poderosos que tengan más poder...

Para ello deberemos cambiar el comportamiento del operador '+' para que cuando los
personajes se fusionen, salga un nuevo personaje con habilidades mejoradas.

una posible formula es: el promedio de las habilidades de ambos, al cuadrado
"""
from recursos import tittle_format as tf # Importamos el formato de título en arte ASCI

class Cazador:
    """Clase que representa a un cazador de criaturas nocturnas"""
    def __init__(self, latigo, fuerza, defensa):
        self.latigo = latigo
        self.fuerza = fuerza
        self.defensa = defensa
    
    def __repr__(self):
        # Representación del objeto
        return f'Cazador(Latigo = {self.latigo}, Fuer = {self.fuerza}, Def = {self.defensa})'

    def __add__(self, otro_pj):
        """
        Permite fusionar un Cazador con otro personaje (por ejemplo, una Bruja) usando el operador +.
    
        La fusión genera un nuevo Cazador con estadísticas combinadas:
        - La fuerza y la defensa se calculan como el promedio de ambas, luego elevadas al cuadrado y redondeadas.
        - El látigo se modifica combinando el látigo actual con el poder del otro personaje.

        Parámetros:
            otro_pj (object): Otro personaje con atributos `fuerza`, `defensa` y `poder`.

        Retorna:
            Cazador: Una nueva instancia con los atributos fusionados.

        Nota:
            - hasattr(obj, attr) -> verifica si un objeto tiene un atrbuto con ese nombre.
            - getattr(obj, attr, default) -> busca un atributo. Si no existe, devuelve un valor por defecto 
        """
        if not hasattr(otro_pj, 'fuerza') or not hasattr(otro_pj, 'defensa'): 
            # chequeamos que el otro_pj tenga los attr fuerza y defensa
            raise TypeError("No se puede fusionar con un objeto sin fuerza ni defensa.")
        
        poder_extra = getattr(otro_pj, 'poder', '???')  # Usa '???' si no tiene poder
        nuevo_latigo = f'{self.latigo}-{poder_extra}'

        mas_fuerza = round(((self.fuerza + otro_pj.fuerza) / 2) ** 2)
        mas_defensa = round(((self.defensa + otro_pj.defensa) / 2) ** 2)
        
        return Cazador(nuevo_latigo, mas_fuerza, mas_defensa)

class Bruja:
    def __init__(self, poder, fuerza, defensa):
        """Clase que representa a una compañera con poderes mágicos"""
        self.poder = poder
        self.fuerza = fuerza
        self.defensa = defensa
    
    def __repr__(self):
        return f'Bruja(Poder = {self.poder}, Fuer = {self.fuerza}, Def = {self.defensa})'
    


tf('Ejercicio III') # Imprime el título

belmont = Cazador('Latigo', 10, 5) # Instanciamos la clase Cazador
print(belmont)  # Imprimimos llamando a __repre__

belnades = Bruja('Fuego', 5, 2)
print(belnades)

julius_belmont = belmont + belmont
print(julius_belmont)

# CREAR UN JUEGO INTERATUABLE CON EL USUARIO EN DONDE PUEAS CREAR ESPADAS