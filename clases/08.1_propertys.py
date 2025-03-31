from recursos import tittle_format as tf

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property # Convierte el método nombre en un getter
    # Ahora podemos acceder a persona.nombre como si fuera un atributo, sin necesidad de usar persona.nombre().
    def nombre(self):
        """Getter: obtiene el nombre"""
        return self.__nombre
    
    @nombre.setter # Atributo.setter se usa para definir el setter de dicho atributo
    def nombre(self, new_nombre):
        """Setter: modifica el nombre con validación"""
        if not isinstance(new_nombre, str): # si new_nombre no es una instancia de str
            # es decir, no es un string, entra en el if
            raise ValueError('El nombre debe ser una cadena de texto.') # Lanza un error
            #raise es una palabra clave que se utiliza para lanzar excepciones de manera manual
            
        self.__nombre = new_nombre


tf('property')

persona = Persona('Brayan')
print(persona.nombre) # Llama al getter

persona.nombre = 'Ellis' # Llama al setter
print(persona.nombre)