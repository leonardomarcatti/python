print('+-/*=' * 8)
print('C A L C U L A D O R A'.center(40))
print('+-/*=' * 8)


def soma(a, b): return a + b
def subtrai(a, b): return a - b
def divide(a, b): return a / b
def multiplica(a, b): return a * b

operation: dict = {1: soma, 2: subtrai, 3: divide, 4: multiplica}

def menu():
   print('1 - Somar\n2 - Subtrair\n3 - Dividir\n4 - Multiplicar\n0 - Sair');
   global operation
   while True: 
      inserted_operation = int(input('Digite a operação: '))
      if operation == 0 or (inserted_operation not in operation):
         break

      print('Digite dois números ')
      n1:float = float(input('Digiter o prieiro número: '))   
      n2:float = float(input('Digiter o prieiro número: '))   
      result: float = operation[inserted_operation](n1, n2)
      print(result)
      break

menu()