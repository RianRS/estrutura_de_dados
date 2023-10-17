# Exemplo de pilha em Python
pilha = [1, 1, 2, 3, 5]
print('Pilha:', pilha)
pilha.append(8)
print('Inserindo um elemento:', pilha)
pilha.append(13)
print('Inserindo outro elemento:', pilha)
pilha.pop()
print('Removendo um elemento:', pilha)
pilha.pop()
print('Removendo outro elemento:', pilha)




# Cria uma pilha vazia
pilha = list()
print('Pilha vazia: ', pilha)


# Insere elementos na pilha
for i in range(5):
    pilha.insert(i, i)
    print('Insere o valor {0} no topo da pilha: {1}'.format(i, pilha))


# Remove elementos da pilha
while pilha:
    if not pilha:
        pass
    else:
        pilha.pop()
    print('Removendo elemento que está no topo da pilha: ', pilha)