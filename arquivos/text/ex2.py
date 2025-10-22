car_list: list = []

while True :
   car:str = str(input('Digite um fabricante e nome de carro: '))

   if car == '':
      break;
   
   car_list.append(car);

file = open('carList.txt', 'a')

for car in car_list:
   file.write(f'{car} \n');

