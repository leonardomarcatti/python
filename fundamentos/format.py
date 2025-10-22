color = input('Escolha uma cor: ')
# :30 significa que a string terá pelo menos 30caracteres
print('A cor é {:30}.' . format(color))
#alinhar a direita
print('A cor é {:>30}.' . format(color))
#alinhar a esquerda
print('A cor é {:<30}.' . format(color))
#centralizar
print('A cor é {:^30}.' . format(color))

n1 = 7
n2 = 3

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2



# .2f significa duas casas decimais em ponto flutuante
#end= ' ' permite a não quebra de linha 

print(f'{n1} dividido por {n2} é: {d:.2f}', end=' ')
print('ok')