names: object = []

while True:
   newName = str(input('Digite um nome: ')).strip()
   if newName == '':
      break;

   names.append(newName)


names.sort()
print(names)

print('Você deve deletar um dos nomes da lista')
print('Digite um número correspondente para o nome')

for i, name in enumerate(names):
   print(f'{i} - {name}');

deleteName: int = int(input(f'Digite um número entre 0 e {len(names) - 1}: \n'))

if deleteName < len(names):
   print(f'Você deletou {names[deleteName]}')
   del(names[deleteName])
else:
   print('O número digitado não corresponde a um nome válido')
   

print(f'Sua nova lista é: \n {names}')
   