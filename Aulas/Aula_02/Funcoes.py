# Retorna a razão entre dois floats mediante uma condição
lower = float(input('Insira o número à esquerda: '))
upper = float(input('Insira o número à direita: '))

def displayRange(lower, upper):
    if lower < upper:
        return 0
    else:
        return lower/upper
t = displayRange(lower, upper)
print(t)




# Fatorial de um número
n = int(input('Entre com um número inteiro: '))
def factorial(n, product = 1):
    if n == 1:
        return product
    else:
        return factorial(n - 1, n * product)
n1 = factorial(n, 1)
print('O fatorial de', n, 'é', n1)




# Média de valores
def media(parametro = []):
    list(parametro)
    for index in range(len(parametro)):
       return sum(parametro)/len(parametro)

print(media(parametro = [10, 9, 2]))