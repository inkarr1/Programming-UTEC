import json
import requests
api = "https://restcountries.com/v3/alpha/"
country = "br"
api = api + country
result = requests.get(api).json()
#print(json.dumps(result, indent = 4))


result = dict(result[0])
#print(json.dumps(result, indent = 4))
pais = result["name"]["official"]
print(pais)
