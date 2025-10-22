people = [
   ['1', 'José da Silva', '123456789', 'josedasilva@teste.com'],
   ['2', 'Maria Rosa', '987654321', 'mariarosa@teste.com'],
   ['3', 'Enzo costa', '147852369', 'enzocosta@teste.com'],
   ['4', 'Valentina Pereira', '369852147', 'valentinapereira@teste.com'],
]

bkp = open('bkp.txt', 'w')


print(f'{"COD":<5} {"NOME":<40}  {"TELEFONE":<20} {"EMAIL".center(15)}')
for i, el in enumerate(people):
   if i == 0:
      bkp.write(f'{"COD":<5} {"NOME":<40}  {"TELEFONE":<20} {"EMAIL".center(15)}\n')
   bkp.write(f'{el[0]:<5} {el[1]:<40} {el[2]:<20} {el[3].center(15)}\n')
   print(f'{el[0]:<5} {el[1]:<40} {el[2]:<20} {el[3].center(15)}')

bkp.close()