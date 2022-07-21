import json

with open('/Users/kerri/Documents/experimental-/taxonomy.json', 'r') as item:
    data = json.load(item)

print(data['02828884'])
