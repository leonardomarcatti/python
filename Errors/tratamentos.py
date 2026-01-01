import math
import sys



print('='*100)
print('Digite um número para calcular a raíz quadrada ou 0 para sair'.center(100))
print('='*100)

try:
   insert: int = int(input('Insira um número: '))
   
except ValueError:
   print('Digite apenas números')
   sys.exit('Encerrado')

newNumber: str = '' 

while insert != 0 and (newNumber == 's' or newNumber == ''):
   if newNumber != '':
      insert: int = int(input('Insira um número: '))

   if insert == 0:
      sys.exit('Saíndo')
   if insert < 0 :
      sys.exit('Não é possível calcular raíz de números negativos')
   else :
      print (f'{math.sqrt(insert):.4f}')
      print('Deseja calcular outro número? S para Sim ou N para Não')
      newNumber = input('Digite sua resposta: ').strip().lower()
