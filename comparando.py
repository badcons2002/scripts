n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 > n2:
    print('este número {} é maior que {} '.format(n1, n2))
elif n1 < n2:
    print('este número {} é menor que {} '.format(n1, n2))
else:
    print('esses números são iguais')