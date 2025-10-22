
myString: str = 'Curso de Python 3'
myArray: object = ['a', 1, 'b', 2, 'c', 3]

inString = 'o' in myString
inArray = 'd' not in myArray

print(f'1 - A letra \'o\' está na frase {myString}? \n {inString} ')
print(f'2 - A letra \'d\' não está no array {myArray}? \n {inArray} ')



myString: str = 'aaassffhg'

response: dict[str, int] = {}

for char in myString:
   if char in response:
      response[char] += 1
   else:
      response[char] = 1;


print(f'3 - {response}')

for i,el in response.items():
   print(f'4 - {el, i}')

idade = 46
peso = 80.45

print(type(idade), type(peso))