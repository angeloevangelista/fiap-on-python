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

search = int(input('\nDigite o serial do equipamento que deseja buscar: '))

for index in range(0, len(serialNumbers)):
  if search == serialNumbers[index]:
    print('Equipamento: ', equipments[index])
    print('Serial: ', serialNumbers[index])
    print('Valor: ', values[index])
    print('Departamento: ', departments[index])
    break
