
import requests
import json

url = "https://randomuser.me/api/"

response = requests.get(url)

ladies = ['Ms','Mrs','Miss']
men = ['Mr']
random_person = ""
results = response.json()['results']
for result in results:
    name = result['name']
    if name["title"] in men:
        random_person += "Dl "
    elif name["title"] in ladies:
        random_person += "Dna "
    random_person += f"{name["first"]} {name["last"]}"
print(random_person)