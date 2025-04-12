"""
Ejercicio III   
                                            --- 🗡️ ¡Forja tu Espada Definitiva! 🗡️---

Vas a crear un programa interactivo en consola donde el usuario pueda gestionar una colección de espadas mágicas. El menú debe tener las siguientes opciones:
    - Crear espada
    - Fusionar espadas
    - Ver espadas creadas
    - Eliminar espada
    - Salir

🔧 DETALLES TÉCNICOS

1. Clase base EspadaBase
Crea una clase llamada EspadaBase con estos dos atributos:
    - corte (int): nivel de filo de la espada
    - dureza (int 0-3): resistencia del material

2. Clases hijas: EspadaElemental
Crea una clase hija que herede de EspadaBase. Esta clase debe tener un atributo adicional:
    - elemento (str): uno de estos valores posibles → "fuego", "agua", "tierra" o "aire"

También debe poder soportar más de un elemento si se fusionan espadas (ver siguiente punto).

💥 FUSIÓN DE ESPADAS

El usuario puede elegir dos espadas ya creadas para fusionarlas.
    - La nueva espada tendrá:
        * Elementos combinados: por ejemplo, "fuego" + "agua" → "fuego-agua"
        * corte y dureza calculados así: el promedio de ambos habilidades al cuadrado
        * La nueva espada reemplaza a las originales (opcional: puedes pedir confirmación).

🗃️ GESTIÓN DE ESPADAS

Usa una lista para almacenar las espadas creadas. Cada espada debe tener un nombre o identificador único que el usuario pueda elegir (o asigna tú uno automáticamente con un contador).

🎯 OBJETIVO

Tu programa debe permitir al usuario:
    - Crear espadas con atributos personalizados.
    - Fusionarlas para obtener versiones más poderosas.
    - Ver todas las espadas creadas con sus detalles.
    - Eliminar las que ya no sirvan.

"""
from recursos import tittle_format as tf

class EspadaBase():
    """
    Representa una espada con atributos básicos.

    Attributes:
        corte (int): Nivel de corte de la espada.
        dureza (int): Dureza del material (0 a 3).
    """
    def __init__(self, corte, dureza):
        """
        Inicializa una instancia de EspadaBase

        Args:
            corte (int): Nivel de corte.
            dureza (int): Dureza del material (0 a 3).
        """
        self.corte = corte
        self.dureza = dureza

class EspadaElemental(EspadaBase):
    """
    Representa una espada con un poder elemental.

    Attributes:
        corte (int): Nivel de corte heredado de EspadaBase.
        dureza (int): Dureza heredada de EspadaBase.
        elemento (str): Tipo de elemento (fuego, agua, tierra o aire).
    """
    def __init__(self, corte, dureza, elemento):
        """
        Inicializa una instancia de EspadaElemental.

        Args:
            corte (int): Nivel de corte.
            dureza (int): Dureza del material (0 a 3).
            elemento (str): Tipo de elemento (fuego, hielo, etc.).
        """
        super().__init__(corte, dureza)
        self.elemento = elemento

    def __repr__(self):
        """
        Representación en texto de la espada elemental.

        Returns:
            str: Descripción con los stats de la espada.
        """
        return f'Espada elemental stats: corte={self.corte}, dureza={self.dureza}, elemento={self.elemento}'


def opciones_menu():
    """
    Muestra un menú interactivo para gestionar espadas.

    Permite al usuario:
        - Crear una nueva espada.
        - Fusionar espadas existentes.
        - Ver la lista de espadas creadas.
        - Eliminar una espada.
        - Salir del programa.

    El menú se repite hasta que el usuario elige salir (opción 0).
    
    Maneja errores como:
        - Entrada no numérica (ValueError).
        - Interrupción del teclado (KeyboardInterrupt).
    
    No recibe parámetros ni devuelve valores.
    """
    while True:
        try:
            print('[1] - Crear espada\n[2] - Fusionar espadas\n[3] - Ver espadas creadas\n[4] - Eliminar espada\n[0] - Salir')
            opcion = int(input('Elíga una opción: '))
            if opcion == 0:
                print('Saliendo del creador de espadas.')
                break
            elif opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            else:
                print('='*100)
                print('Valor fuera de rango.\nDigite una opción valida.')
                print('='*100)
                    
        except(ValueError):
            print('Error con el tipo de dato digitado.')
            print('Digite una opción valida.')
        except KeyboardInterrupt:
                print('Programa interrumpido por el usuario.')

    print('Gracias, ¡vuelva pronto!.')












tf('¡Forja tu Espada Definitiva!')
opciones_menu()