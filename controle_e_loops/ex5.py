'''
import time

for i in range(10, 0, -1):
   time.sleep(0.1)
   print(i)

print ('==|==|==|==|==|==|==|')

for i in range(1,51):
   if i%2 != 0:
      print(i)

print ('==|==|==|==|==|==|==|==|==|==|')

sum = 0
for i in range(1, 501):
   if i%2 != 0 and i%3 == 0:
      sum+=i

print(sum)

print ('==|==|==|==|==|==|==|==|==|==|')


number = int(input('Digite um número para saber se ele é primo '))
prime = True


if number <= 3:
   print(f'O número{number} é primo')

if number > 3:
   for i in range(1, number+1):
      if i == 1:
         continue
      
      if number%i == 0 and number != i:
         prime = False
         break


if prime == False:
   print(f'O número {number} não é primo')
else:
   print(f'O número {number} é primo')
   
'''

phrase = str(input('Digite uma frase '))
length = len(phrase)
inverse = ''
for i in range(length, 0, -1):
   inverse +=phrase[i-1]

print(inverse)

