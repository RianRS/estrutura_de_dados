'Questão 1'
# Seja a somatório do quadrado de n naturais descrito por
# SOMATÓRIO de k ** 2 = 1 ** 2 + 2 ** 2 + 3 ** 2 + ...(n) ** 2

# (a) Construa um código Python de forma manual usando um laço de
# repetição que retorne corretamente o valor desta soma e teste-o se
# possível.
# (b) Usando esse código, calcule a soma para n = 500. Demonstre o
# mesmo valor de forma analítica.
def soma_quadrados(num):
    soma = 0
    for item in range(num + 1):
        soma += item ** 2
    return soma

print(soma_quadrados(500))



'Questão 2'
# Veja o código que usa a definição de operador de fatia

# d1 = [:]
# d2 = [2:]
# d3 = [2:7]
# d4 = [5:]
# print('[{}, {}, {}, {}]'.format(8, 5, 6, 9))

# (a) Descreva a saída deste código como uma lista.
# (b) Descreva a sintaxe genérica no python do operador de fatia.
