import math

number = int(input('Digite um número: '))

double = number*2
triple = number*3
sqr = number**0.5

print(f'O número digitado foi: {number}. \nSeu dobro é : {double}, seu triplo é: {triple} e sua raíz quadrada é: {sqr}')

print(f'Tabuada do número {number}')

for i in range(1,11):
   print (f'{number} x {i} = {number*i} ')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

avg = (n1+n2)/2
std_deviation = math.sqrt( (math.pow((n1-avg), 2) + math.pow((n2-avg), 2))/2 )

print(f'A média dos números {n1} e {n2} é {avg}')
print(f'O desvio padrão dos números {n1} e {n2} é {std_deviation}')