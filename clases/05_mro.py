# MRO o método de resolución de orden, báscicamente hace referencia al orden en que python búsca métodos y atributos en las clases

from recursos import tittle_format as tf

class A:
    def hablar(self):
        print('Hola desde A')

class B(A):
    def hablar(self):
        print('Hola desde B')

class G():
    def hablar(self):
        print('Hola desde G')

class C(G):
    def hablar(self):
        print('Hola desde C')

class D(B,C):
    def hablar(self):
        print('Hola desde D')


# MAIN
tf('mro')

d = D() # Instanciamos un objeto de la clase D
d.hablar() # Accedemos al método hablar desde D

print(D.mro()) # muestra el orden en que python busca los métodos
A.hablar(d) # llamá al método 'hablar()' desde el objeto 'd'