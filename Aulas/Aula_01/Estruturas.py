# Instrução if multidirecional
x = float(input('Value x: '))
y = float(input('Value y: '))
if x > y:
     print('x is greater than y')
elif x < y:
     print('x is less than y')
else:
     print('x is equal to y')


# Instruções de laços de repetições
product = 1
value = 1
while value <= 10:
     product *= value
     value += 1
print(product)

product = 1

for value in range(1, 11):
    product *= value
print(product)

for expoent in range(7,11):
    print(expoent, 10 ** expoent)