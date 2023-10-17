# Função de pesquisa linear
def pesquisa_linear(arranjo, elemento_desejado):
    for elemento in arranjo:
        if elemento == elemento_desejado:
            print('Elemento {} está presente no arranjo.'.format(elemento_desejado))
            return
    print('Elemento {} não está presente no arranjo.'.format(elemento_desejado))

pesquisa_linear([10, 10, 20, 30, 50, 80, 130], 130)




# Função de pesquisa binaria
def pesquisa_binaria(A, item):
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if A[meio] == item:
            return meio
        elif A[meio] > item:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return -1

A = [0, 10, 20, 30, 40, 50, 60, 70]
print('Pesquisa com sucesso:', pesquisa_binaria(A, 60))