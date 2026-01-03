import math
import sys, os

print('='*50)
print('CALCULADORA'.center(50))
print('='*50)

def getInputs():
   try:
      print('Escolha uma operação.')
      print('\33[31mA para ADIÇÃO\33[m\n\33[32mS para SUBTRAÇÃO\33[0m\n\33[33mM para MULTIPLICAÇÃO\33[0m\n\33[34mD para DIVISÃO\33[0m\n\33[35mP para POTÊNCIA\33[0m\n\33[36mR para RAÍZ QUADRADA\33[0m\n\33[37mDigite outra coisa para sair do programa\33[0m')
      numbers: list[int] = []
      operation:str = input('Insira a operação: ').strip().lower()

      if operation in ['a', 's', 'm', 'd', 'p']: 
         numbers.append(int(input('Insira um número: ')))
         numbers.append(int(input('Insira um número: ')))
         return [numbers, operation]
      
      if operation == 'r':
         numbers.append(int(input('Insira um número: ')))
         return [numbers, operation]
      else:
         sys.exit('Operação inexistente. Encerrado programa')

   except Exception:
      sys.exit('Digite apenas números. Encerrado programa')

def calculate(numbers, operation):
   if operation == 's' :
      return numbers[0]-numbers[1]
   
   if operation == 'a' :
      return numbers[0]+numbers[1]
   
   if operation == 'd':
      if numbers[1] == 0:
         sys.exit('Erro: divisão por zero.')
      return numbers[0] / numbers[1]
   
   if operation == 'm' :
      return numbers[0]*numbers[1]
   
   if operation == 'r' :
      return math.sqrt(numbers[0])
   
   if operation == 'p':
      return math.pow(numbers[0], numbers[1])
   
   sys.exit('Encerrado programa')
   
inserts = getInputs()

newNumber: str = '' 

while inserts:
   print(calculate(inserts[0], inserts[1]))
   newNumber = input('Deseja fazer outra operação? S para SIM ou N para NÃO\n').strip().lower()
   os.system('cls' if os.name == 'nt' else 'clear')
   if newNumber == 's':
      inserts = getInputs()

   if newNumber != 's':
      break