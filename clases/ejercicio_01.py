"""
Crear la clase 'Estudiante', con lo siguientes atriutos: 
* Nombre 
* Edad 
* Grado

además de crear un Método 'estudiar()' -> el estudiante (nombre) está estudiando

El objetivo es crear un objeto 'Estudiante' y usar el método 'estudiar()', se debe
interactuar con el usuario y este debe brindar los atributos.
"""
from recursos import tittle_format as tf

class Estudiante:
    def __init__(self, nombre, edad, semestre):
        self.nombre = nombre
        self.edad = edad
        self.semestre = semestre
    
    def estudiar():
        print('Estudiando')
        

# Main
tf('ejercicios I')

while True:
    # Validamos el nombre del estudiante
    name = str(input('Digite su nombre: ')).strip().upper()
    if name.isdigit():
        while True:
            print('Eso no es un nombre.\nDigite su nombre real.')
            name = str(input('Digite su nombre: ')).strip().upper()
            if not name.isdigit():
                break
    
    # Validamos la edad
    try:
        edad = int(input('Digite su edad: '))
        if edad < 18 or edad > 80:
            while True:
                print('Edad fuera de rango.')
                edad = int(input('Digite su edad: '))
                if edad > 18 and edad < 80:
                    break
    except (ValueError, TypeError):
        print('Error por tipo de dato.\nDigite un número entero.')

        
    break
print('FIN')

    