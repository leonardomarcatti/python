import os
import shutil

# Retorna diretório atual
print(os.getcwd())

#Muda de diretório
os.chdir('/app/pdf')
print(os.getcwd())

#Deleta arquivos
# os.remove('Teste')

# Cria um diretório dentro do diretório atual
os.mkdir('Teste')

print(os.listdir())

#Deleta diretórios
# shutil.rmtree('Teste2')

print(os.listdir())

# Cria um diretório dentro do diretório atual
# os.mkdir('Teste')

# Lista arquivos e diretórios
print(os.listdir())

#Renomeia arquivos
os.rename('Teste', 'Teste2')

print(os.listdir())