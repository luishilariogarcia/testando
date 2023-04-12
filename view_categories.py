import json

with open('categories.json', 'r', encoding='utf-8') as outfile:
    categorias = json.load(outfile)

print(json.dumps(categorias, indent = 4, sort_keys=True))