with open('temp_file.py', 'r+') as file:
  lines = file.readlines()

  if len(lines) == 0:
    file.writelines('print(\' Hello, World!\')\n')
    print('File with no content, \'hello world\' added')
  else:
    for line in lines:
      print(line)
