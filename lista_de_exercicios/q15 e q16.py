'Questão 15'
# Considere a lista binária [1, 1, 0, 0, 1, 1, 1, 0, 0]. Descreva usando o princí-
# pio FIFO a nova lista considerando os casos:

# (a) Início pela direita e a sequência de comandos [pop(), pop(), push(0),
# push(1),push(1), pop()].
# (b) Início pela esquerda e a sequência de comandos [push(0), push(0),
# push(1), pop(), pop()].

# RESPOSTA (a):

lista_binaria = [1, 1, 0, 0, 1, 1, 1, 0, 0]

lista_binaria.pop()
lista_binaria.pop()
lista_binaria.append(0)
lista_binaria.append(1)
lista_binaria.append(1)
lista_binaria.pop()

lista_esperada = [1, 1, 0, 0, 1, 1, 1, 0, 1]
print(lista_binaria)
print(lista_binaria == lista_esperada)

# RESPOSTA (b):

lista_binaria2 = [1, 1, 0, 0, 1, 1, 1, 0, 0]

# Inicio pela esquerda
lista_binaria2.insert(0, 0)
lista_binaria2.insert(0, 0)
lista_binaria2.insert(0, 1)
lista_binaria2.pop()
lista_binaria2.pop()

lista_esperada2 = [1, 0, 0, 1, 1, 0, 0, 1, 1, 1]
print(lista_binaria2)
print(lista_binaria2 == lista_esperada2)


'Questão 16'
# Usando o princípio FIFO, escreva em cada linha da sequência as
# operações usando push e pop.

lista = []

lista.append('a')
lista.append('b')
lista.remove('a')
lista.append('c')
lista.append('d')

lista_esperada = ['b' ,'c', 'd']
print(lista)
print(lista == lista_esperada)