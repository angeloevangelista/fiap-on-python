inventory = []
answer = 'S'

while answer == 'S':
  inventory.append(input('Equipamento: '))
  inventory.append(float(input('Valor: ')))
  inventory.append(int(input('Número Serial: ')))
  inventory.append(input('Departamento: '))

  answer = input('Digite "S" para continuar: ').upper()

for item in inventory:
  print(item)
