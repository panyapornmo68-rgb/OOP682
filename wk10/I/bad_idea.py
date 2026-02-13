class Machine:
    def __init__(self, document):
        pass

    def start(self, document):
        pass

    def stop(self, document):
        pass

class OldPrinter(Machine):
    def print(self, document):
        print("Printing document:", document)
    def scan(self, document):
        raise NotImplementedError("This printer cannot scan documents.")
    def fax(self, document):
        raise NotImplementedError("This printer cannot fax documents.")