import json

with open('products.json', 'r', encoding='utf-8') as outfile:
    produtos = json.load(outfile)

print(json.dumps(produtos, indent = 4, sort_keys=True))