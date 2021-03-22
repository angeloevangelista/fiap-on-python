import pathlib

filePath = f'{pathlib.Path(__file__).parent.absolute()}/iris.data'

database = []

with open(filePath, 'r') as file:
  for line in file.readlines():
    line = line.replace('\n', '')

    if line != '':
      database.append(line.split(','))

print(float(database[0][0]) + float(database[0][1]))
