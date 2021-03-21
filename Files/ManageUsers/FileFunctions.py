FILENAME = 'temp_users.txt'

def checkFileExistsAndCreateIt(filename = FILENAME):
  try:
    file = open(filename)
  except IOError:
    file = open(filename, 'w')
  finally:
    file.close()
#

def saveUsersToFile(dictionary, filename = FILENAME):
  checkFileExistsAndCreateIt(filename)

  with open(filename, 'w') as file:
    for (key, value) in dictionary.items():
      file.write(key + ':' + str(value) + '\n')
#

def listUsersFromFile(filename = FILENAME):
  dictionary = {}

  checkFileExistsAndCreateIt(filename)

  with open(filename, 'r') as file:
    for line in file.readlines():
      (login, data) = line.split(':')

      treatedData = []

      for rawDataItem in data.split(','):
        treatedData.append(
          rawDataItem
            .replace('[', '')
            .replace(']', '')
            .replace('\n', '')
            .replace('\'', '')
            .strip()
        )

      dictionary[login] = treatedData

  return dictionary
#
