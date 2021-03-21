def insert(dictionary, key, data):
  dictionary[key] = data
#

def find(dictionary, key):
  return dictionary[key]
#

def update(dictionary, key, data):
  dictionary.update(key, data)
#

def remove(dictionary, key):
  dictionary.pop(key, None)
#
