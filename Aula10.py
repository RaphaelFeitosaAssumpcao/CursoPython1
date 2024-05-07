#nome = str(input('Qual seu nome? '))
#if nome == 'Raphael':
#   print('Seu nome é incrível')
#else:
#    print('Que nome normal!')
#print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a nota na primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))
m = (n1 + n2) / 2

if m >= 6:
    print('O aluno foi aprovado com média de {}'.format(m))
else:
    print('O aluno reprovou com média de {}'.format(m))