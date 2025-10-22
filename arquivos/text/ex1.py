file = open('cores.txt', 'r')
print('='*40)
print('Exibindo com for'.center(40))
print('='*40)

for color in file:
   print(color)

print('\n')
print('='*40)

file.close()

file = open('cores.txt', 'r')

print('Exibindo com while'.center(40))
print('='*40)

color = file.readline()

while len(color) > 0 :
   print(color)
   color = file.readline();


file.close()