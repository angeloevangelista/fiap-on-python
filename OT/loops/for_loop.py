multiplicationTableNumber = int(input('Digite um número para exibir a tabuada: '))

print('Tabuada do número ', multiplicationTableNumber)

initialRangeValue = 1
finalRangeValue = 11
loopIncrementValue = 1

for value in range(initialRangeValue, finalRangeValue, loopIncrementValue):
  print(
    str(multiplicationTableNumber)
    + ' x '
    + str(value)
    + " = "
    + str(multiplicationTableNumber * value)
  )
