def fillInventory(inventory):
  answer = 'S'

  while answer == 'S':
    equipment = [
      input('Equipamento: '),
      float(input('Valor: ')),
      int(input('Número Serial: ')),
      input('Departamento: '),
    ]

    inventory.append(equipment)
    answer = input('Digite "S" para continuar: ').upper()
#


def listInventory(inventory):
  for item in inventory:
    print('Nome: ', item[0])
    print('Valor: ', item[1])
    print('Serial: ', item[2])
    print('Departamento: ', item[3])
#


def findBySerial(inventory, serialNumber):
  for item in inventory:
    if serialNumber == item[2]:
      print('Nome: ', item[0])
      print('Valor: ', item[1])
      print('Serial: ', item[2])
      print('Departamento: ', item[3])
      break
#


def deprecateBySerial(inventory, serialNumber):
  for item in inventory:
    if serialNumber == item[2]:
      print('Valor antigo: ', item[1])
      item[1] *= 0.9
      print('Valor atual: ', item[1])
      break
#


def removeBySerial(inventory, serialNumber):
  for item in inventory:
    if serialNumber == item[2]:
      inventory.remove(item)
      break
#


def summarizeInventory(inventory):
  values = []

  for item in inventory:
    values.append(item[1])

  if len(values) > 0:
    print('O equipamento mais caro custa: ', max(values))
    print('O equipamento mais barato custa: ', min(values))
    print('O valor total em equipamentos é de: ', sum(values))
#
