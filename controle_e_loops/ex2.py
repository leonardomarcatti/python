speed: int = int(input('Qual a velocidade de seu carro (km/h)? \n'))

if speed > 80:
   tip: int = int((speed - 80)*5)
   print (f'Sua multa será de R${tip},00')
else:
   print('Você está dentro do limite de 80km/h')