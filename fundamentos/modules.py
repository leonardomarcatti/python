'''
   Existem duas formas de importação de módulos. Uma geral e uma espacífica. A geral importa todas as funcionalidades ao passo que a específica importa apenas uma.

   A sintaxe da importação geral é:
      import nome_modulo
   A específica é:
      from nome_modulo import nome_funcionalidade
'''

# import math
from math import sqrt, floor, ceil, pow, fmod
import emoji

number = int(input('Digite um número: '))
sqr = sqrt(number)
floor = floor(sqr)
ceil = ceil(sqr)
power = pow(2, number)

print(f'A raíz quadrada de {number} é {sqr} {floor} {ceil} {power}')
print(fmod(8,3))

print(emoji.emojize('Hello Emoji :pile_of_poo:'))