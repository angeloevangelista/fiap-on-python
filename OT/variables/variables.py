name = input('Digite um funcionário: ')
company = input('Digite a instituição: ')
employeeAmount = int(input('Digite a quantidade de funcionários: '))
monthlyPaymentAverage = float(input('Digite a média da mensalidade: '))

print('\n')
print(name + ' trabalha na empresa ' + company)
print('Possui: ', employeeAmount, ' de funcionários.')
print('A média da mensalidade é de: ' + str(monthlyPaymentAverage))

print('\n')
print('========== DataTypes ==========')

print('\n')
print('O tipo de dado da variável [name] é: ', type(name))
print('O tipo de dado da variável [company] é: ', type(company))
print('O tipo de dado da variável [employeeAmount] é: ', type(employeeAmount))
print('O tipo de dado da variável [monthlyPaymentAverage] é: ', type(monthlyPaymentAverage))
