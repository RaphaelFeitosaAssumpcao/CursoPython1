#Crie um projeto onde mostre o número, o seu dobro, seu triplo e sua raiz
n = int(input('Digite um número: '))
dobro = n*2
triplo = n*3
raiz = n**(1/2)
print('O número é {}, o dobro do seu número é {}, o triplo do seu número é {}. \nA raiz quadrada é {:.2f}'.format(n,dobro,triplo, raiz))
