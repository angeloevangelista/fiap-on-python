users = {}
emails = ['xpto@xyz.com', 'xkcd@phd.com']

myTuple = list(enumerate(emails))

for index in range(0, len(myTuple)):
  print('Email: ', myTuple[index][1])

  name = input('Digite o nome: ')
  level = input('Digite o de acesso: ')

  users[myTuple[index]] = [name, level]

for (key, data) in users.items():
  print('Usuário: ', key[0])
  print('Email: ', key[1])
  print('Nome: ', data[0])
  print('Nível: ', data[1])
