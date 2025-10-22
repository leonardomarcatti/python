def somar(number1:float, number2:float ):
      return float(number1 + number2)


while True:
   try:
      number1: float = float(input('Digiter um número: '))

      if number1 == 0:
          break
      number2: float = float(input('Digiter outro número: '))
      
      print(f'\n O resultado da soma entre {number1} e {number2} é: {somar(number1, number2):.2f}\n')
   except ValueError:
       print('Digite apenas números! ')