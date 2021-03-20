name = input('Digite o nome: ')
age = int(input('Digite a idade: '))

if age >= 65:
  print('O paciente ' + name + ' POSSUI atendimento prioritário.')
else:
  print('O paciente ' + name + ' NÃO POSSUI atendimento prioritário.')
