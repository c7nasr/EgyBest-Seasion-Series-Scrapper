from termcolor import cprint


class Printer:

    def InfoPrinter(self, text):
        cprint(f'INFO: {text}', 'blue')

    def PendingPrinter(self, text):
        cprint(f'PENDING: {text}', 'yellow')

    def SuccessPrinter(self, text):
        cprint(f'SUCCESS: {text}', 'green')

    def CationPrinter(self, text):
        cprint(f'CATION: {text}', 'red')
