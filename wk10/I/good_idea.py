from abc import abstractmethod

class Printer:
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan_document(self, document):
        pass

class fax:
    @abstractmethod
    def fax_document(self, document):
        pass

class MultiFunctionPrinter(Printer, Scanner, fax):
    def print_document(self, document):
        print("Printing document:", document)

    def scan_document(self, document):
        print("Scanning document:", document)

    def fax_document(self, document):
        print("Faxing document:", document)