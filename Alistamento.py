'''Alistamento Militar'''
from datetime import date
atual = date.today().year
print('o ano atual é {}'.format(atual))
nome = str(input('Qual o seu nome?').upper())
print('Seja bem vindo {}'.format(nome).upper())
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos de idade neste ano de {} '.format(nasc, idade, atual ).upper())
if idade == 18:
    print('Você precisa fazer o alistamento urgente {} '.format(nome).upper())
elif idade > 18:
    print('Você deveria ter se alistado desde {}'.format(nasc+18))
    print('a {} anos atras'.format(idade - 18))
else:
    print('Ainda falta {} anos para seu alistamento '.format(18-idade))

