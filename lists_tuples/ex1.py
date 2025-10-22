numbers: object = [15,33,23,90,0,4,67]
chars: object = ['q', 'w', 'e', 'r', 't']
list3 = numbers + chars

print(numbers, chars, list3)
print(f'O índice 5 da nova lista é: {list3[5]}')

for el in list3:
   print(f'{el} \n');
