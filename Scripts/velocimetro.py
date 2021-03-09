'''Detector de velocidade'''
print('lembrando que a velocidade máxima permitida é de 60km/h')
vel = float(input('Digite a velocidade do veículo: '))
exc = vel - 60
multa = exc * 7
if vel >60:
        print('O veículo recebeu uma multa de R$7,00 por kilômetro ultrapassado')
        print('Sua multa foi de R${} reais'.format(multa))
else:
    print('O veículo está dentro da velocidade permitida')