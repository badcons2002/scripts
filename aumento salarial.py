'''Aumento salarial '''
#Para salário acima de R$1250 aumento de 10% e se inferior 15%
print('Vamos dar um aumento salarial, vamos ver como fica o novo salário !')
sal = float(input('Digite o salário atual: '))
dez = sal*10/100 + sal
quinze = sal*15/100 + sal
if sal >=1250:
    print('Seu novo salário é de {}'.format(dez))
if sal < 1250:
    print('Seu novo salário é de {} '.format(quinze))

