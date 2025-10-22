
myList = [0,1,2,3,4,5,6,7,8,9,10]

numbers = [1,2,3,4,5]
print(f'1 - {numbers}')

for i in numbers:
   print(f'2 - {i}');


myList = list('Python')
print(f'3 - {myList}')



numbers = [1,2,3,4,5]
char = ['a', 'b', 'c']
mix = numbers + char
print(f'4 - {mix}')

numbers.append(6) # insere no final
print(f'5 - {numbers}')
numbers.insert
numbers.pop() # remove do final
print(f'6 - {numbers}')
del(numbers[2]) # deleta um índice se for -1 deleta o último elemento
print(f'7 - {numbers}')

lista = [['Ana', 'João', 'julia'], [30, 5, 80]]
print(f'8 - A pessoa {lista[0][0]} tem {lista[1][0]} anos')
print(f'9 = A pessoa {lista[0][-1]} tem {lista[1][-1]} anos')


i = 0
qte = len(myList)

while i < qte:
   print(f'10 - {myList[i]}')
   i += 1;

for item in myList:
   print(f'11 - {item * 20}');

for index, element in enumerate(myList):
   print(f'12 - {index}, {element*10}');

#Fatias
myList2 = myList[3:6] 
even = myList[::2] # Pega do primeiro até o último de 2 em 2
print(f'13 - {myList2}, {myList}, {even}')


myList3 = ['Ana', 'Maria', 'João', 'Lucas']
myList3.append('Inserido no final') #insere no final
myList3.insert(0, 'Inserido no início') #insere em um determinado índice. Nesse caso no início
print(f'14 - {myList3}')
del(myList3[2:5]) #deleta uma fatia
print(f'15 - {myList3}')


myList3.clear() # limpa a lista
print(f'16 - {myList3}')

unorderedList = ['c', 'b', 'a', 'e']

unorderedList.sort() #Ordena a lista
unorderedList.reverse() #Inverte a lista
print(f'17 - {unorderedList}')
print(f'18 - {len(unorderedList)}')


myList = ['a', 's', 'd', 'f', 'q', 'w', 'e', 'r', 't', 'a', 'f', 'f']
phrase: str = 'Curso de Python na Udemy'
myList.sort()
print(f'19 - {myList}')
del(myList[-1])
print(f'20 - {myList}')
print(f'21 - {myList.count('f')}') # conta aquantidade de determinado elemento na lista
print(f'22 - {phrase.count('o')}') # conta aquantidade de determinado elemento na lista
