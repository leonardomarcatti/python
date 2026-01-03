import math, os


number:int = int(input('Digite um número: '))
os.system('cls' if os.name == 'nt' else 'clear')

try:
   value = (math.sqrt(number))
   
   print(f'A raíz quadrada de {number} é {value:.4f} ')
except ValueError:
   print('Não é possível calcular raíz de números negativos')

except Exception:
   print('Não é possível calcular')

finally:
   print('Obrigado por calcular conosco!')

   