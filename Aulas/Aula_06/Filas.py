# Inicializando uma fila vazia
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print('Initial queue')
print(queue)

print('\nElements dequeue from queue')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print('\nQueue after removing elements')
print(queue)




# Processos de agendamento de uma CPU
from collections import deque

fila = deque(['A', 'B', 'C'])

# Inserindo o elemento D
fila.append('D')

# Removendo o elemento A
fila.popleft()

print(fila)