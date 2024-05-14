# Crie um programa onde mostre true se você nasceu em uma cidade que possui SANTOS no nome e false para quem não nasce
cidade = str(input('Digite em que cidade você nasceu: '))
print(cidade[:5].upper().strip() == 'SANTO')