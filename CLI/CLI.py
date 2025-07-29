import os
from cmd import Cmd
from MySME.mySME import MySME


class CLI(Cmd):
    intro = 'Bienvendio a la shell de MiPyME\n\nPara una lista completa de comandos ingrese "help" o "?"\n'
    prompt = '(MiPyME)/> '
    mysme = MySME()

    # Accepted commands

    def do_clear(self, arg):
        """Clears terminal"""
        self.__clear()

    def do_exit(self, arg):
        """Exit"""
        print('Finalizando MiPyME.')
        return True

    def do_add_supply(self, arg):
        """Adds a supply request"""
        # print(self.__parse(arg))
        args = self.__parse(arg)
        print(args)
        self.mysme.add_supply(args[0], int(args[1]), args[2], args[3])

    def do_show_supplies(self, arg):
        """Show a list with all supplies"""
        self.mysme.show_supply()

    def do_add_tps(self, arg):
        """Adds a service request"""
        args = self.__parse(arg)
        print(args)
        self.mysme.add_tps(args[0], args[1], args[2])

    def do_show_tps(self, arg):
        """Show a list with all third party services"""
        self.mysme.show_tps()

    def do_load_supplies(self, arg):
        self.mysme._load_supplies()
    
    def do_save_supplies(self, arg):
        self.mysme._save_supplies()

    # Other methods

    def preloop(self):
        self.__clear()

    def __clear(self):
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Linux/macOS
            os.system('clear')

    def __parse(self, arg):
        'Convert a series of zero or more numbers to an argument tuple'
        return tuple(arg.split(" "))
