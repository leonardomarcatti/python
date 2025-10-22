import random

number: int = 0
userNumber: int = 10
while number != userNumber:
   number = int(random.randint(0,10))
   userNumber = int(input('Digite um número entre 0 e 10 \n'))
   if number == userNumber:
      print('Acertou!')
