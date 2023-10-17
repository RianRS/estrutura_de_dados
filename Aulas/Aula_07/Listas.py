# Lista indexada
inicio = int(input('Entre com um inteiro: '))
fim = int(input('Entre com outro inteiro: '))
passo = int(input('Entre com o tamanho do passo: '))

for i in range(inicio, fim, passo):
    print(i)




# Listas baseadas em critérios de parada e uma classe para implementar uma iteração de força 2
class PowTwo:

    def __init__(self, max = 0 ):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

# Criando um objeto
numbers = PowTwo(4)

# Criando uma iteração do objeto
i = iter(numbers)

# Usando next para obter a próxima iteração do elemento
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
