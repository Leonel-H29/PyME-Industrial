import os
from cmd import Cmd


class MipymeShell(Cmd):
    intro = 'Bienvendio a la shell de MiPyME\n\nPara una lista completa de comandos ingrese "help" o "?"\n'
    prompt = '(MiPyME)/> '

    # Accepted commands

    def do_clear(self, arg):
        """Limpia la pantalla del terminal."""
        # Check the operating system and execute the appropriate command
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Linux/macOS
            os.system('clear')


    def do_exit(self, arg):
        """Termina y sale del programa."""
        print('Finalizando MiPyME.')
        return True
    

    # Other methods

    def preloop(self):
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Linux/macOS
            os.system('clear')


