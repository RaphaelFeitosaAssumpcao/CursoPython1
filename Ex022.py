#Crie um projeto onde a nmáquina pense em um número de 0 a 5 e o usuário tente adivinhar.
import random
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-=-' * 20)
numa = random.randint(0,5) # faz o computador escolher o número
num =int(input('Digite um número de 0 a 5: ')) # jogador tenta adivinhar
print('Processando......')
sleep(3)
if num == numa:
    print('Parabéns, você acertou o número misterioso')
else:
    print('Você perdeu para a maquina, o seu número escolhido foi {} e o número que a maquina escolheu foi {}'.format(num,numa))

