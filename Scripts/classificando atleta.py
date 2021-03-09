from datetime import date
ano = date.today().year
print('-='*40)
print('-'*60)
print('            CATEGORIA DO ATLETA')
print('-'*60)
print('-='*40)
nome = str(input('NOME DO ATLETA: ').upper())
print('_'*40)
print('Seja bem vindo {} agora informe o ano de nascimento'.format(nome).upper())
nasc = int(input('Ano de nascimento: '))
idade = ano - nasc
print('O atleta tem {} anos de idade'.format(idade))
if idade <=9:
    print('CLASSIFICAÇÃO MIRIM')
elif idade <=14:
    print('CLASSIFICAÇÃO INFANTIL')
elif idade <=17:
    print('CLASSIFICAÇÃO JUVENIL')
elif idade <=26:
    print('CLASSIFICAÇÃO ADULTO')
elif idade <= 30:
    print('CLASSIFICAÇÃO SÊNIOR')
elif idade <= 35:
    print('CLASSIFICAÇÃO MASTER')
elif idade <=40:
    print('CLASSIFICAÇÃO MASTE 1')
elif idade <= 45:
    print('CLASSIFICAÇÃO MASTER 2')
else:
    print('CLASSIFICAÇÃO MASTER 3')

