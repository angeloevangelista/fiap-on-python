name = input('Digite o nome: ')
age = int(input('Digite a idade: '))

infectiousAndContagiousDisease = input(
  'Suspeita de doença infectocontagiosa? '
).upper()

if age >= 65:
  print('O paciente ' + name + ' POSSUI atendimento prioritário.')
elif infectiousAndContagiousDisease == 'SIM':
  print('O paciente ' + name + ' deve ser levado para sala reservada.')
else:
  print(
    'O paciente '
    + name
    + ' NÃO POSSUI atendimento prioritário e pode aguardar em sala comum.'
  )
