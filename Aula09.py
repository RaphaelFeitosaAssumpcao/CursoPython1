frase = 'Curso em video python'
#ler a quantidade de espaços da string
print(len(frase))
#ver a quantidade de letras em uma string
print(frase.count('o',0,13))
#Dizer quantas vezes encontrou um valor
print(frase.find('deo'))
#Dizer se existe o valor na string
print('Curso' in frase)
#Para reposicionar a string substituindo ou mudando ordem
print(frase.replace('python','Android'))
#Colocar o que não era maiúsculo em maiúsculo
print(frase.upper())
#Colocar tudo que estiver em maiúsculo em minusculo
print(frase.lower())
#Colocar todos os começos de palavras com letra maiúscula
print(frase.title())
#Jogar todos os caracteres pra minusculo e a primeira letra da primeira palavra vai ficar em maiúsculo
print(frase.capitalize())
#Remover todos os espaços inúteis da string, se colocamos o r antes do strip somente irá tratar os espaços da direita e se colar l irá tratar da esquerda
print(frase.strip())
#Divisão dentro da sua string usando os espaços vazio
print(frase.split())
#Junção de espaços separados em listas
print('-'.join(frase))