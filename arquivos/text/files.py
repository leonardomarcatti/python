# cars = open('carros.txt', 'r')
# lines = cars.read()
# print(lines)
# cars.close()

# *Quando o arquivo não existe ele é criado automaticamente

# # !w apaga tudo e reescreve o conteúdo
# furniture = open('moveis.txt', 'w')
# furniture.write('Armário\n')
# furniture.write('Guarda Roupas\n')

# furniture.close()

# # !a adiciona um texto
# tech = open('tecnologia.txt', 'a')
# tech.write('Video Game\n')
# tech.close()

#strings e listas

# ! Limpar espaços desnecessários
bkp = open('bkp.txt', 'r')
line = bkp.readline()
while len(line) >0 :
   cod = line[0:5].strip()
   name = line[5:45].strip()
   tel = line[45:65].strip()
   email = line[65:90].strip()
   
   print(f'\nCod..... {cod}')
   print(f'Nome..... {name}')
   print(f'Telefone..... {tel}')
   print(f'Email..... {email}')

   line = bkp.readline()
   
bkp.close()
