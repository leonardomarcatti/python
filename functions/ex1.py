print('+-/*=' * 8)
print('INVERSOR DE PALAVRAS'.center(40))
print('+-/*=' * 8)

word: str = str(input('Digite uma palavra: '))


def reverse_word(word: str) -> str:
   inverted: str = ''
   inverted = word[::-1]
   return inverted
      
if word == reverse_word(word) :
   print('Palíndromo')

else :
   print('Error')

