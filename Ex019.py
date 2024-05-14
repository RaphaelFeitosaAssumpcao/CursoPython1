# Crie um programa onde mostre se o seu nome possui SILVA.
nome = str(input('Digite qual seu nome: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))