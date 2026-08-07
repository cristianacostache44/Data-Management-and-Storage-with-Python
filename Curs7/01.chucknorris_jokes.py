
import requests

url = "https://api.chucknorris.io/jokes/search"
topics = ["political", "china", "political&china"]

for topic in topics:
    response = requests.get(f'{url}/?query={topic}')
    data = response.json()
    print(data['result'][0]['value'])
