from abc import ABC, abstractmethod
class Shortcuts(ABC):
    @abstractmethod
    def ctrlC(self):
        pass

class Mac:
    def commandC(self):
        print('Copied successfully')

class Adapter(Shortcuts):
    def __init__(self, computer: Mac):
        self.computer = computer
    def ctrlC(self):
        self.computer.commandC()

macbook = Mac()
macbook.commandC()

adapterMac = Adapter(macbook)
adapterMac.ctrlC()