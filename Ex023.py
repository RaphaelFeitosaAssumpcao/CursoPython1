# Crie um programa de multa por velocidade
velo = int(input('Qual a velocidade do seu carro? '))
if velo > 80:
    print('VOCÊ ACABA DE SER MULTADO POR ALTA VELOCIDADE! LIMITE DE 80 KM')
    multa = (velo-80) * 7
    print('O valor da multa é de {:.2f}'.format(multa))
else:
    print('Boa viagem e continue dirigindo com segurança')