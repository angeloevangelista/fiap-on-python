import json, pathlib
from Functions import printJsonAndReturnIt

jsonPath = f'{pathlib.Path(__file__).parent.absolute()}/database.json'

printJsonAndReturnIt(jsonPath, json)

dictionary = {
  'CHAVES': ['CHAVES DO 8', '12/12/2000', 'RECEP_01'],
  'QUICO': ['QUICO FLORES', '12/12/2000', 'RAIOX_01'],
  'FLORINDA': ['FLORINDA FLORES', '12/12/2000', 'RECEP_03']
}

newJsonPath = f'{pathlib.Path(__file__).parent.absolute()}/temp_database.json'

with open(newJsonPath, 'w') as file:
  json.dump(dictionary, file, indent = 2)
