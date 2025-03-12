from pyfiglet import Figlet

def tittle_format(subtittle):
    tittle = Figlet(font='speed', justify='center')
    format_subtittle = Figlet(font='smshadow', justify='center')

    print('-'*80)
    print(tittle.renderText('POO'))
    print(format_subtittle.renderText(subtittle.upper()))
    print('-'*80)


clase_hoy = 'metodos'
tittle_format(clase_hoy)