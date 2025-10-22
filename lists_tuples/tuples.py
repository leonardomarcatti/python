'''
   Para ser considerada uma tupla é necessário uma vírgula no elemento.
   Para defiinitr uma tuple usamos parenteses mas não é obrigatório.
   Tuplas são imutáveis
'''
t1 = (1,2)
t2 = (1)
t3 = 'a', 2, True, [1,2,3]
t4 = tuple('Python3')
print(type(t1), type(t2), type(t3), type(t4))
print(t4)