equipments = []
values = []
serialNumbers = []
departments = []

answer = 'S'

while answer == 'S':
  equipments.append(input('Equipamento: '))
  values.append(float(input('Valor: ')))
  serialNumbers.append(int(input('Número Serial: ')))
  departments.append(input('Departamento: '))

  answer = input('Digite "S" para continuar: ').upper()

for index in range(0, len(equipments), 1):
  print('\nEquipamento: ', index + 1)
  print('Nome: ', equipments[index])
  print('Valor: ', values[index])
  print('Serial: ', serialNumbers[index])
  print('Departamento: ', departments[index])
