# Importando a biblioteca math, faça um programa onde mostre o valor da hipotenusa de um triângulo.
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))