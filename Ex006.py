#Crie um projeto que mostre a primeira nota do aluno, a segunda e que faça uma média.
nota1 = float(input('Digite a nota 1 do aluno: '))
nota2 = float(input('Digite a nota 2 do aluno: '))
media = (nota1+nota2)/2
print('A primeira nota do aluno é {:.1f}, a segunda nota do aluno é {:.1f}, a média do aluno é {:.1f}'.format(nota1,nota2,media))
