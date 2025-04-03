# Métodos especiales
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'

    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'


persona = Persona('Brayan', 25)
print(persona)

repre = repr(persona)
result = eval(repre)
print(result)
print(result.edad)