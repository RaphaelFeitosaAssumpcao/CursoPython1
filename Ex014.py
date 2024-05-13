# Importando a bliblioteca math, faça um programa onde mostre o seno, cosseno e tangente de um triângulo através de um ângulo
import math
a = float(input('Digite um ângulo qualquer: '))
s = math.sin(math.radians(a))
print('O ângulo de {} tem seno de {:.2f}'.format(a, s))
c = math.cos(math.radians(a))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(a,c))
t = math.tan(math.radians(a))
print('O ângulo de {} tem a tangente de {:.2f}'.format(a, t))