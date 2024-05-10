produto = float(input('Digite o preço de um produto: '))
desconto = produto - (produto*5/100)
print('O produto que custava {:.2f}, com promoção de 5% irá custar {:.2f}'.format(produto,desconto))