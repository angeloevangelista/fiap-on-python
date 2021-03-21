from DictionaryFunctions import (
  find,
  insert,
  remove,
  update
)

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

def handleUserInsertion(users):
  login = input('Digite o login: ').upper()
  name = input('Digite o nome: ').upper()
  lastAccessDate = input('Digite a data do último acesso: ')
  station = input('Digite a última estação acessada: ').upper()

  insert(users, login, [name, lastAccessDate, station])
#

def handleUserSearch(users):
  login = input('Digite o login: ').upper()

  foundUser = find(users, login)

  print(foundUser)
#

def handleUserRemotion(users):
  login = input('Digite o login do usuário a ser removido: ').upper()

  remove(users, login)
#

def handleUserList(users):
  for login in users:
    print(users[login])
#
