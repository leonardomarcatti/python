import random

number: int = random.randint(0,5)
choose: int = int(input('Digite um número entre 0 e 5: '))

if number == choose:
   print('Você acertou o número')
else :
   print(f'Você errou. O número secreto é {number}')