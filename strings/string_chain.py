
phrase = ' Eu sou uma frase '

#[x:y] x é considerado porém y não

print(f'1 - {phrase}')
print(f'1 - {phrase}')
print(f'2 -  {phrase[3:5]}') #Uma fatia do índice 3 ao índice 4
print(f'3 - {phrase[:5]}') # Conta até o índice 4 a partir do início
print(f'4 - {phrase[5:]}') # Conta a partir do índice até o fim
print(f'5 -  {phrase[:-5]}') #Conta do íncio até a regressiva 5
print(f'6 -  {phrase[0::3]}') #pula de 2 em 2 caracteres
print(f'7 - Tamanho da string: {len(phrase)}') # Comprimento da string
print(f'8 - {phrase.count('s')}') # número de ocorrências
print(f'9 - {phrase.find('sou')}') # índice onde começa
print(f'9 - {"sou" in phrase}') # existe ocorrência ou não
print(f'10 - {phrase.replace('frase', 'teste')}')
print(f'11 - {phrase.capitalize()}')
print(f'12 - {phrase.title()}')
print(f'13 - {phrase.strip()}')
print(f'6 -  {phrase[::-1]}') # Inverte a palavra

string =  '1,2,3,4,5,6'

print(f'14 - {string.split(',')}') #separa por caractere específico
print(f'15 - {string.split(',', maxsplit=1)}') #separa apenas o primeiro item

split = phrase.split()
print('|-|'.join(split))