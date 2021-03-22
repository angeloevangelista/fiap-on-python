def printJsonAndReturnIt(filePath, jsonHandler):
  with open(filePath, 'r') as jsonFile:
    jsonDictionary = jsonHandler.load(jsonFile)

    for (key, data) in jsonDictionary.items():
      print(f'{key}: {data}')

    return jsonDictionary
#
