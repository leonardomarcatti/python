myDic: dict = {'name': 'Leo', 'age': 46, 'height': 180, 'weight': 84.5}
print(f'1 - Nome: {myDic['name']}, Idade: {myDic['age']}, Altura: {myDic['height']}, Pseo: {myDic['weight']}')

myDic2: dict = {}

myDic2['a'] = 'Teste'
myDic2[1] = 200
myDic2['c'] = 12.3

print(myDic2)

value = myDic.get('name')
values = myDic.values()
keys = myDic.keys()

if value:
   print(value);

print(values, keys)

del(myDic['height'])
print(myDic)

friends: dict = {'Ana': 123, 'Carlos': 456, 'João': 789}

friend = 'João' in friends

print(friend)

friends.pop('João')
print(friends)

keys = ['a', 'b', 'c']
values = [1, 2, 3]

print(dict(zip(keys, values)))