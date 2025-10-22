number: int = int(input('Digite um número: '))
result = number%2

if result == 0:
   print(f'{number} é par')
else:
   print(f'{number} é impar')