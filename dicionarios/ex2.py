apto_list: dict = {}
apto_number: int = 00
apto_owner: str = ''

while apto_list != 0 and apto_owner != '' :
   apto_number = int(input('Digite o número do apartamento: '))
   apto_owner = str(input('Digite o nome do dono do apartamento: '))
   apto_list[apto_number] = apto_owner


print(apto_list)