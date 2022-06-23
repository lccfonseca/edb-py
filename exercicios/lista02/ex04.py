import copy

from edb.basico.lista import ListaDuplamenteEncadeada

# Ex. 04
# Escreva uma TAD que implemente uma lista circular ordenada duplamente
# encadeada que armazena em cada nó uma chave inteira e um nome. As
# seguintes operações abaixo devem ser definidas:
# a) Buscar um nome dado o valor da chave;
# b) Inserir um novo elemento na lista mantendo a ordem;
# c) Remover um elemento da lista;
# d) Imprimir os valores da lista;
# e) Copiar uma lista l1 para uma lista l2;
# f) Concatenar uma lista l1 com uma lista l2;
# g) Intercalar l1 e l2;

class ListaEx04(ListaDuplamenteEncadeada):
    def __init__(self, lst=None):
        super().__init__(lst)

if __name__ == '__main__':
    print('Exercício 04 da Lista de Exercícios 02')