import requests
import json
pagina = requests.get('https://jacto.com/api/v1/markets')
#print(pagina.content)
dados = json.loads(pagina.content)
print(dados)
with open('markets.json', 'w', encoding='utf-8') as outfile:
    json.dump(dados, outfile, ensure_ascii=False, indent=2)