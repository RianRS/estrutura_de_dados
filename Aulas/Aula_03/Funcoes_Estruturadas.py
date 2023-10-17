import time

# Algoritmo 1
problemSize = 10000000
print('%12s%16s' % ('Problem Size', 'Seconds'))
for count in range(5):
    start = time.time()
    # Início do algoritmo
    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1
    # Fim do algoritmo
    elapsed = time.time() - start
    print('%12d%16.3f' % (problemSize, elapsed))
    problemSize *= 2




# Algoritmo 2
problemSize = 1000
print('%12s%15s' % ('Problem Size', 'Iterations'))
for count in range(5):
    number = 0
    # Início do algoritmo
    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            number += 1
            work += 1
            work -= 1
    # Fim do algoritmo
    print('%12d%15d' % (problemSize, number))
    problemSize *= 2




# Sequencia Fibonacci
n = int(input('Entre com um número natural: '))
def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n - 2)
t = fib(n)
print(t)