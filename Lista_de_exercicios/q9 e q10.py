'Questão 9'
# Simplifique usando as propriedades da notação BIG-O os seguintes produtos.
# (a) O(n) * O(n ** c).
# (b) O(ln(n)) + O(ln(n))
# (c) O(n * c ** n).

# RESPOSTA:
# item(a) = O(n * (n ** c))
# item(b) = O(ln(n))
# item(c) = n * O(c ** n)



'Questão 10'
# Analisando a sequência de empilhamento de dados.
# Descreva manualmente a sequência de coluna em coluna usando os
# comandos push() e pop() como no modelo anterior.

# RESPOSTA:
f = []

f.append('x')
f.append('w')
f.append('k')
f.pop()
f.pop()
f.append('x')
f.append('w')
f.append('k')
f.append('y')
f.append('z')

print(f)
