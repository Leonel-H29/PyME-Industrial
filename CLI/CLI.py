import os
from cmd import Cmd
from MySME.mySME import MySME


class MySMEShell(Cmd):
    intro = 'Bienvendio a la shell de MiPyME\n\nPara una lista completa de comandos ingrese "help" o "?"\n'
    prompt = '(MiPyME)/> '

    # Accepted commands

    def do_clear(self, arg):
        """Limpia la pantalla del terminal."""
        self.__clear()

    def do_exit(self, arg):
        """Termina y sale del programa."""
        print('Finalizando MiPyME.')
        return True

    def do_add_supply_request(self, arg):
        """Adds a supply request."""
        pass

    def do_add_service_request(self, arg):
        """Adds a service request."""
        pass

    # Other methods

    def preloop(self):
        self.__clear()

    def __clear(self):
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Linux/macOS
            os.system('clear')
