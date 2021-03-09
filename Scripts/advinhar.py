from random import randint
computador = randint(0, 5) #Fazendo o computador pensar
print('-=-' *40)
print('                           Vou pensar em um número de 0 a 5, tente advinhar !')
print('-=-' *40)
jogador = int(input('Em qual número eu pensei ?  ')) #Jogador digita para tentar advinhar
if jogador == computador:
    print(' Parabéns, você acertou')
else:
    print('Eu pensei no número {} e não no {}'.format(computador, jogador))
    print('Infelizmente você errou, tente novamente.')



