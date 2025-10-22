exercise = input('Qual exercício quer fazer? 1 ou 2? ')

if exercise == '1':
    name = input('Qual o seu nome? ')
    day = input('Qual o dia do mês de seu nascimento? ')
    month = input('Qual o mês de seu nascimento? ')
    year = input('Qual o ano de seu nascimento? ')
    print(f'Bem-vindo {name}! Sua data de nascimento é: {day} de {month} de {year}')

elif exercise == '2':
    try:
        valor1 = int(input('Insira o primeiro valor: '))
        valor2 = int(input('Insira o segundo valor: '))
        print(f'{valor1} + {valor2} = {valor1 + valor2}')
    except ValueError:
        print('Você precisa digitar números inteiros válidos.')

else:
    print('Opção inválida. Por favor, escolha 1 ou 2.')
