# Crie um programa onde mostre seu nome completo e identifique quaL seu primeiro nome e seu último nome
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer {}'.format(n))
print('Seu primeiro nome é {}'.format(nome[0]))
print('O seu último nome é  {}'.format(nome[len(nome)-1]))
