import numpy as np


# Matrizes comuns
a = np.ones((3, 3)) # Tupla
print('a =', a)
b = np.zeros((2, 2)) # Tupla
print('b =', b)
c = np.eye(3)
print('c =', c)
d = np.diag(np.array([1, 2, 3, 4]))
print('d =', d)




# Operações com arrays
a = np.ones((3, 3)) # Ponto flutuante
print(type(a))
d = np.array([1 + 2j, 3+4j, 5 + 6 * 1j]) # Ponto complexo
print(type(d))
e = np.array([True, False, False, True]) # Booleano
print(type(e))
f = np.array(['Bonjour', 'Hello', 'Oi'])
print(type(f))