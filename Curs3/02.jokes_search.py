
import requests
import json

url = "https://icanhazdadjoke.com/"
headers1 = {
    "Accept" : "application/json"
}
params1 = {
    "term" : "dog"
}
response1 = requests.get(f"{url}search", params=params1, headers=headers1)

for item in response1.json()["results"]:
    print(item["joke"])