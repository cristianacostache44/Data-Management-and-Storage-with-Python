
import json, requests

base_url = "https://country.io/names.json"
response = requests.get(base_url)

with open("all_countries.json", "w") as file_writer:
    file_writer.write(response.text)