cars_list: dict = { 'Uno': {'year': 2002, 'value': 'R$ 12.000,00'}, 'Gol': {'year': 2002, 'value': 'R$ 30.000,00'}, 'Onix': {'year': 2025, 'value': '20.000,00'}, }

car: str = input('Digite o nome do carro: ').title()

print(car.title())

found_car = car in  cars_list

if found_car :
   print(f'O carro {car} é do ano {cars_list[car]['year']} e custa {cars_list[car]['value']}')

else :
   print('Não temos esse carro')