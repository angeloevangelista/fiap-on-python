from UserHandlers import (
  requestOption,
  handleUserList,
  handleUserSearch,
  handleUserRemotion,
  handleUserInsertion
)

users = {}

option = requestOption()

while option == 'I' or option == 'P' or option == 'E' or option == 'L':
  if option == 'I':
    handleUserInsertion(users)
  if option == 'P':
    handleUserSearch(users)
  if option == 'E':
    handleUserRemotion(users)
  if option == 'L':
    handleUserList(users)

  option = requestOption()
