# La herencia permite a la clase hija acceder a todos los métodos y atributos de la clase padre.
# Esto fomenta la reutilización de código y la creación de jerarquías de clases.
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def saludar(self):
        print(f'Hola, soy {self.nombre}, mucho gusto.')

class Empleado(Persona):#Indicamos que la clase Empleado heredara de la clase Persona
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad) #Herencia de la clase padre 'Persona'
        """ explicación de 'super()': básicamente llama al constructor de la calse 
        Persona para incializar los atributos heredados"""
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, universidad, carrera):
        super().__init__(nombre, edad, nacionalidad)
        self.universidad = universidad
        self.carrera = carrera


trabajador = Empleado('Brayan', 25, 'venezolano', 'Programador', 500)
estudiante = Estudiante('kevin', 23, 'venezolano', 'UBV', 'Relaciones Internacionales')

trabajador.saludar()
print(trabajador.trabajo)

estudiante.saludar()
print(estudiante.carrera)