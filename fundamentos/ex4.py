import math, random

number = float(input('Digite um número '))
print(f'O número digitado foi {number}. A parte ineira é: {math.floor(number)}')

name1 = input('Digite o nome 1: ')
name2 = input('Digite o nome 2: ')
name3 = input('Digite o nome 3: ')

names = [name1, name2, name3]
choise = random.choice(names)

print(choise)
