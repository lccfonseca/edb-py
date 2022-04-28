import copy

# TAD Lista com as seguintes operações:
# Inicializador do TAD, podentanto iniciar com [], como com uma lista passada como parâmetro
# Verificar se a lista está vazia
# Inserir um elemento no início da Lista
# Inserir um elemento no final da Lista
# Remover um elemento do início da Lista
# Remover um elemento do final da Lista

class Lista:
    def __init__(self, lst=None):
        self.items = []
        if lst is not None:
            self.items = lst

    def is_empty(self):
        return self.items == []

    def insert_bol(self, item):
        # Refatorar
        self.items.append(item)

    def insert_mol(self, item):
        # Refatorar
        self.items.append(item)

    def insert_eol(self, item):
        self.items.append(item)

    def remove_bol(self):
        first = self.items[0]
        del self.items[0]
        return first

    def remove_mol(self):
        # Refatorar
        return self.items.pop()

    def remove_eol(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_list(self):
        for item in self.items:
            print(item)