import requests
import json
pagina = requests.get('https://jacto.com/api/v1/categories')
#print(pagina.content)
dados = json.loads(pagina.content)
print(dados)
with open('categories.json', 'w', encoding='utf-8') as outfile:
    json.dump(dados, outfile, ensure_ascii=False, indent=2)