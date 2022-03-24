from edb.basico.pilha import Pilha


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

p = Pilha()

print('Exemplos de operações com pilhas')
print(p.is_empty())
p.push(5)
p.push('python')
print(p.peek())
p.push(True)
print(p.size())
print(p.is_empty())
p.push(11.5)
print(p.pop())
print(p.pop())
print(p.size())
