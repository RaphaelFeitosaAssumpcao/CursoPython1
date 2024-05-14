# Crie um programa onde leia seu nome completo, mostre seu nome inteiramente em minúsculo e maiúsculo, que conte o número de letras do seu nome todo e do seu primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))