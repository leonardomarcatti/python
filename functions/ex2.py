import locale

try:
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
except:
    locale.setlocale(locale.LC_MONETARY, 'Portuguese_Brazil.1252')

cars: list = [['Fiat Argo', 48300], ['Hyundai HB20', 35890], ['VW T-Cross', 105200], ['GM Onyx', 44800], ['Ford Focus', 58200], ['Toyota Corolla', 280000], ['Honda Civic', 90000]]

print(f'\n{"Código".center(12)} {"Modelo".center(24)} {"Preço".center(10)}')
print('-' * 50)

for i, car in enumerate(cars):
   print(f'{str(i).center(12)}{car[0]:<25}{locale.currency(car[1], grouping=True):<10}')


code: int = int(input('\nDigite o código do carro '))

selected_car = cars[code]

print(f'O carro {selected_car[0]} custa {locale.currency(selected_car[1], grouping=True)}')
