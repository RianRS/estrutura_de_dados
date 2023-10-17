# Convertendo decimal para binário
def dec2bin(n):
    b = ''
    while n != 0:
        b = b + str(n % 2)
        n = int(n / 2)
    return b[::-1]

def d2b(n):
    if n == 0:
        return ''
    else:
        return d2b(n//2) + str(n % 2)


n1 = int(input('Entre com um natural: '))
n2 = int(input('Entre com outro natural: '))
d1 = dec2bin(n1)
d2 = d2b(n2)

if d1 == d2:
    k = True
else:
    k = False

print([d1, d2], k)