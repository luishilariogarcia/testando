import json

with open('markets.json', 'r', encoding='utf-8') as outfile:
    mercados = json.load(outfile)

print(json.dumps(mercados, indent = 4, sort_keys=True))