# Las clases son plantillas de como se debe hacer un objeto

class Celular(): # Las clases se definen en PascalCase
    # Todos los atributos de la clase se definen aka
    # estos atributos serán compartidos por todos los objetos que instaciemos a partir de esta clase
    marca = 'Samsung'
    modelo = 'S23'
    camara = '48MP'

celu1 = Celular() # Cada que creamos un objeto estamos creando una instancia de la clase
print(celu1)
print(celu1.marca)
print(celu1.modelo)