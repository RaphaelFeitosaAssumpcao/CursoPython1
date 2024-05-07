import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

#Caso queira importar somente um modulo específico podemos usar esse comando

#from math import sqrt, ceil
#num = int(input('Digite um número: ')
#raiz = sqrt(num)
#print ('A raiz de {} é igual a {}'.format(num,ceil(raiz)))

import random
num = random.randint(1,10)
print('O número aleatório que foi gerado é {}'.format(num))
