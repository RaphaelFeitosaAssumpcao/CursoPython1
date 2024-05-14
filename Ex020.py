# Crie um programa onde mostre o  número de vezes que a letra 'A' aparece e qual a posição do último "A"
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A última letra "A" apareceu na posição {} da frase'.format(frase.rfind('A')))