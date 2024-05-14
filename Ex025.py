# Crie um programa onde calcule o preço de uma viagem que se a viagem for maior ou igual a 200 km o valor é multiplicado por 0.45 caso contrário por 0.50
dist = int(input('Digite a distância da viagem: '))
print('Você está prestes a começar uma viagem de {} km.'.format(dist))
if dist >= 200:
    preço = dist * 0.45
else:
    preço = dist * 0.50
print('O valor da sua viagem de {} km é de R${}'.format(dist,preço))