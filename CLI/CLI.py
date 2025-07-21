from cmd import Cmd


class MipymeShell(Cmd):
    intro = 'Bienvendio a la shell de MiPyME\n\nPara una lista completa de comandos ingrese "help" o "?"\n'
    prompt = '(MiPyME)/> '

    def do_exit(self, arg):
        'Termina y sale del programa'
        print('Finalizando MiPyME.')
        return True

