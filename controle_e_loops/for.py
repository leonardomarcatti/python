forOne: object = []
forTwo: object = []

for i in range(1,10):
   forOne.append(i)

print(forOne)

print('='*20, '\n')

for i in range(10,1,-1):
   forTwo.append(i)

print(forTwo)

print('='*20, '\n')

for num in range(5):   
   if num == 2:
      break
   print(num)


print('='*20, '\n')

phrase = 'Curso de Python'
short_phrase: str = ''

for element in phrase:
   if element in 'yrh': # Equivalente a c == 'y' || c == 'r' || c == 'h'
      continue
   short_phrase += element
   
print(short_phrase)
   
