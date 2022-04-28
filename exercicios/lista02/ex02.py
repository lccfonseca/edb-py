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

class ListaEx02(Lista):

    def __init__(self, lst=None):
        super().__init__(lst)


if __name__ == '__main__':
    print('Exercício 02 da Lista de Exercícios 02')