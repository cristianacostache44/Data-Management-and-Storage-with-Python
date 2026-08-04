
import json, requests

BASE_URL = "https://country.io"
NAME_PATH = "/names.json"
CAPITALS_PATH = "/capital.json"

names_response = requests.get(BASE_URL + NAME_PATH)
capitals_response = requests.get(BASE_URL + CAPITALS_PATH)

names_dict = names_response.json()
capitals_dict = capitals_response.json()

inverted_dict = {}
for short, long in names_dict.items():
    inverted_dict[long] = capitals_dict[short]

with open("tari_capitale.json", "w") as file_writer:
    json.dump(inverted_dict,file_writer)

while True:
    tara = input("A carei tari vrei sa afli capitala?")
    print(f"{tara} - {inverted_dict[tara]}")
