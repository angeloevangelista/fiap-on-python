from FileFunctions import (listUsersFromFile, saveUsersToFile)

def requestOption():
  selectedOption = input(
    'O que deseja fazer?\n'
    + '<I> - Inserir um usuário.\n'
    + '<P> - Pesquisar um usuário.\n'
    + '<E> - Excluir um usuário.\n'
    + '<L> - Listar usuários.\n'
  ).upper()

  return selectedOption
#

def handleUserInsertion():
  users = listUsersFromFile()

  login = input('Digite o login: ').upper()
  name = input('Digite o nome: ').upper()
  lastAccessDate = input('Digite a data do último acesso: ')
  station = input('Digite a última estação acessada: ').upper()

  users[login] = [name, lastAccessDate, station]

  saveUsersToFile(users)
#

def handleUserSearch():
  users = listUsersFromFile()
  login = input('Digite o login: ').upper()

  foundUser = users[login]

  print(foundUser)
#

def handleUserRemotion():
  login = input('Digite o login do usuário a ser removido: ').upper()

  users = listUsersFromFile()

  users.pop(login, None)
  saveUsersToFile(users)
#

def handleUserList():
  users = listUsersFromFile()

  for login in users:
    print(users[login])
#
