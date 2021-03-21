from functions import *

inventory = []
answer = 'S'

fillInventory(inventory)

listInventory(inventory)

findBySerial(
  inventory,
  serialNumber = int(
    input('\nDigite o serial do equipamento que deseja buscar: ')
  )
)

deprecateBySerial(
  inventory,
  serialNumber = int(
    input('\nDigite o serial do equipamento que será depreciado: ')
  )
)

removeBySerial(
  inventory,
  serialNumber = int(
    input('\nDigite o serial do equipamento que será removido: ')
  )
)

summarizeInventory(inventory)
