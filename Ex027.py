# Faça um programa onde mostre o salário do funcionário
# se for menor ou igual a R$1250 tem um aumento de 10%
# se for maior um de 15%
salario = int(input('Digite o salário do funcionário:R$ '))
if salario <= 1250:
    aumento = salario * (10/100)
    salario2 = aumento + salario
    print(salario2)
else:
    aumento = salario * (15/100)
    salario2 = aumento + salario
    print(salario2)