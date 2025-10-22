person: dict = {}

person['name'] = str.title (input('Digite o nome da pessoa '))
person['surName'] = str.title(input('Digite o sobrenome da pessoa '))
person['age'] = int(input('Digite a idade da pessoa: '))
person['weight'] = float(input('Digite o peso da Pessoa '))

print(f'{person['name']} {person['surName']} tem {person['age']} anos de idade e pesa {person['weight']}Kg')