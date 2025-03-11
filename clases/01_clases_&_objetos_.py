# Las clases son plantillas de como se debe hacer un objeto
from pyfiglet import Figlet

def tittle_format(tittle, subtittle):
    format_tittle = Figlet(font='sblood', justify='center')
    format_subtittle = Figlet(font='pepper', justify='center')

    print('-'*(len(subtittle)*8))
    print(format_tittle.renderText(tittle.upper()))
    print(format_subtittle.renderText(subtittle.upper()))
    print('-'*(len(subtittle)*8))

class Celular: # Las clases se definen en PascalCase
    # Todos los atributos de la clase se definen aka
    # estos atributos serán compartidos por todos los objetos que instaciemos a partir de esta clase
    def __init__(self, marca, modelo, camara): # Este es un método especial llamado 'constructor'
        # Se ejecuta automáticamente al crear un nuevo objeto de la clase
        # el primer parametro de cualquier método es 'self'. Representa la instacia del objeto que se esta creando
        self.marca = marca # Se le asigna un valor al parámetro
        self.modelo = modelo
        self.camara = camara


tittle = 'POO'
subtittle = '- Clases -'

celu1 = Celular('Samsung', 'S23', '48MP') # Cada que creamos un objeto estamos creando una instancia de la clase
celu2 = Celular('XIAOMI', 'Redmi', '32MP')

tittle_format(tittle, subtittle)

print(celu1)
print(celu1.marca) # esto en realidad es: 'self.marca'
print(celu1.modelo)

print(celu2)
print(celu2.marca)
print(celu2.modelo)