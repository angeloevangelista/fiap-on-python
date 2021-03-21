from UserHandlers import (
  requestOption,
  handleUserList,
  handleUserSearch,
  handleUserRemotion,
  handleUserInsertion,
)

option = requestOption()

while option == 'I' or option == 'P' or option == 'E' or option == 'L':
  if option == 'I':
    handleUserInsertion()
  if option == 'P':
    handleUserSearch()
  if option == 'E':
    handleUserRemotion()
  if option == 'L':
    handleUserList()

  option = requestOption()
