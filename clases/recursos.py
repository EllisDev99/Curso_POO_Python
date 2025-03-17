from pyfiglet import Figlet

def tittle_format(subtittle):
    """
    Genera un título formateado con estilo ASCII art para una lección o tema.

    Esta función utiliza las librerías `pyfiglet` para crear títulos en ASCII art.
    El título principal "POO" se muestra con la fuente 'speed' y el subtítulo
    proporcionado se muestra con la fuente 'smshadow', ambos centrados.

    Args:
        subtittle (str): El subtítulo que se mostrará debajo del título principal.

    Ejemplo:
        tittle_format('metodos')
        # Salida esperada:
        # --------------------------------------------------------------------------------
        #                                       POO
        #                                     METODOS
        # --------------------------------------------------------------------------------
    """
    tittle = Figlet(font='speed', justify='center')
    format_subtittle = Figlet(font='smshadow', justify='center')

    print('-'*80)
    print(tittle.renderText('POO'))
    print(format_subtittle.renderText(subtittle.upper()))
    print('-'*80)