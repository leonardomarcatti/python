estate: int = int(input('Qual o valor do imóvel? '))
salary: float = float(input('Qual o valor de seu salário? '))
years: int = int(input('Em quantos anos deseja pagar? '))
fee: float = 3/10

monthly_pay = estate/(years*12)
limit = salary*fee

if monthly_pay > limit:
   print(f'O pagamento mensal de {monthly_pay} é maior que seu limite de {limit}')

else:
   print('Crédito aprovado!')

