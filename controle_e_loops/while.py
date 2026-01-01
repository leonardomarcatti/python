import sys

try:
   n1 = int(input('Digite o primeiro número: '))
   n2  = int(input('Digite o segundo número: '))
except ValueError:
   print('Digite apenas números')
   sys.exit('Encerrado')

while n1 != 0 and n2 != 0:
   soma = n1 + n2
   print(f'{n1} + {n2} = {soma}')
   n1 = 0

'''
x: int = 0

while x <=10 :
   if x%2 == 0:
      print(f'{x} é par')
      x+=1
      continue
   print(f'{x} é ímpar')
   x+=1

'''
   
