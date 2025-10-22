for i in range(1,3):
   print(f'O valor é: {i}')

for i in range(3,1,-1):
   print(f'O valor é: {i}')

print('Start')

for num in range(5):
   
   if num == 2:
      break
   
   print(num)


print('End')

for c in 'Curso de Python':
   if c in 'yrh': # Equivalente a c == 'y' || c == 'r' || c == 'h'
      continue
   print(c)
   
