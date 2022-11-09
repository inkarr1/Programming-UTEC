import json
import requests
api = "https://reqres.in/api/users?page=1"

result = requests.get(api).json()
users = dict(result)
#print(json.dumps(result, indent = 2))
#print(users)


data = users["data"]
name = input("Ingrese nombre:")
for item in data:
    #print(item["first_name"])
    if item["first_name"] == name:
        print(item)
