from math import floor

name = input('Digite seu nome completo ')
name_upper = name.upper()
name_lower = name.lower()
name_split = name.split(' ')
first_name_length = len(name_split[0])
first_name = name_split[0]
no_space = len(name.replace(' ', ''))

print(f'{name_upper}')
print(f'{name_lower}')
print(f'{no_space}')
print(f'{first_name_length}')
print(f'{first_name}')

number = int(input('Digite um número entre 0 e 999: '))

c = floor(number/100)
d = floor(number/10) % 10
u = number%10


print(f'Unidade {u}, Dezenas: {d}, Centenas: {c}')

city = input('Digite o nome da cidade: ')
city = city.lower()

result = city.startswith('são')
print(result)