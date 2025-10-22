numbers: list = []
names: list = []
contacts: dict = {}


new_name: str = ''
new_number: int = 0

while True:
   new_name: str = str(input('Digite um nome ou X para sair \n'))
   if new_name.lower() == 'x':
      break
   
   new_number = int(input('Digite o número do contato: \n'))
   numbers.append(new_number)
   names.append(new_name)
   contacts = dict(zip(names, numbers))

print(contacts)
