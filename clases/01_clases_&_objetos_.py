# Las clases son plantillas de como se debe hacer un objeto

from pyfiglet import Figlet

tittle = 'POO'
subtittle = '- Clases -'

def tittle_format(tittle, subtittle):
    format_tittle = Figlet(font='sblood', justify='center')
    format_subtittle = Figlet(font='pepper', justify='center')

    print('-'*(len(subtittle)*8))
    print(format_tittle.renderText(tittle.upper()))
    print(format_subtittle.renderText(subtittle.upper()))
    print('-'*(len(subtittle)*8))

class Celular(): # Las clases se definen en PascalCase
    # Todos los atributos de la clase se definen aka
    # estos atributos serán compartidos por todos los objetos que instaciemos a partir de esta clase
    marca = 'Samsung'
    modelo = 'S23'
    camara = '48MP'

celu1 = Celular() # Cada que creamos un objeto estamos creando una instancia de la clase

tittle_format(tittle, subtittle)

print(celu1)
print(celu1.marca)
print(celu1.modelo)