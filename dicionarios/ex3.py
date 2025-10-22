grades: dict = {}
result: float = 0

grades[0] = int(input('Insira o valor da primeira nota: '))
grades[1] = int(input('Insira o valor da segunda nota: '))
grades[2] = int(input('Insira o valor da terceira nota: '))

print(f'As notas são: {grades[0]}, {grades[1]} e {grades[2]}')
print('Qual delas deseja deletar? \n')
print(f'1 - {grades[0]}\n2 - {grades[1]}\n3 - {grades[2]}')
del_grade: int = int(input('Digite o número da nota'))

del(grades[del_grade-1])

for i, grade in grades.items(): 
   result += grade


# result = result/len(grades)

print(f'A média das notas restantes é: {result/len(grades)}')