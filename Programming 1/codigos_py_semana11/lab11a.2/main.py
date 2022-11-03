import json
import requests

obj={
"nombre":"Juan Perez",
"edad":19,
"ciudad":"Lima"
}
"""
with open('data.json','w') as outfile:
    json.dump(obj,outfile)



with open('data.json') as json_file:
  data = json.load(json_file)
  print('Nombre: ' + data['nombre'])
  print('Edad: ' + str(data['edad']))
  print('Ciudad: ' + data['ciudad'])
  print()



data = {'personas':[{'nombre': 'Juan Perez', 'email': 'juan.perez@mail.com', 'ciudad': 'Lima'}]}
print(json.dumps(data, indent=4))


name = "Marcoandre"
url = "https://api.nationalize.io/?name=" + name
result = requests.get(url).json()
print(json.dumps(result, indent = 1))

"""
url = 'http://www.randomnumberapi.com/api/v1.0/random'
input = {
    "min": 1,
    "max": 1000,
    "count": 10
}
result = requests.get(url, data = input)
print(result.json())
