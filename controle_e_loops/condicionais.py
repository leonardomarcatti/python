age: int = int(input('Digite sua idade: '))

if age < 18:
   print('Você não pode entrar')


if age >= 18 and age <=21:
   print('Vc pode beber apenas refrigerante')

if age > 21 and age <=60:
   print('Vc pode beber cerveja ou vodka')

if age > 60:
   print('Vc pode beber apenas água')