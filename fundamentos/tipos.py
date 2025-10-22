#Números inteiros
value1 = None
value2 = None
value3 = None
value4 = None
value5 = None
value6 = None

while (value1 == None or value2 == None) :
   try :
      value1 = int(input('Digite um número: '))
      value2 = int(input('Digite outro número :'))
      soma = value1+value2
      print(f'A soma de {value1} e {value2} é: {soma}')
      
   except ValueError :
      print('Por favor digite apenas números')

#Números float
while (value4 == None or value3 == None) :
   try :
      value3 = float(input('Entre um número float: '))
      value4 = float(input('Entre outro número float: '))
      soma = value3+value4
      print(f'A soma de {value3} e {value4} é: {soma}')
   except ValueError :
      print('Por favor digite apenas números float')

#Booleanos

#Qualquer valor digitado será considerado vardadeiro.
#Se deixar em branco será considerado falso

value5 = bool(input('digite algo, ou não: '))
print(value5)

#strings
value6 = input('Digite uma palavra:')
print(value6.upper()) 
