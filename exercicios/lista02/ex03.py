import copy

from edb.basico.lista import Node
from edb.basico.lista import ListaEncadeada

# Tutoriais Listas Encadeadas
# https://realpython.com/linked-lists-python/
# https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
# https://www.openbookproject.net/thinkcs/python/english2e/ch19.html

# Ex. 03:
# Considere uma coleção de nomes de sites da web e seus respectivos links
# na Internet armazenados através de uma lista simplesmente encadeada.
# Escreva a respectiva estrutura e um método que, dado o nome de um site,
# busque o seu link correspondente na lista e ao mesmo tempo mova o nó que
# contém o nome buscado para o início da lista, de forma que ele possa ser
# encontrado mais rapidamente na próxima vez que for buscado.

class ListaEx03(ListaEncadeada):
    def __init__(self, nodes=None):
        super().__init__(nodes)

    def search(self, node):
        try:
            l.remove_node(node.data)
            l.add_first(node)
            print(f"Site: {node.data} encontrado e priorizado!")
        except Exception:
            print("Erro: Nó não encontrado!")


    def show_sites(self):
        for node in self:
            print(node.data)


if __name__ == '__main__':
    print('Exercício 03 da Lista de Exercícios 02')

    l = ListaEx03(["www.jp.com.br"])

    l.add_last(Node("www.google.com"))
    l.add_last(Node("www.cnn.com"))
    l.add_last(Node("www.fox.com"))
    l.add_last(Node("www.uol.com.br"))
    l.add_last(Node("g1.globo.com"))

    l.show_sites()

    l.search(Node("www.cnn.com"))
    l.search(Node("xyz.com"))

    l.show_sites()
