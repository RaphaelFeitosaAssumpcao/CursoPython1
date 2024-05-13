# Faça um programa usando a biblioteca random e que mostre uma lista de alunos que me mostre a ordem de apresentação de um  trabalho, onde um aluno irá ganhar um bonus
import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
list = [n1,n2,n3,n4]
sorteio = random.choice(list)
print('O aluno escolhido para ganhar bonus foi {}'.format(sorteio))

random.shuffle(list)
print ('A ordem de apresentação será: ')
print(list)