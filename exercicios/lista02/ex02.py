import copy

from edb.basico.lista import Lista

# Ex. 02:
# Escreva uma TAD de lista de inteiros ordenada simplesmente encadeada
# com as seguintes operações:
# a) Verificar se um número pertence lista;
# b) Inserir um novo elemento na lista mantendo a ordem;
# c) Remover um elemento da lista;
# d) Imprimir os valores da lista;
# e) Copiar uma lista l1 para uma lista l2;
# f) Concatenar uma lista l1 com uma lista l2;
# g) Intercalar l1 e l2;
# Exercícios extra que não se aplicam a Lista Ordenada, devem ser aplicados na super classe
# h) Inserir um elemento no início da lista;
# i) Inserir um elemento no meio da lista;
# j) Remover um elemento da Lista;
# l) Implemente uma busca binária interativa;

class ListaEx02(Lista):

    def __init__(self, lst=None):
        super().__init__(lst)

    def busca_nat(self, x):
        return x in self.items

    def busca_seq(self, x):
        pos = -1
        for i in range(0, len(self.items)):
            if x == self.items[i]:
                pos = i
                break
        return pos

    def busca_bin_rec(self, e, d, x):
        if d < e:
            return -1
        m = (e + d) // 2
        if self.items[m] == x:
            return m
        elif self.items[m] > x:
            return self.busca_bin_rec(e, m - 1, x)
        else:
            return self.busca_bin_rec(m + 1, d, x)

    def seek_pos(self, x):
        pos = len(self.items)
        for i in range(0, len(self.items)):
            if x <= self.items[i]:
                pos = i
                break
        return pos

    def insert_sort(self, item):
        pos = self.seek_pos(item)
        self.items = self.items[0:pos] + [item] + self.items[pos:]
        return pos

    def get_items(self):
        return self.items

    def copiar(self, origem):
        for e in origem:
            self.insert_eol(e)

    def concatenar(self, l2):
        return self.items + l2

    def intercalar(self, l2):
        lr = ListaEx02([val for pair in zip(self.items, l2) for val in pair])
        return lr

    def intercalar2(self, l2):
        la = ListaEx02(self.get_items())
        lb = ListaEx02(l2)
        lr = ListaEx02()
        while (not la.is_empty()) and (not lb.is_empty()):
            if lr.size() % 2 == 0:
                if not la.is_empty():
                    lr.insert_eol(la.remove_bol())
            else:
                if not lb.is_empty():
                    lr.insert_eol(lb.remove_bol())
        return lr

if __name__ == '__main__':
    print('Exercício 02 da Lista de Exercícios 02')

    l = ListaEx02([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21])

    l1 = ListaEx02()
    l1.copiar(l.get_items())
    l2 = Lista(l1.concatenar(l.get_items()))

    print(l.busca_seq(17))

    print(l.busca_bin_rec(0, len(l.items), 19))

    l.insert_sort(20)
    l.insert_sort(30)

    print("--- Imprime L ---")
    l.print_list()

    print("--- Imprime L1 ---")
    l1.print_list()

    print("--- Imprime L2 ---")
    l2.print_list()

    l3 = l.intercalar2(l1.get_items())

    print("--- Imprime L3 ---")
    l3.print_list()