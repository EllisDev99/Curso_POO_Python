# Métodos especiales
# Definición de la clase Persona con métodos especiales __str__ y __repr__
class Persona:
    def __init__(self, nombre, edad):
        # Método constructor que inicializa los atributos nombre y edad
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        # Este método define cómo se verá la instancia cuando se use print()
        # Devuelve una representación "bonita" para humanos
        return f'Persona(nombre={self.nombre}, edad={self.edad})'

    def __repr__(self):
        # Este método devuelve una representación más formal del objeto
        # Esta forma debería poder ser usada con eval() para recrear el objeto
        return f'Persona("{self.nombre}",{self.edad})'


# Se crea una instancia de Persona 
persona = Persona('Brayan', 25)
# Mostrar la instancia en consola (usa __str__)
print(persona) # Salida: Persona(nombre=Brayan, edad=25)

# Obtener una representación formal (usa __repr__)
repre = repr(persona) # repre ahora contiene: 'Persona("Brayan",25)'

# Usar eval para recrear una nueva instancia a partir del string
result = eval(repre)

# Mostrar la nueva instancia al igual que antes, se llama al método __str__()
print(result) # Salida: Persona(nombre=Brayan, edad=25)

# Se accede directamente al atributo edad del nuevo objeto
print(result.edad) # Salida: 25

"""
Si __str__ no está definido, Python usa __repr__ como respaldo para mostrar algo.

eval() ejecuta cualquier cadena de texto como si fuera código Python.
si evalúas una cadena que viene de un usuario, le estás dando el poder de ejecutar código arbitrario.

🔒 ¿Cuándo se puede usar (con precaución)?:
* Si controlás 100% lo que contiene el string (como en tu ejemplo del __repr__).
* Para scripts temporales, testing, o en código interno.
* Pero nunca en producción con datos externos.

💡 Alternativas seguras:
* ast.literal_eval() → Evalúa solo estructuras de datos (listas, dicts, strings, números). Nada de código peligroso.
* json.loads() → Si estás manejando datos tipo JSON (también más seguro).
"""