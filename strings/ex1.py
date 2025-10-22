name: str =  ''
surName: str = ''

name = input('Digite o nome da pessoa ')
surName = input('Digite o sobrenome da pessoa ')

print(f'1 - {name[1]} {surName[2]}')

phrase: str = 'Curso de Python'

print(f'2 - {phrase}')
phrase2:str = phrase.replace('Python', 'SQL')
print(f'2 - {phrase2}')

colors:str = 'verde, amarelo, azul, branco, rosa, vermelho, preto'
insertedColor:str = str(input('Digiter uma cor: '))
foundcolor = insertedColor.lower() in colors
print(insertedColor, foundcolor)


if foundcolor :
   print('Cor encontrada')
else:
   print('Cor não encontrada')
   
