from edb.basico.pilha import Pilha

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    p = Pilha()
    print('Exemplos de operações com pilhas')
    print('Empty:', p.is_empty())
    p.push(1)
    p.push(2)
    p.push(3)
    p.push(4)
    p.push(5)
    print('Top:', p.top())
    print('Size:', p.size())
    print('Empty?', p.is_empty())
    print('Pop:', p.pop())
    print('Pop:', p.pop())
    print('Size:', p.size())
