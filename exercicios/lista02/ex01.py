import copy

from edb.basico.lista import Lista

# Ex. 01:
# Seja L uma lista simplesmente encadeada composta de números inteiros
# cujos nós são l1, l2, l3, ..., ln. Escreva uma TAD que, percorrendo L, uma
# única vez, construa uma outra lista L’ formada dos seguintes elementos:
# a) l2, l3, ..., ln, l1;
# b) ln, ln‐1 ,...,l1;
# c) l1+ln, l2+ln‐1, ..., ln/2+ln/2+1; onde n é par.

# Como solução para este exercício, foi necessário a criação de um novo TAD (Classe),
# derivado do TAD Lista

class ListaEx01(Lista):

    def __init__(self, lst=None):
        super().__init__(lst)

    def e_par(self):
        return (self.size() % 2) == 0

    def reverse(self):
        l_res = ListaEx01()
        l_clone = copy.deepcopy(self)
        while not l_clone.is_empty():
            l_res.insert_eol(l_clone.remove_eol())
        return l_res

    def half_list_sum(self):
        if self.e_par():
            l_res = ListaEx01()
            l_clone = copy.deepcopy(self)
            while not l_clone.is_empty():
                soma = l_clone.remove_bol() + l_clone.remove_eol()
                l_res.insert_eol(soma)
            return l_res
        else:
            return None

if __name__ == '__main__':
    print('Exercício 01 da Lista de Exercícios 02')

    l = ListaEx01([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    l1 = copy.deepcopy(l)

    # Resolução da letra a
    l1.insert_eol(l1.remove_bol())
    print("Lista")
    l.print_list()
    print("Lista L1")
    l1.print_list()

    # Resolução da letra b
    print("Lista Reversa")
    l.reverse().print_list()

    # Resolução da letra c
    print("Lista Soma")
    l.half_list_sum().print_list()