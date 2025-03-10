# Las clases son plantillas de como se debe hacer un objeto

from pyfiglet import Figlet

tittle = Figlet(font='sblood')
subtittle = Figlet(font='pepper')

class Celular(): # Las clases se definen en PascalCase
    # Todos los atributos de la clase se definen aka
    # estos atributos serán compartidos por todos los objetos que instaciemos a partir de esta clase
    marca = 'Samsung'
    modelo = 'S23'
    camara = '48MP'

celu1 = Celular() # Cada que creamos un objeto estamos creando una instancia de la clase

print('-'*70)
print(tittle.renderText('POO'))
print(subtittle.renderText('CLASES'))
print('-'*70)
print(celu1)
print(celu1.marca)
print(celu1.modelo)