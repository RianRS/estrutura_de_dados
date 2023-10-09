'Questão 21'
# Descreva a lista final de acordo com a sequência de comandos indexados
# append(a)−append(b)−append(c)−insert(2, d)−insert(0, e)−append(g)

lista = []

lista.append('a')
lista.append('b')
lista.append('c')
lista.insert(2, 'd')
lista.insert(0, 'e')
lista.append('c')

lista_esperada = ['e', 'a', 'b', 'd','c', 'c']
print(lista)
print(lista == lista_esperada)